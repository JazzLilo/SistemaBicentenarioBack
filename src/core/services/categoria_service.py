from src.infrastrucutre.repository.categoria_repository import CategoriaRepository
from src.core.models.categoria_domain import CategoriaBase, CategoriaInDB

from src.responses.response import Response

class CategoriaService:
    def __init__(self, repository: CategoriaRepository):
        self.repository = repository

    async def get_categorias(self, skip: int = 0, limit: int = 100) -> Response:
        return await self.repository.get_categorias(skip=skip, limit=limit)

