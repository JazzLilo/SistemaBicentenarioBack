from src.core.models.rol_domain import RolCreate, RolInDB, RolUpdate
from src.responses.response import Response
from src.infrastrucutre.repository.rol_repository import RolRepository

class RolService:
    def __init__(self, rol_repository: RolRepository):
        self.rol_repository = rol_repository

    async def crear_rol(self, rol: RolCreate) -> Response:
        return await self.rol_repository.crear_rol(rol)

    async def obtener_roles(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.rol_repository.obtener_roles(skip, limit)