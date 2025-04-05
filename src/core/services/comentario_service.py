from src.core.models.comentario_domain import (
    ComentarioCreate,
    ComentarioInDB,
    ComentarioUpdate,
    ComentarioWithRelations
)
from src.core.models.biblioteca_domain import BibliotecaInDB
from src.core.models.usuario_domain import UsuarioInDB
from src.core.models.evento_agendable_domain import EventoAgendableInDB
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.responses.response import Response
from typing import Optional
from src.infrastrucutre.repository.comentario_repository import ComentarioRepository


class ComentarioService:
    def __init__(self, repository: ComentarioRepository):
        self.comentario_repository = repository
        
        
    async def crear_comentario(self, comentario: ComentarioCreate) -> Response:
        return await self.comentario_repository.crear_comentario(comentario)
    
    async def obtener_comentario(self, id: int) -> Response:
        return await self.comentario_repository.obtener_comentario(id)
    
    async def actualizar_comentario(
        self, 
        id: int, 
        update_data: ComentarioUpdate
    ) -> Response:
        return await self.comentario_repository.actualizar_comentario(id, update_data)
    
    async def eliminar_comentario(self, id: int) -> Response:
        return await self.comentario_repository.eliminar_comentario(id)
    
    
    async def listar_comentarios_por_entidad(
        self,
        id_biblioteca: Optional[int] = None,
        id_evento_agendable: Optional[int] = None,
        id_evento_historico: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        return await self.comentario_repository.listar_comentarios_por_entidad(
            id_biblioteca,
            id_evento_agendable,
            id_evento_historico,
            skip,
            limit
        )
        
    async def listar_comentarios_por_usuario(
            self,
            id_usuario: int,
            skip: int = 0,
            limit: int = 100
        ) -> Response:
        return await self.comentario_repository.listar_comentarios_por_usuario(
                id_usuario,
                skip,
                limit
            )