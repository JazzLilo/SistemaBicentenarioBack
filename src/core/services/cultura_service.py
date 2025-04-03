from typing import Optional
from src.infrastrucutre.repository.cultura_repository import CulturaRepository
from src.core.models.cultura_domain import (
    CulturaCreate,
    CulturaInDB,
    CulturaUpdate
)
from src.responses.response import Response

class CulturaService:
    def __init__(self, repository: CulturaRepository):
        self.repository = repository

    async def crear_cultura(self, cultura: CulturaCreate) -> Response:
        return await self.repository.crear_cultura(cultura)

    async def obtener_culturas(
        self,
        skip: int = 0,
        limit: int = 100,
        ubicacion_id: Optional[int] = None
    ) -> Response:
        return await self.repository.obtener_culturas(skip, limit, ubicacion_id)

    async def obtener_cultura(self, cultura_id: int) -> Response:
        return await self.repository.obtener_cultura_por_id(cultura_id)

    async def actualizar_cultura(
        self,
        cultura_id: int,
        cultura: CulturaUpdate
    ) -> Response:
        return await self.repository.actualizar_cultura(cultura_id, cultura)

    async def eliminar_cultura(self, cultura_id: int) -> Response:
        return await self.repository.eliminar_cultura(cultura_id)