from typing import List, Optional
from prisma import Prisma
from src.core.models.usuario_rol_domain import UsuarioRolCreate, UsuarioRolInDB, UsuarioRolUpdate
from src.responses.response import Response

class UsuarioRolRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection


    async def asignar_rol_a_usuario(self, usuario_rol: UsuarioRolCreate) -> Response:
        try:
            usuario_rol_db = await self.connection.usuariorol.create({
                'id_usuario': usuario_rol.id_usuario,
                'id_rol': usuario_rol.id_rol
            }, include={'usuario': True, 'rol': True})
            user_rol = [UsuarioRolInDB.model_validate(usuario_rol_db.model_dump())]
            return Response(
                status=201,
                success=True,
                message="Rol asignado exitosamente",
                data=user_rol
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al asignar rol: {str(e)}"
            )

    async def get_roles_by_usuario(self, id_usuario: int) -> Response:
        try:
            usuario_rol_db = await self.connection.usuariorol.find_many(
                where={'id_usuario': id_usuario},
                include={'rol': True}
            )
            
            if not usuario_rol_db:
                return Response(
                    status=404,
                    success=False,
                    message="No se encontraron roles para el usuario especificado",
                    data=[]
                )
            
            return Response(
                status=200,
                success=True,
                message="Roles encontrados",
                data=[UsuarioRolInDB.model_validate(ur.model_dump()) for ur in usuario_rol_db]
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al obtener roles: {str(e)}"
            )
    
    async def remove_rol_from_usuario(self, id_usuario: int, id_rol: int) -> Response:
        try:
            deleted_count = await self.connection.usuariorol.delete_many(
                where={
                    'AND': [
                        {'id_usuario': id_usuario},
                        {'id_rol': id_rol}
                    ]
                }
            )
            
            if deleted_count == 0:
                return Response(
                    status=404,
                    success=False,
                    message="No se encontró la relación de rol para eliminar",
                    data=[]
                )
            
            return Response(
                status=200,
                success=True,
                message="Rol eliminado exitosamente",
                data=[]
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar rol: {str(e)}"
            )