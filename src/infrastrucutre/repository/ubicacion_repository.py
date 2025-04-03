from prisma import Prisma
from src.core.models.ubicacion_domain import (
    UbicacionCreate, 
    UbicacionInDB, 
    UbicacionUpdate
)
from src.responses.response import Response

class UbicacionRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_ubicacion(self, ubicacion: UbicacionCreate) -> Response:
        try:
            ubicacion_db = await self.connection.ubicacion.create({
                'nombre': ubicacion.nombre,
                'latitud': ubicacion.latitud,
                'longitud': ubicacion.longitud,
                'imagen': ubicacion.imagen,
                'descripcion': ubicacion.descripcion
            })
            return Response(
                status=201,
                success=True,
                message="Ubicación creada exitosamente",
                data=UbicacionInDB.model_validate(ubicacion_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear ubicación: {str(e)}"
            )

    async def obtener_ubicaciones(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            ubicaciones_db = await self.connection.ubicacion.find_many(
                skip=skip,
                take=limit,
                order={'nombre': 'asc'}
            )
            ubicaciones = [UbicacionInDB.model_validate(u) for u in ubicaciones_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(ubicaciones)} ubicaciones",
                data=ubicaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener ubicaciones: {str(e)}"
            )

    async def obtener_ubicacion_por_id(self, ubicacion_id: int) -> Response:
        try:
            ubicacion_db = await self.connection.ubicacion.find_unique(
                where={'id': ubicacion_id},
                include={
                    'historias': True,
                    'culturas': True,
                    'eventos': True
                }
            )
            if not ubicacion_db:
                return Response(
                    status=404,
                    success=False,
                    message="Ubicación no encontrada"
                )
            return Response(
                status=200,
                success=True,
                message="Ubicación encontrada",
                data=UbicacionInDB.model_validate(ubicacion_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener ubicación: {str(e)}"
            )

    async def actualizar_ubicacion(self, ubicacion_id: int, ubicacion: UbicacionUpdate) -> Response:
        try:
            data = ubicacion.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            ubicacion_db = await self.connection.ubicacion.update(
                where={'id': ubicacion_id},
                data=data
            )
            return Response(
                status=200,
                success=True,
                message="Ubicación actualizada exitosamente",
                data=UbicacionInDB.model_validate(ubicacion_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar ubicación: {str(e)}"
            )

    async def eliminar_ubicacion(self, ubicacion_id: int) -> Response:
        try:
            # Primero verificar si existe
            ubicacion = await self.connection.ubicacion.find_unique(
                where={'id': ubicacion_id}
            )
            if not ubicacion:
                return Response(
                    status=404,
                    success=False,
                    message="Ubicación no encontrada"
                )
                
            await self.connection.ubicacion.delete(
                where={'id': ubicacion_id}
            )
            return Response(
                status=200,
                success=True,
                message="Ubicación eliminada exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar ubicación: {str(e)}"
            )