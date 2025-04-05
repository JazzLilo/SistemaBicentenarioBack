from prisma import Prisma
from src.core.models.cultura_domain import (
    CulturaCreate,
    CulturaInDB,
    CulturaUpdate,
    CulturaWithRelations
)
from src.responses.response import Response
from typing import Optional

class CulturaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_cultura(self, cultura: CulturaCreate) -> Response:
        try:
            if cultura.id_ubicacion is not None:
                ubicacion = await self.connection.ubicacion.find_unique(
                    where={'id': cultura.id_ubicacion}
                )
                if not ubicacion:
                    return Response(
                        status=404,
                        success=False,
                        message="Ubicación no encontrada"
                    )

            nueva_cultura = await self.connection.cultura.create({
                'nombre': cultura.nombre,
                'descripcion': cultura.descripcion,
                'imagen': cultura.imagen,
                'id_ubicacion': cultura.id_ubicacion
            })

            return Response(
                status=201,
                success=True,
                message="Cultura creada exitosamente",
                data=CulturaInDB.model_validate(nueva_cultura)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear cultura: {str(e)}"
            )

    async def obtener_cultura_por_id(self, id: int) -> Response:
        try:
            cultura = await self.connection.cultura.find_unique(
                where={'id': id},
                include={'ubicacion': True}
            )

            if not cultura:
                return Response(
                    status=404,
                    success=False,
                    message="Cultura no encontrada"
                )

            cultura_dict = cultura.model_dump()
            
            if cultura.ubicacion:
                from src.core.models.ubicacion_domain import UbicacionInDB
                cultura_dict['ubicacion'] = UbicacionInDB.model_validate(cultura.ubicacion.model_dump())

            cultura_with_relations = CulturaWithRelations.model_validate(cultura_dict)
            
            return Response(
                status=200,
                success=True,
                message="Cultura encontrada",
                data=cultura_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener cultura: {str(e)}"
            )

    async def actualizar_cultura(
        self, 
        id: int, 
        cultura_data: CulturaUpdate
    ) -> Response:
        try:
            cultura_existente = await self.connection.cultura.find_unique(
                where={'id': id}
            )
            if not cultura_existente:
                return Response(
                    status=404,
                    success=False,
                    message="Cultura no encontrada"
                )

            if cultura_data.id_ubicacion is not None:
                ubicacion = await self.connection.ubicacion.find_unique(
                    where={'id': cultura_data.id_ubicacion}
                )
                if not ubicacion:
                    return Response(
                        status=404,
                        success=False,
                        message="Ubicación no encontrada"
                    )

            update_data = {k: v for k, v in cultura_data.model_dump().items() if v is not None}
            
            cultura_actualizada = await self.connection.cultura.update(
                where={'id': id},
                data=update_data,
                include={'ubicacion': True}
            )

            cultura_dict = cultura_actualizada.model_dump()
            
            if cultura_actualizada.ubicacion:
                from src.core.models.ubicacion_domain import UbicacionInDB
                cultura_dict['ubicacion'] = UbicacionInDB.model_validate(cultura_actualizada.ubicacion.model_dump())

            cultura_with_relations = CulturaWithRelations.model_validate(cultura_dict)
            
            return Response(
                status=200,
                success=True,
                message="Cultura actualizada exitosamente",
                data=cultura_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar cultura: {str(e)}"
            )

    async def eliminar_cultura(self, id: int) -> Response:
        try:
            cultura = await self.connection.cultura.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Cultura eliminada exitosamente",
                data=CulturaInDB.model_validate(cultura)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar cultura: {str(e)}"
            )

    async def listar_culturas(
        self, 
        skip: int = 0, 
        limit: int = 100,
        nombre: Optional[str] = None
    ) -> Response:
        try:
            where_clause = {}
            if nombre:
                where_clause['nombre'] = {
                    'contains': nombre,
                    'mode': 'insensitive'
                }

            culturas = await self.connection.cultura.find_many(
                where=where_clause,
                skip=skip,
                take=limit,
                include={'ubicacion': True},
                order={'nombre': 'asc'}  
            )

            culturas_con_relaciones = []
            for cultura in culturas:
                cultura_dict = cultura.model_dump()
                
                if cultura.ubicacion:
                    from src.core.models.ubicacion_domain import UbicacionInDB
                    cultura_dict['ubicacion'] = UbicacionInDB.model_validate(cultura.ubicacion.model_dump())
                
                culturas_con_relaciones.append(
                    CulturaWithRelations.model_validate(cultura_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(culturas_con_relaciones)} culturas",
                data=culturas_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar culturas: {str(e)}"
            )

    async def buscar_culturas_por_ubicacion(
        self, 
        id_ubicacion: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            culturas = await self.connection.cultura.find_many(
                where={'id_ubicacion': id_ubicacion},
                skip=skip,
                take=limit,
                include={'ubicacion': True}
            )

            culturas_con_relaciones = []
            for cultura in culturas:
                cultura_dict = cultura.model_dump()
                
                if cultura.ubicacion:
                    from src.core.models.ubicacion_domain import UbicacionInDB
                    cultura_dict['ubicacion'] = UbicacionInDB.model_validate(cultura.ubicacion.model_dump())
                
                culturas_con_relaciones.append(
                    CulturaWithRelations.model_validate(cultura_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(culturas_con_relaciones)} culturas para esta ubicación",
                data=culturas_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al buscar culturas por ubicación: {str(e)}"
            )