from src.core.models.participante_evento_domain import (
    ParticipanteEventoCreate,
    ParticipanteEventoUpdate
)
from src.responses.response import Response
from src.infrastrucutre.repository.participante_evento_repository import ParticipanteEventoRepository

class ParticipanteEventoService:
    def __init__(self, repository: ParticipanteEventoRepository):
        self.repository = repository
        
    async def agregar_participante(self, participante: ParticipanteEventoCreate) -> Response:
        return await self.repository.agregar_participante(participante)
    
    async def obtener_participante(self, id_usuario: int, id_evento: int) -> Response:
        return await self.repository.obtener_participante(id_usuario, id_evento)
    
    async def actualizar_asistencia(
        self, 
        id_usuario: int, 
        id_evento: int, 
        update_data: ParticipanteEventoUpdate
    ) -> Response:
        return await self.repository.actualizar_asistencia(id_usuario, id_evento, update_data)
    
    async def eliminar_participante(self, id_usuario: int, id_evento: int) -> Response:
        return await self.repository.eliminar_participante(id_usuario, id_evento)
    
    
    async def listar_participantes_por_evento(self, id_evento: int) -> Response:
        return await self.repository.listar_participantes_por_evento(id_evento)
    
    async def listar_eventos_por_participante(self, id_usuario: int) -> Response:
        return await self.repository.listar_eventos_por_participante(id_usuario)