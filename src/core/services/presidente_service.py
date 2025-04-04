from src.core.models.presidente_domain import PresidenteCreate, PresidenteInDB, PresidenteUpdate
from src.responses.response import Response
from src.infrastrucutre.repository.presidente_repository import PresidenteRepository
class PresidenteService:
    def __init__(self, presidente_repository: PresidenteRepository):
        self.presidente_repository = presidente_repository
        
    async def crear_presidente(self, presidente: PresidenteCreate) -> Response:
        return await self.presidente_repository.crear_presidente(presidente)
    
    async def obtener_presidentes(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.presidente_repository.obtener_presidentes(skip, limit)
    
    async def obtener_presidente_por_id(self, presidente_id: int) -> Response:
        return await self.presidente_repository.obtener_presidente_por_id(presidente_id)
    
    async def actualizar_presidente(self, presidente_id: int, presidente: PresidenteUpdate) -> Response:
        return await self.presidente_repository.actualizar_presidente(presidente_id, presidente)
    
    async def eliminar_presidente(self, presidente_id: int) -> Response:
        return await self.presidente_repository.eliminar_presidente(presidente_id)