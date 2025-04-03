from src.infrastrucutre.repository.ubicacion_repository import UbicacionRepository
from src.responses.response import Response
from src.core.models.ubicacion_domain import UbicacionCreate, UbicacionUpdate, UbicacionInDB

class UbicacionService:
    def __init__(self, ubicacion_repository):
        self.ubicacion_repository = ubicacion_repository
    
    async def crear_ubicacion(self, ubicacion: UbicacionCreate) -> Response:
        return await self.ubicacion_repository.crear_ubicacion(ubicacion)
    async def obtener_ubicaciones(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.ubicacion_repository.obtener_ubicaciones(skip, limit)
        
    async def obtener_ubicacion_por_id(self, ubicacion_id: int) -> Response:
        return await self.ubicacion_repository.obtener_ubicacion_por_id(ubicacion_id)
        
    async def actualizar_ubicacion(self, ubicacion_id: int, ubicacion: UbicacionUpdate) -> Response:
        return await self.ubicacion_repository.actualizar_ubicacion(ubicacion_id, ubicacion)
        
    async def eliminar_ubicacion(self, ubicacion_id: int) -> Response:
        return await self.ubicacion_repository.eliminar_ubicacion(ubicacion_id)