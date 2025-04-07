from src.infrastrucutre.repository.ubicacion_respository import UbicacionRepository
from src.responses.response import Response
from src.core.models.ubicacion_domain import UbicacionCreate, UbicacionInDB, UbicacionWithRelations


class UbicacionService:
    def __init__(self, ubicacion_repository: UbicacionRepository):
        self.ubicacion_repository = ubicacion_repository
        
    async def crear_ubicacion(self, ubicacion: UbicacionCreate) -> Response:
        return await self.ubicacion_repository.crear_ubicacion(ubicacion)
    
    async def actualizar_ubicacion(self, id_ubicacion: int, ubicacion: UbicacionInDB) -> Response:
        return await self.ubicacion_repository.actualizar_ubicacion(id_ubicacion, ubicacion)
    
    async def obtener_ubicaciones(self, skip: int = 0, limit: int = 100, tipo: str = None) -> Response:
        return await self.ubicacion_repository.obtener_ubicaciones(skip, limit, tipo)

