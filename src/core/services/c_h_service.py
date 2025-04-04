from src.core.models.c_h_domain import (
    CategoriaEventoHistoricoCreate,
    CategoriaEventoHistoricoInDB,
)
from src.responses.response import Response
from src.infrastrucutre.repository.c_h_repository import (
    CategoriaEventoHistoricoRepository
)

class CategoriaEventoHistoricoService:
    def __init__(self, repository: CategoriaEventoHistoricoRepository):
        self.repository = repository
    
    async def crear_relacion(self, relacion: CategoriaEventoHistoricoCreate) -> Response:
        return await self.repository.crear_relacion(relacion)
    
    async def obtener_por_ids(self, id_evento: int, id_categoria: int) -> Response:
        return await self.repository.obtener_por_ids(id_evento, id_categoria)
    
    async def obtener_categorias_por_evento(self, id_evento: int) -> Response:
        return await self.repository.obtener_categorias_por_evento(id_evento)
    
    async def obtener_eventos_por_categoria(self, id_categoria: int) -> Response:
        return await self.repository.obtener_eventos_por_categoria(id_categoria)
    
    async def eliminar_relacion(self, id_evento: int, id_categoria: int) -> Response:
        return await self.repository.eliminar_relacion(id_evento, id_categoria)