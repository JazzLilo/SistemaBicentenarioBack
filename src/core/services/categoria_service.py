from src.infrastrucutre.repository.categoria_repository import CategoriaRepository
from src.responses.response import Response
from src.core.models.categoria_domain import CategoriaCreate, CategoriaUpdate, CategoriaInDB


class CategoriaService:
    
    def __init__(self, categoria_repository: CategoriaRepository):
        self.categoria_repository = categoria_repository
    
    async def crear_categoria(self, categoria: CategoriaCreate) -> Response:
        return await self.categoria_repository.crear_categoria(categoria)
    
    async def obtener_categorias(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.categoria_repository.obtener_categorias(skip, limit)
    
    async def obtener_categoria_por_id(self, categoria_id: int, include_historias: bool = False) -> Response:
        return await self.categoria_repository.obtener_categoria_por_id(categoria_id, include_historias)
    
    async def actualizar_categoria(self, categoria_id: int, categoria: CategoriaUpdate) -> Response:
        return await self.categoria_repository.actualizar_categoria(categoria_id, categoria)
    
    async def eliminar_categoria(self, categoria_id: int) -> Response:
        return await self.categoria_repository.eliminar_categoria(categoria_id)