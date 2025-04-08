from prisma import Prisma
from src.core.models.usuario_domain import UsuarioInDB, UsuarioCreate, UsuarioUpdate, UsuarioCreateResponse    
from src.responses.response import Response
import bcrypt
from datetime import datetime, timedelta
import pytz 


class UsuarioRepository:
    
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_usuario(self, usuario: UsuarioCreate) -> Response:
        
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': usuario.correo}
            )
            await self.eliminar_por_correo(usuario.correo)
            hashed_password = self._hash_password(usuario.contrasena)
            

            usuario_db = await self.connection.usuario.create({
                **usuario.model_dump(exclude={'contrasena'}),
                'contrasena': hashed_password.decode('utf-8'), 
                'email_verified_at': usuario_db.email_verified_at,
                'estado': False 
            })
            
            print(f"Usuario creado: {usuario_db}")
            
            return Response(
                status=201,
                success=True,
                message="Usuario creado exitosamente",
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear usuario: {str(e)}"
            )

    async def obtener_usuario_por_email(self, email: str) -> Response:
        usuario_db = await self.connection.usuario.find_unique(
            where={'correo': email}
        )
        if not usuario_db:
            return Response(
                status=404,
                success=False,
                message="Usuario no encontrado"
            )
        return Response(
            status=200,
            success=True,
            message="Usuario encontrado",
            data=UsuarioInDB.model_validate(usuario_db)
        )

    async def actualizar_usuario(self, usuario_id: int, usuario: UsuarioUpdate) -> Response:
        data = usuario.model_dump(exclude_unset=True)
        if not data:
            return Response(
                status=400,
                success=False,
                message="No se proporcionaron datos para actualizar"
            )
        
        try:
            usuario_db = await self.connection.usuario.update(
                where={'id': usuario_id},
                data=data
            )
            return Response(
                status=200,
                success=True,
                message="Usuario actualizado exitosamente",
                data={
                    "usuario": usuario_db.model_dump(exclude={'contrasena', 'codeValidacion'})
            
                }
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar usuario: {str(e)}"
            )

    async def desactivar_usuario(self, usuario_id: int) -> Response:
        try:
            usuario_db = await self.connection.usuario.delete(
                where={'id': usuario_id}
            )
            return Response(
                status=200,
                success=True,
                message="Usuario desactivado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al desactivar usuario: {str(e)}"
            )
            
    async def eliminar_por_correo(self, email: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.delete(
                where={'correo': email}
            )
            return Response(
                status=200,
                success=True,
                message="Usuario eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar usuario: {str(e)}"
            )
            

    async def listar_usuarios(self, skip: int, limit: int) -> Response:
        try:
            usuarios_db = await self.connection.usuario.find_many(
                skip=skip,
                take=limit
            )
            usuarios = [UsuarioInDB.model_validate(u.model_dump()) for u in usuarios_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(usuarios)} usuarios",
                data=usuarios
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar usuarios: {str(e)}"
            )

    async def verificar_codigo(self, email: str, code: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={
                    'correo': email,
                    'codeValidacion': code
                }
            )
            
            if not usuario_db:
                return Response(
                    status=401,
                    success=False,
                    message="Código de verificación inválido o usuario no encontrado"
                )
            
            await self.connection.usuario.update(
                where={'id': usuario_db.id},
                data={
                    'estado': True,
                    'email_verified_at': datetime.now()
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Código de verificación exitoso",
            )
            
        except Exception as e:
            print(f"Error en verificación de código para {email}: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la verificación del código"
            )

    async def autenticar_usuario(self, email: str, password: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': email}
            )
            
            if not usuario_db:
                return Response(
                    status=401,
                    success=False,
                    message="Credenciales inválidas"
                )
                
            if self._usuario_bloqueado(usuario_db):
                tiempo_restante = self._calcular_tiempo_bloqueo(usuario_db)
                return Response(
                    status=403,
                    success=False,
                    message=f"Cuenta bloqueada temporalmente. Intente nuevamente en {tiempo_restante} segundos"
                )
            
            if not self._verificar_password(password, usuario_db.contrasena) or not usuario_db.email_verified_at:
                await self._registrar_intento_fallido(usuario_db)
                return Response(
                    status=401,
                    success=False,
                    message="Credenciales inválidas"
                )
            
            await self._resetear_intentos(usuario_db)
            
            usuario_dict = usuario_db.model_dump()
            usuario_validado = UsuarioInDB.model_validate(usuario_dict)
            usuario_response = usuario_validado.model_dump(exclude={'contrasena', 'codeValidacion'})
            
            return Response(
                status=200,
                success=True,
                message="Autenticación exitosa",
                data={"usuario": usuario_response}
            )
            
        except Exception as e:
            print(f"Error en autenticación para {email}: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la autenticación"
            )

    async def unauthenticate_usuario(self, email: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': email}
            )
            
            if not usuario_db:
                return Response(
                    status=404,
                    success=False,
                    message="Usuario no encontrado"
                )
            
            await self.connection.usuario.update(
                where={'id': usuario_db.id},
                data={
                    'estado': False,
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Usuario desautenticado exitosamente",
            )
            
        except Exception as e:
            print(f"Error en desautenticación para {email}: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la desautenticación"
            )

    async def actualizar_contrasena(self, email: str, olf_contrasena: str, nueva_contrasena: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': email}
            )
            
            if not usuario_db:
                return Response(
                    status=404,
                    success=False,
                    message="Usuario no encontrado"
                )
            
            if not self._verificar_password(olf_contrasena, usuario_db.contrasena):
                return Response(
                    status=401,
                    success=False,
                    message="Contraseña actual incorrecta"
                )
            
            hashed_password = self._hash_password(nueva_contrasena)
            
            await self.connection.usuario.update(
                where={'id': usuario_db.id},
                data={'contrasena': hashed_password.decode('utf-8')}
            )
            
            return Response(
                status=200,
                success=True,
                message="Contraseña actualizada exitosamente",
            )
            
        except Exception as e:
            print(f"Error en actualización de contraseña para {email}: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la actualización de contraseña"
            )
      
    async def verificar_email_for_recovery(self, email: str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': email}
            )
            
            if not usuario_db:
                return Response(
                    status=404,
                    success=False,
                    message="Correo no encontrado"
                )
            
            verification_code = self._generate_verification_code()
            
            await self.connection.usuario.update(
                where={'id': usuario_db.id},
                data={
                    'codeValidacion': verification_code,
                    'email_verified_at': None
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Código de verificación enviado",
                data={"verification_code": verification_code}
            )
            
        except Exception as e:
            print(f"Error en verificación de email para recuperación: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la verificación de email"
            )

    async def reset_password(self, email:str, newPassword:str) -> Response:
        try:
            usuario_db = await self.connection.usuario.find_unique(
                where={'correo': email}
            )
            
            if not usuario_db:
                return Response(
                    status=404,
                    success=False,
                    message="Usuario no encontrado"
                )
            
            hashed_password = self._hash_password(newPassword)
            
            await self.connection.usuario.update(
                where={'id': usuario_db.id},
                data={
                    'contrasena': hashed_password.decode('utf-8'),
                    'codeValidacion': None
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Contraseña actualizada exitosamente",
            )
            
        except Exception as e:
            print(f"Error en actualización de contraseña para {email}: {str(e)}")
            return Response(
                status=500,
                success=False,
                message="Error interno durante la actualización de contraseña"
            )

    def _usuario_bloqueado(self, usuario_db) -> bool:
        if usuario_db.cantIntentos and usuario_db.cantIntentos >= 3:
            if usuario_db.ultimoIntentoFallido:
                ultimo_intento = self._ensure_timezone(usuario_db.ultimoIntentoFallido)
                ahora = datetime.now(pytz.utc) if ultimo_intento.tzinfo else datetime.now()
                
                tiempo_transcurrido = (ahora - ultimo_intento).total_seconds()
                return tiempo_transcurrido < 10 
        return False

    def _calcular_tiempo_bloqueo(self, usuario_db) -> int:
        if usuario_db.ultimoIntentoFallido:
            ultimo_intento = self._ensure_timezone(usuario_db.ultimoIntentoFallido)
            ahora = datetime.now(pytz.utc) if ultimo_intento.tzinfo else datetime.now()
            
            tiempo_transcurrido = (ahora - ultimo_intento).total_seconds()
            return max(0, 10 - int(tiempo_transcurrido))
        return 180

    def _ensure_timezone(self, dt: datetime) -> datetime:
        if dt.tzinfo is None:
            return dt.replace(tzinfo=pytz.utc)
        return dt

    async def _registrar_intento_fallido(self, usuario_db):
        nuevos_intentos = (usuario_db.cantIntentos or 0) + 1
        await self.connection.usuario.update(
            where={'id': usuario_db.id},
            data={
                'ultimoIntentoFallido': datetime.now(pytz.utc), 
                'cantIntentos': nuevos_intentos
            }
        )
        
    async def veryficar_exist_email(self, email: str) -> Response:
        
        
        usuario_db = await self.connection.usuario.find_unique(
            where={'correo': email}
        )
        
        if not usuario_db:
            verification_code = self._generate_verification_code()
            await self.connection.usuario.create({
                'correo': email,
                'codeValidacion': verification_code,
            })
            return Response(
                status=200,
                success=True,
                message="No existe el correo",
                data={
                    "verification_code": verification_code,
                }
            )
       
        return Response(
            status=400,
            success=False,
            message="Correo Existente",
            data=usuario_db
        )
        

    async def _resetear_intentos(self, usuario_db):
        await self.connection.usuario.update(
            where={'id': usuario_db.id},
            data={
                'ultimoIntentoFallido': None,
                'cantIntentos': 0
            }
        )
    
    def _hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def _verificar_password(self, plain_password: str, hashed_password: str) -> bool:
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)
    
    def _generate_verification_code(self) -> str:
        import random
        code_length = 6
        verification_code = ''.join(random.choices('0123456789', k=code_length))
        return verification_code