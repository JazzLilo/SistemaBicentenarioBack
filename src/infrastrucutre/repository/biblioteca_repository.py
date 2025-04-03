from typing import Optional
from prisma import Prisma
from src.core.models.biblioteca_domain import (
    BibliotecaCreate,
    BibliotecaInDB,
    BibliotecaUpdate
)
from src.responses.response import Response

class BibliotecaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_biblioteca(self, biblioteca: BibliotecaCreate) -> Response:
        try:
            biblioteca_data = {
                'titulo': biblioteca.titulo,
                'autor': biblioteca.autor,
                'imagen': biblioteca.imagen,
                'fecha_publicacion': biblioteca.fecha_publicacion,
                'edicion': biblioteca.edicion,
                'id_tipo': biblioteca.id_tipo,
                'fuente': biblioteca.fuente,
                'enlace': biblioteca.enlace
            }
            biblioteca_db = await self.connection.biblioteca.create(
                data=biblioteca_data,
                include={'tipo': True}
            )
            return Response(
                status=201,
                success=True,
                message="Recurso bibliográfico creado exitosamente",
                data=BibliotecaInDB.model_validate(biblioteca_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear recurso bibliográfico: {str(e)}"
            )

    async def obtener_bibliotecas(
        self,
        skip: int = 0,
        limit: int = 100,
        tipo_id: Optional[int] = None,
        autor: Optional[str] = None
    ) -> Response:
        try:
            where_conditions = {}
            if tipo_id:
                where_conditions['id_tipo'] = tipo_id
            if autor:
                where_conditions['autor'] = {'contains': autor}

            bibliotecas_db = await self.connection.biblioteca.find_many(
                skip=skip,
                take=limit,
                where=where_conditions,
                order={'titulo': 'asc'},
                include={'tipo': True}
            )
            bibliotecas = [BibliotecaInDB.model_validate(b) for b in bibliotecas_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(bibliotecas)} recursos bibliográficos",
                data=bibliotecas
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener recursos bibliográficos: {str(e)}"
            )

    async def obtener_biblioteca_por_id(self, biblioteca_id: int) -> Response:
        try:
            biblioteca_db = await self.connection.biblioteca.find_unique(
                where={'id': biblioteca_id},
                include={'tipo': True}
            )
            if not biblioteca_db:
                return Response(
                    status=404,
                    success=False,
                    message="Recurso bibliográfico no encontrado"
                )
            return Response(
                status=200,
                success=True,
                message="Recurso bibliográfico encontrado",
                data=BibliotecaInDB.model_validate(biblioteca_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener recurso bibliográfico: {str(e)}"
            )

    async def actualizar_biblioteca(
        self,
        biblioteca_id: int,
        biblioteca: BibliotecaUpdate
    ) -> Response:
        try:
            data = biblioteca.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            biblioteca_db = await self.connection.biblioteca.update(
                where={'id': biblioteca_id},
                data=data,
                include={'tipo': True}
            )
            return Response(
                status=200,
                success=True,
                message="Recurso bibliográfico actualizado exitosamente",
                data=BibliotecaInDB.model_validate(biblioteca_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar recurso bibliográfico: {str(e)}"
            )

    async def eliminar_biblioteca(self, biblioteca_id: int) -> Response:
        try:
            # Primero verificar si existe
            biblioteca = await self.connection.biblioteca.find_unique(
                where={'id': biblioteca_id}
            )
            if not biblioteca:
                return Response(
                    status=404,
                    success=False,
                    message="Recurso bibliográfico no encontrado"
                )
                
            await self.connection.biblioteca.delete(
                where={'id': biblioteca_id}
            )
            return Response(
                status=200,
                success=True,
                message="Recurso bibliográfico eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar recurso bibliográfico: {str(e)}"
            )