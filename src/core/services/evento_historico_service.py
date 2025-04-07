from src.core.models.evento_historico_domain import EventoHistoricoCreate, EventoHistoricoInDB, EventoHistoricoUpdate
from src.responses.response import Response
from src.infrastrucutre.repository.evento_historico_repository import EventoHistoricoRepository

class EventoHistoricoService:
    
    def __init__(self, evento_historico_repository: EventoHistoricoRepository):
        self.evento_historico_repository = evento_historico_repository
        
    async def crear_evento_historico(self, evento_historico: EventoHistoricoCreate) -> Response:
        return await self.evento_historico_repository.crear_evento_historico(evento_historico)
    
    async def obtener_eventos_historicos(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.evento_historico_repository.obtener_eventos_historicos(skip, limit)
    
    async def obtener_evento_historico_por_id(self, id: int) -> Response:
        return await self.evento_historico_repository.obtener_evento_historico_por_id(id)
    
    async def actualizar_evento_historico(self, id: int, evento_historico: EventoHistoricoUpdate) -> Response:
        return await self.evento_historico_repository.editar_evento_historico(id, evento_historico)
    
    async def eliminar_evento_historico(self, id: int) -> Response:
        return await self.evento_historico_repository.eliminar_evento_historico(id)