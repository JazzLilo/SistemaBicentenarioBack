from src.infrastrucutre.repository.historia_repository import HistoriaRepository
from src.responses.response import Response
from src.core.models.historia_domain import HistoriaCreate, HistoriaInDB, HistoriaUpdate
from typing import Optional

class HistoriaService:
    def __init__(self, historia_repository: HistoriaRepository):
        self.historia_repository = historia_repository
        
    async def crear_historia(self, historia: HistoriaCreate) -> Response:
        return await self.historia_repository.crear_historia(historia)
    
    async def obtener_historias(
        self,
        skip: int = 0,
        limit: int = 100,
        categoria_id: Optional[int] = None,
        ubicacion_id: Optional[int] = None
    ) -> Response:
        return await self.historia_repository.obtener_historias(skip, limit, categoria_id, ubicacion_id)
    
    async def obtener_historia_por_id(self, historia_id: int) -> Response:
        return await self.historia_repository.obtener_historia_por_id(historia_id)
    
    async def actualizar_historia(
        self,
        historia_id: int,
        historia: HistoriaUpdate
    ) -> Response:
        return await self.historia_repository.actualizar_historia(historia_id, historia)
    
    async def eliminar_historia(self, historia_id: int) -> Response:
        return await self.historia_repository.eliminar_historia(historia_id)