from typing import List, Optional
from prisma import Prisma
from src.core.models.categoria_domain import (
    CategoriaCreate,
    CategoriaInDB,
    CategoriaUpdate
)
from src.responses.response import Response

class CategoriaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_categoria(self, categoria: CategoriaCreate) -> Response:
        try:
            categoria_db = await self.connection.categoria.create({
                'nombre_categoria': categoria.nombre_categoria,
                'descripcion': categoria.descripcion
            })
            return Response(
                status=201,
                success=True,
                message="Categoría creada exitosamente",
                data=CategoriaInDB.model_validate(categoria_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear categoría: {str(e)}"
            )

    async def obtener_categorias(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            categorias_db = await self.connection.categoria.find_many(
                skip=skip,
                take=limit,
                order={'nombre_categoria': 'asc'}
            )
            categorias = [CategoriaInDB.model_validate(c) for c in categorias_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(categorias)} categorías",
                data=categorias
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener categorías: {str(e)}"
            )

    async def obtener_categoria_por_id(self, categoria_id: int, include_historias: bool = False) -> Response:
        try:
            include = {'historias': True} if include_historias else None
            categoria_db = await self.connection.categoria.find_unique(
                where={'id': categoria_id},
                include=include
            )
            if not categoria_db:
                return Response(
                    status=404,
                    success=False,
                    message="Categoría no encontrada"
                )
            return Response(
                status=200,
                success=True,
                message="Categoría encontrada",
                data=CategoriaInDB.model_validate(categoria_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener categoría: {str(e)}"
            )

    async def actualizar_categoria(self, categoria_id: int, categoria: CategoriaUpdate) -> Response:
        try:
            data = categoria.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            categoria_db = await self.connection.categoria.update(
                where={'id': categoria_id},
                data=data
            )
            return Response(
                status=200,
                success=True,
                message="Categoría actualizada exitosamente",
                data=CategoriaInDB.model_validate(categoria_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar categoría: {str(e)}"
            )

    async def eliminar_categoria(self, categoria_id: int) -> Response:
        try:
            # Primero verificar si existe
            categoria = await self.connection.categoria.find_unique(
                where={'id': categoria_id}
            )
            if not categoria:
                return Response(
                    status=404,
                    success=False,
                    message="Categoría no encontrada"
                )
                
            await self.connection.categoria.delete(
                where={'id': categoria_id}
            )
            return Response(
                status=200,
                success=True,
                message="Categoría eliminada exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar categoría: {str(e)}"
            )
            