from typing import Optional
from prisma import Prisma
from src.core.models.cultura_domain import (
    CulturaCreate,
    CulturaInDB,
    CulturaUpdate
)
from src.responses.response import Response

class CulturaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_cultura(self, cultura: CulturaCreate) -> Response:
        try:
            cultura_data = {
                'nombre': cultura.nombre,
                'imagen': cultura.imagen,
                'descripcion': cultura.descripcion,
                'id_ubicacion': cultura.id_ubicacion
            }
            cultura_db = await self.connection.cultura.create(
                data=cultura_data,
                include={'ubicacion': True}
            )
            return Response(
                status=201,
                success=True,
                message="Cultura creada exitosamente",
                data=CulturaInDB.model_validate(cultura_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear cultura: {str(e)}"
            )

    async def obtener_culturas(
        self,
        skip: int = 0,
        limit: int = 100,
        ubicacion_id: Optional[int] = None
    ) -> Response:
        try:
            where_conditions = {}
            if ubicacion_id:
                where_conditions['id_ubicacion'] = ubicacion_id

            culturas_db = await self.connection.cultura.find_many(
                skip=skip,
                take=limit,
                where=where_conditions,
                order={'nombre': 'asc'},
                include={'ubicacion': True}
            )
            culturas = [CulturaInDB.model_validate(c) for c in culturas_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(culturas)} culturas",
                data=culturas
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener culturas: {str(e)}"
            )

    async def obtener_cultura_por_id(self, cultura_id: int) -> Response:
        try:
            cultura_db = await self.connection.cultura.find_unique(
                where={'id': cultura_id},
                include={'ubicacion': True}
            )
            if not cultura_db:
                return Response(
                    status=404,
                    success=False,
                    message="Cultura no encontrada"
                )
            return Response(
                status=200,
                success=True,
                message="Cultura encontrada",
                data=CulturaInDB.model_validate(cultura_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener cultura: {str(e)}"
            )

    async def actualizar_cultura(
        self,
        cultura_id: int,
        cultura: CulturaUpdate
    ) -> Response:
        try:
            data = cultura.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            cultura_db = await self.connection.cultura.update(
                where={'id': cultura_id},
                data=data,
                include={'ubicacion': True}
            )
            return Response(
                status=200,
                success=True,
                message="Cultura actualizada exitosamente",
                data=CulturaInDB.model_validate(cultura_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar cultura: {str(e)}"
            )

    async def eliminar_cultura(self, cultura_id: int) -> Response:
        try:
            # Primero verificar si existe
            cultura = await self.connection.cultura.find_unique(
                where={'id': cultura_id}
            )
            if not cultura:
                return Response(
                    status=404,
                    success=False,
                    message="Cultura no encontrada"
                )
                
            await self.connection.cultura.delete(
                where={'id': cultura_id}
            )
            return Response(
                status=200,
                success=True,
                message="Cultura eliminada exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar cultura: {str(e)}"
            )