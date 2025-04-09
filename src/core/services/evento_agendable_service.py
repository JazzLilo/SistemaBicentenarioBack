from src.infrastrucutre.repository.evento_agendable_respository import EventoAgendableRepository
from src.responses.response import Response
from src.core.models.evento_agendable_domain import (
    EventoAgendableCreate,
    EventoAgendableInDB,
    EventoAgendableUpdate,
    EventoAgendableWithRelations
)

class EventoAgendableService:
    def __init__(self, evento_agendable_repository:EventoAgendableRepository):
        self.evento_agendable_repository = evento_agendable_repository
        
    async def crear_evento_agendable(self, evento: EventoAgendableCreate) -> Response:
        return await self.evento_agendable_repository.crear_evento_agendable(evento)
    
    async def obtener_eventos_agendables(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.evento_agendable_repository.obtener_eventos_agendables(skip, limit)
    
    async def obtener_evento_agendable_por_id(self, id: int) -> Response:
        return await self.evento_agendable_repository.obtener_evento_agendable_por_id(id)
    
    async def actualizar_evento_agendable(self, id: int, evento: EventoAgendableUpdate) -> Response:
        return await self.evento_agendable_repository.actualizar_evento_agendable(id, evento)
    
    async def eliminar_evento_agendable(self, id: int) -> Response:
        return await self.evento_agendable_repository.eliminar_evento_agendable(id)
    
    async def obtener_eventos_agendables_por_organizador(self, id_organizador: int) -> Response:
        return await self.evento_agendable_repository.obtener_eventos_agendables_por_organizador(id_organizador)
    
    async def obtener_categorias(self) -> Response:
        return await self.evento_agendable_repository.obtener_categorias()
    
    