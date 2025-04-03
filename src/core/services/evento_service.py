from typing import Optional
from src.infrastrucutre.repository.evento_repository import EventoRepository
from src.core.models.evento_domain import (
    EventoCreate,
    EventoUpdate
)
from src.responses.response import Response
from datetime import datetime

class EventoService:
    def __init__(self, repository: EventoRepository):
        self.repository = repository

    async def crear_evento(self, evento: EventoCreate) -> Response:
        return await self.repository.crear_evento(evento)

    async def obtener_eventos(
        self,
        skip: int = 0,
        limit: int = 100,
        organizador_id: Optional[int] = None,
        ubicacion_id: Optional[int] = None,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None
    ) -> Response:
        return await self.repository.obtener_eventos(
            skip, limit, organizador_id, ubicacion_id, fecha_inicio, fecha_fin
        )

    async def obtener_evento(self, evento_id: int) -> Response:
        return await self.repository.obtener_evento_por_id(evento_id)

    async def actualizar_evento(
        self,
        evento_id: int,
        evento: EventoUpdate
    ) -> Response:
        return await self.repository.actualizar_evento(evento_id, evento)

    async def eliminar_evento(self, evento_id: int) -> Response:
        return await self.repository.eliminar_evento(evento_id)