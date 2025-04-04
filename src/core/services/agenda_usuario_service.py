from src.core.models.agenda_usuario_domain import (
    AgendaUsuarioBase,
    AgendaUsuarioCreate, AgendaUsuarioUpdate, AgendaUsuarioInDB,
)
from src.infrastrucutre.repository.agenda_usuario_repository import AgendaUsuarioRepository
from src.responses.response import Response
from typing import Optional

class AgendaUsuarioService:
    
    def __init__(self, repository: AgendaUsuarioRepository):
        self.repository = repository
        
    async def crear_agenda_usuario(self, agenda: AgendaUsuarioCreate) -> Response:
        return await self.repository.crear_agenda_usuario(agenda)
    
    async def obtener_agenda_por_id(self, id: int) -> Response:
        return await self.repository.obtener_agenda_por_id(id)
    
    async def actualizar_agenda_usuario(
        self, 
        id: int, 
        update_data: AgendaUsuarioUpdate
    ) -> Response:
        return await self.repository.actualizar_agenda_usuario(id, update_data)
    
    async def eliminar_agenda_usuario(self, id: int) -> Response:
        return await self.repository.eliminar_agenda_usuario(id)
    
    async def listar_agendas_por_usuario(
        self, 
        id_usuario: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        return await self.repository.listar_agendas_por_usuario(id_usuario, skip, limit)
    
    async def obtener_agenda_por_evento_usuario(
        self,
        id_usuario: int,
        id_evento_historico: Optional[int] = None,
        id_evento_agendable: Optional[int] = None
    ) -> Response:
        return await self.repository.obtener_agenda_por_evento_usuario(
            id_usuario, id_evento_historico, id_evento_agendable
        )