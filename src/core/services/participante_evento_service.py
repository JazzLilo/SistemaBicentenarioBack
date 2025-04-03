from typing import Optional
from src.infrastrucutre.repository.participante_evento_repository import ParticipanteEventoRepository
from src.core.models.participante_evento_domain import (
    ParticipanteEventoCreate,
    ParticipanteEventoInDB,
    ParticipanteEventoUpdate
)
from src.responses.response import Response

class ParticipanteEventoService:
    def __init__(self, repository: ParticipanteEventoRepository):
        self.repository = repository

    async def registrar_participante(self, participante: ParticipanteEventoCreate) -> Response:
        return await self.repository.registrar_participante(participante)

    async def obtener_participantes_evento(
        self,
        evento_id: int,
        skip: int = 0,
        limit: int = 100,
        confirmados: Optional[bool] = None
    ) -> Response:
        return await self.repository.obtener_participantes_evento(
            evento_id, skip, limit, confirmados
        )

    async def obtener_eventos_usuario(
        self,
        usuario_id: int,
        skip: int = 0,
        limit: int = 100,
        confirmados: Optional[bool] = None
    ) -> Response:
        return await self.repository.obtener_eventos_usuario(
            usuario_id, skip, limit, confirmados
        )

    async def actualizar_asistencia(
        self,
        usuario_id: int,
        evento_id: int,
        participante: ParticipanteEventoUpdate
    ) -> Response:
        return await self.repository.actualizar_asistencia(
            usuario_id, evento_id, participante
        )

    async def eliminar_participante(
        self,
        usuario_id: int,
        evento_id: int
    ) -> Response:
        return await self.repository.eliminar_participante(usuario_id, evento_id)