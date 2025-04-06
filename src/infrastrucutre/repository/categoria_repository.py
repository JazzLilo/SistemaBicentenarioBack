from prisma import Prisma
from src.core.models.categoria_domain import CategoriaBase, CategoriaInDB, CategoriaWithRelations

from src.responses.response import Response

class CategoriaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection
    
    async def get_categorias(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            categorias_db = await self.connection.categoria.find_many(
                skip=skip,
                take=limit
            )
            categorias = [CategoriaInDB.model_validate(categoria_db.model_dump()) for categoria_db in categorias_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(categorias)} categorias",
                data=categorias
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener las categorias: {str(e)}"
            )