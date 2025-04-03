from src.infrastrucutre.repository.UserRepository import UsuarioRepository
from src.responses.response import Response
from src.core.models.usuario_domain import UsuarioCreate, UsuarioUpdate
from src.mails.format_mail import verify_mail, recuperacion_pass
from src.mails.send_mail import EmailService    
from typing import Optional

class UsuarioService:
    
    def __init__(self, user_repository: UsuarioRepository, email_service: Optional[EmailService] = None):
        self.user_repository = user_repository
        self.email_service = email_service or EmailService() 
        
    async def crear_usuario(self, usuario: UsuarioCreate) -> Response:
        response = await self.user_repository.crear_usuario(usuario)
        
        if not response.success:
            return response
        
        try:
            usuario_data = response.data
            subject, html_content = verify_mail(usuario_data["verification_code"])
        
            email_sent = await self.email_service.send_email(
                receiver_email=usuario.correo,
                subject=subject,
                html_content=html_content
            )
            
            if not email_sent:
                print(f"Usuario creado pero falló el envío de correo a {usuario.correo}")
            return response
        
        except Exception as e:
            print(f"Error al enviar correo de verificación: {str(e)}")
            return response
    
    async def obtener_usuario_por_email(self, email: str) -> Response:
        return await self.user_repository.obtener_usuario_por_email(email)
    
    async def actualizar_usuario(self, usuario_id: int, usuario: UsuarioUpdate) -> Response:
        return await self.user_repository.actualizar_usuario(usuario_id, usuario)
    
    async def desactivar_usuario(self, usuario_id: int) -> Response:
        return await self.user_repository.desactivar_usuario(usuario_id)
        
    async def listar_usuarios(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.user_repository.listar_usuarios(skip, limit)

    async def verificar_codigo(self, email: str, code: str) -> Response:
        return await self.user_repository.verificar_codigo(email, code)            

    async def autenticar_usuario(self, email: str, password: str) -> Response:
        return await self.user_repository.autenticar_usuario(email, password)
    
    async def unauthenticate_usuario(self, email: str) -> Response:
        return await self.user_repository.unauthenticate_usuario(email)
    
    async def actualizar_contrasena(self, email: str, olf_contrasena: str, nueva_contrasena: str) -> Response:
        return await self.user_repository.actualizar_contrasena(email, olf_contrasena, nueva_contrasena)
    
    async def veryficar_exist_email(self, email: str) -> Response:
        return await self.user_repository.veryficar_exist_email(email)
    
    async def reset_password(self, email:str, newPassword:str) -> Response:
        return await self.user_repository.reset_password(email, newPassword)
    
    async def verificar_email_for_recovery(self, email: str) -> Response:
        response = await self.user_repository.verificar_email_for_recovery(email)
        if not response.success:
            return response
        try:
            subject, html_content = verify_mail(response.data["verification_code"])
            email_sent = await self.email_service.send_email(
                receiver_email=email,
                subject=subject,
                html_content=html_content
            )
            
            if not email_sent:
                print(f"Usuario creado pero falló el envío de correo a {email}")
            return response
        
        except Exception as e:
            print(f"Error al enviar correo de verificación: {str(e)}")
            return response