from typing import Optional
from src.infrastrucutre.repository.presidente_repository import PresidenteRepository
from src.core.models.presidente_domain import (
    PresidenteCreate,
    PresidenteInDB,
    PresidenteUpdate
)
from src.responses.response import Response

class PresidenteService:
    def __init__(self, repository: PresidenteRepository):
        self.repository = repository

    async def crear_presidente(self, presidente: PresidenteCreate) -> Response:
        return await self.repository.crear_presidente(presidente)

    async def obtener_presidentes(
        self,
        skip: int = 0,
        limit: int = 100,
        partido: Optional[str] = None,
        periodo_activo: bool = False
    ) -> Response:
        return await self.repository.obtener_presidentes(skip, limit, partido, periodo_activo)

    async def obtener_presidente(self, presidente_id: int) -> Response:
        return await self.repository.obtener_presidente_por_id(presidente_id)

    async def actualizar_presidente(
        self,
        presidente_id: int,
        presidente: PresidenteUpdate
    ) -> Response:
        return await self.repository.actualizar_presidente(presidente_id, presidente)

    async def eliminar_presidente(self, presidente_id: int) -> Response:
        return await self.repository.eliminar_presidente(presidente_id)