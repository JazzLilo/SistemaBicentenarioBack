from src.infrastrucutre.repository.cultura_repository import CulturaRepository
from src.core.models.cultura_domain import (
    CulturaCreate,
    CulturaUpdate,
    CulturaInDB,
    CulturaWithRelations
)
from src.responses.response import Response
from typing import Optional

class CulturaService:
    
    def __init__(self, repository: CulturaRepository):
        self.repository = repository
        
    
    async def crear_cultura(self, cultura: CulturaCreate) -> Response:
        return await self.repository.crear_cultura(cultura)

    async def obtener_cultura_por_id(self, id: int) -> Response:
        return await self.repository.obtener_cultura_por_id(id)

    async def actualizar_cultura(
        self, 
        id: int, 
        cultura_data: CulturaUpdate
    ) -> Response:
        return await self.repository.actualizar_cultura(id, cultura_data)
    
    async def eliminar_cultura(self, id: int) -> Response:
        return await self.repository.eliminar_cultura(id)
    
    async def listar_culturas(
        self, 
        skip: int = 0, 
        limit: int = 100,
        nombre: Optional[str] = None
    ) -> Response:
        return await self.repository.listar_culturas(skip, limit, nombre)
    
    async def buscar_culturas_por_ubicacion(
        self, 
        id_ubicacion: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        return await self.repository.buscar_culturas_por_ubicacion(id_ubicacion, skip, limit)