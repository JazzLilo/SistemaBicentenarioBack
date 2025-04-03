from src.infrastrucutre.repository.usuario_rol_repository import UsuarioRolRepository
from src.responses.response import Response
from src.core.models.usuario_rol_domain import UsuarioRolCreate, UsuarioRolInDB, UsuarioRolUpdate

class UsuarioRolService:
    def __init__(self, usuario_rol_repository: UsuarioRolRepository):
        self.usuario_rol_repository = usuario_rol_repository
        
    async def asignar_rol_a_usuario(self, usuario_rol: UsuarioRolCreate) -> Response:
        return await self.usuario_rol_repository.asignar_rol_a_usuario(usuario_rol)
    
    async def obtener_roles_por_usuario(self, id_usuario: int) -> Response:
        return await self.usuario_rol_repository.get_roles_by_usuario(id_usuario)
    
    async def remove_rol_from_usuario(self, id_usuario: int, id_rol: int) -> Response:
        return await self.usuario_rol_repository.remove_rol_from_usuario(id_usuario, id_rol)