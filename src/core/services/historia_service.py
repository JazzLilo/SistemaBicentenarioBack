from src.infrastrucutre.repository.historia_repository import HistoriaRepository
from src.core.models.historia_domain import (
    HistoriaCreate,
    HistoriaInDB,
    HistoriaUpdate,
    HistoriaWithRelations
)
from src.responses.response import Response
from typing import Optional

class HistoriaService:
    def __init__(self, historia_repository: HistoriaRepository):
        self.historia_repository = historia_repository
        
    async def crear_historia(self, historia: HistoriaCreate) -> Response:
        return await self.historia_repository.crear_historia(historia)
    
    async def obtener_historia_por_id(self, id: int) -> Response:
        return await self.historia_repository.obtener_historia_por_id(id)
    
    async def actualizar_historia(
        self, 
        id: int, 
        historia_data: HistoriaUpdate
    ) -> Response:
        return await self.historia_repository.actualizar_historia(id, historia_data)
    
    async def eliminar_historia(self, id: int) -> Response:
        return await self.historia_repository.eliminar_historia(id)
    
    async def listar_historias(
        self, 
        skip: int = 0, 
        limit: int = 100,
        id_categoria: Optional[int] = None
    ) -> Response:
        return await self.historia_repository.listar_historias(skip, limit, id_categoria)
    
    async def buscar_historias_por_titulo(
        self, 
        titulo: str,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        return await self.historia_repository.buscar_historias_por_titulo(titulo, skip, limit)