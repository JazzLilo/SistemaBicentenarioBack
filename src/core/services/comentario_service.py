from src.infrastrucutre.repository.comentario_repository import ComentarioRepository
from src.responses.response import Response
from src.core.models.comentario_domain import ComentarioCreate, ComentarioUpdate
from typing import Optional

class ComentarioService:
    
    def __init__(self, comentario_repository: ComentarioRepository):
        self.comentario_repository = comentario_repository
        
    async def crear_comentario(self, comentario: ComentarioCreate) -> Response:
        return await self.comentario_repository.crear_comentario(comentario)

    async def obtener_comentarios(
        self,
        skip: int = 0,
        limit: int = 100,
        usuario_id: Optional[int] = None,
        biblioteca_id: Optional[int] = None,
        evento_id: Optional[int] = None
    ) -> Response:
        return await self.comentario_repository.obtener_comentarios(skip, limit, usuario_id, biblioteca_id, evento_id)
    
    async def obtener_comentario_por_id(self, comentario_id: int) -> Response:
        return await self.comentario_repository.obtener_comentario_por_id(comentario_id)
    
    async def actualizar_comentario(
        self,
        comentario_id: int,
        comentario: ComentarioUpdate
    ) -> Response:
        return await self.comentario_repository.actualizar_comentario(comentario_id, comentario)
    
    async def eliminar_comentario(self, comentario_id: int) -> Response:
        return await self.comentario_repository.eliminar_comentario(comentario_id)