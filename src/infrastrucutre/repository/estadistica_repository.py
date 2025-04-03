from typing import Optional
from prisma import Prisma
from src.core.models.estadistica_domain import (
    EstadisticaCreate,
    EstadisticaInDB,
    EstadisticaUpdate,
    EstadisticaTipo
)
from src.responses.response import Response

class EstadisticaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_estadistica(self, estadistica: EstadisticaCreate) -> Response:
        try:
            estadistica_db = await self.connection.estadistica.create(
                data={
                    'tipo': estadistica.tipo.value,
                    'detalle': estadistica.detalle,
                    'id_usuario': estadistica.id_usuario
                },
                include={'usuario': True}
            )
            return Response(
                status=201,
                success=True,
                message="Registro estadístico creado",
                data=EstadisticaInDB.model_validate(estadistica_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear estadística: {str(e)}"
            )

    async def obtener_estadisticas(
        self,
        skip: int = 0,
        limit: int = 100,
        tipo: Optional[EstadisticaTipo] = None,
        usuario_id: Optional[int] = None,
        fecha_inicio: Optional[str] = None,
        fecha_fin: Optional[str] = None
    ) -> Response:
        try:
            where_conditions = {}
            if tipo:
                where_conditions['tipo'] = tipo.value
            if usuario_id:
                where_conditions['id_usuario'] = usuario_id
            if fecha_inicio and fecha_fin:
                where_conditions['fecha'] = {
                    'gte': fecha_inicio,
                    'lte': fecha_fin
                }

            estadisticas_db = await self.connection.estadistica.find_many(
                skip=skip,
                take=limit,
                where=where_conditions,
                order={'fecha': 'desc'},
                include={'usuario': True}
            )
            estadisticas = [EstadisticaInDB.model_validate(e) for e in estadisticas_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(estadisticas)} registros",
                data=estadisticas
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener estadísticas: {str(e)}"
            )

    async def obtener_estadistica_por_id(self, estadistica_id: int) -> Response:
        try:
            estadistica_db = await self.connection.estadistica.find_unique(
                where={'id': estadistica_id},
                include={'usuario': True}
            )
            if not estadistica_db:
                return Response(
                    status=404,
                    success=False,
                    message="Registro estadístico no encontrado"
                )
            return Response(
                status=200,
                success=True,
                message="Registro encontrado",
                data=EstadisticaInDB.model_validate(estadistica_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener estadística: {str(e)}"
            )

    async def actualizar_estadistica(
        self,
        estadistica_id: int,
        estadistica: EstadisticaUpdate
    ) -> Response:
        try:
            data = estadistica.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            estadistica_db = await self.connection.estadistica.update(
                where={'id': estadistica_id},
                data=data,
                include={'usuario': True}
            )
            return Response(
                status=200,
                success=True,
                message="Registro actualizado",
                data=EstadisticaInDB.model_validate(estadistica_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar estadística: {str(e)}"
            )

    async def eliminar_estadistica(self, estadistica_id: int) -> Response:
        try:
            # Verificar existencia
            estadistica = await self.connection.estadistica.find_unique(
                where={'id': estadistica_id}
            )
            if not estadistica:
                return Response(
                    status=404,
                    success=False,
                    message="Registro estadístico no encontrado"
                )
                
            await self.connection.estadistica.delete(
                where={'id': estadistica_id}
            )
            return Response(
                status=200,
                success=True,
                message="Registro eliminado"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar estadística: {str(e)}"
            )

    async def obtener_metricas(
        self,
        tipo: Optional[EstadisticaTipo] = None,
        fecha_inicio: Optional[str] = None,
        fecha_fin: Optional[str] = None
    ) -> Response:
        try:
            where_conditions = {}
            if tipo:
                where_conditions['tipo'] = tipo.value
            if fecha_inicio and fecha_fin:
                where_conditions['fecha'] = {
                    'gte': fecha_inicio,
                    'lte': fecha_fin
                }

            # Conteo total
            total = await self.connection.estadistica.count(
                where=where_conditions
            )

            # Conteo por tipo
            conteo_por_tipo = await self.connection.estadistica.group_by(
                by=['tipo'],
                where=where_conditions,
                count=True
            )

            return Response(
                status=200,
                success=True,
                message="Métricas obtenidas",
                data={
                    'total': total,
                    'por_tipo': conteo_por_tipo
                }
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener métricas: {str(e)}"
            )