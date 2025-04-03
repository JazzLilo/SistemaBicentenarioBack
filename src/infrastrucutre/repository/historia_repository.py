from typing import Optional
from prisma import Prisma
from src.core.models.historia_domain import (
    HistoriaCreate,
    HistoriaInDB,
    HistoriaUpdate
)
from src.responses.response import Response

class HistoriaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_historia(self, historia: HistoriaCreate) -> Response:
        try:
            historia_data = {
                'titulo': historia.titulo,
                'descripcion': historia.descripcion,
                'fecha_inicio': historia.fecha_inicio,
                'fecha_fin': historia.fecha_fin,
                'imagen': historia.imagen,
                'id_ubicacion': historia.id_ubicacion,
                'id_categoria': historia.id_categoria
            }
            historia_db = await self.connection.historia.create(
                data=historia_data,
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )
            return Response(
                status=201,
                success=True,
                message="Historia creada exitosamente",
                data=HistoriaInDB.model_validate(historia_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear historia: {str(e)}"
            )

    async def obtener_historias(
        self,
        skip: int = 0,
        limit: int = 100,
        categoria_id: Optional[int] = None,
        ubicacion_id: Optional[int] = None
    ) -> Response:
        try:
            where_conditions = {}
            if categoria_id:
                where_conditions['id_categoria'] = categoria_id
            if ubicacion_id:
                where_conditions['id_ubicacion'] = ubicacion_id

            historias_db = await self.connection.historia.find_many(
                skip=skip,
                take=limit,
                where=where_conditions,
                order={'titulo': 'asc'},
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )
            historias = [HistoriaInDB.model_validate(h) for h in historias_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(historias)} historias",
                data=historias
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener historias: {str(e)}"
            )

    async def obtener_historia_por_id(self, historia_id: int) -> Response:
        try:
            historia_db = await self.connection.historia.find_unique(
                where={'id': historia_id},
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )
            if not historia_db:
                return Response(
                    status=404,
                    success=False,
                    message="Historia no encontrada"
                )
            return Response(
                status=200,
                success=True,
                message="Historia encontrada",
                data=HistoriaInDB.model_validate(historia_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener historia: {str(e)}"
            )

    async def actualizar_historia(
        self,
        historia_id: int,
        historia: HistoriaUpdate
    ) -> Response:
        try:
            data = historia.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            historia_db = await self.connection.historia.update(
                where={'id': historia_id},
                data=data,
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )
            return Response(
                status=200,
                success=True,
                message="Historia actualizada exitosamente",
                data=HistoriaInDB.model_validate(historia_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar historia: {str(e)}"
            )

    async def eliminar_historia(self, historia_id: int) -> Response:
        try:
            historia = await self.connection.historia.find_unique(
                where={'id': historia_id}
            )
            if not historia:
                return Response(
                    status=404,
                    success=False,
                    message="Historia no encontrada"
                )
                
            await self.connection.historia.delete(
                where={'id': historia_id}
            )
            return Response(
                status=200,
                success=True,
                message="Historia eliminada exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar historia: {str(e)}"
            )
            