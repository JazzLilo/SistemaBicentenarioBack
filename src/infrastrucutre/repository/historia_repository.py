from prisma import Prisma
from src.core.models.historia_domain import (
    HistoriaCreate,
    HistoriaInDB,
    HistoriaUpdate,
    HistoriaWithRelations
)
from src.responses.response import Response
from typing import Optional

class HistoriaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_historia(self, historia: HistoriaCreate) -> Response:
        try:
            categoria = await self.connection.categoria.find_unique(
                where={'id': historia.id_categoria}
            )
            if not categoria:
                return Response(
                    status=404,
                    success=False,
                    message="Categoría no encontrada"
                )

            if historia.id_ubicacion:
                ubicacion = await self.connection.ubicacion.find_unique(
                    where={'id': historia.id_ubicacion}
                )
                if not ubicacion:
                    return Response(
                        status=404,
                        success=False,
                        message="Ubicación no encontrada"
                    )

            nueva_historia = await self.connection.historia.create({
                'titulo': historia.titulo,
                'descripcion': historia.descripcion,
                'fecha_inicio': historia.fecha_inicio,
                'fecha_fin': historia.fecha_fin,
                'imagen': historia.imagen,
                'id_ubicacion': historia.id_ubicacion,
                'id_categoria': historia.id_categoria
            })

            return Response(
                status=201,
                success=True,
                message="Historia creada exitosamente",
                data=HistoriaInDB.model_validate(nueva_historia)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear historia: {str(e)}"
            )

    async def obtener_historia_por_id(self, id: int) -> Response:
        try:
            historia = await self.connection.historia.find_unique(
                where={'id': id},
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )

            if not historia:
                return Response(
                    status=404,
                    success=False,
                    message="Historia no encontrada"
                )

            historia_dict = historia.model_dump()
            
            if historia.ubicacion:
                from src.core.models.ubicacion_domain import UbicacionInDB
                historia_dict['ubicacion'] = UbicacionInDB.model_validate(historia.ubicacion.model_dump())
            
            if historia.categoria:
                from src.core.models.categoria_domain import CategoriaInDB
                historia_dict['categoria'] = CategoriaInDB.model_validate(historia.categoria.model_dump())

            historia_with_relations = HistoriaWithRelations.model_validate(historia_dict)
            
            return Response(
                status=200,
                success=True,
                message="Historia encontrada",
                data=historia_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener historia: {str(e)}"
            )

    async def actualizar_historia(
        self, 
        id: int, 
        historia_data: HistoriaUpdate
    ) -> Response:
        try:
            historia_existente = await self.connection.historia.find_unique(
                where={'id': id}
            )
            if not historia_existente:
                return Response(
                    status=404,
                    success=False,
                    message="Historia no encontrada"
                )

            if historia_data.id_categoria is not None:
                categoria = await self.connection.categoria.find_unique(
                    where={'id': historia_data.id_categoria}
                )
                if not categoria:
                    return Response(
                        status=404,
                        success=False,
                        message="Categoría no encontrada"
                    )

            if historia_data.id_ubicacion is not None:
                ubicacion = await self.connection.ubicacion.find_unique(
                    where={'id': historia_data.id_ubicacion}
                )
                if not ubicacion:
                    return Response(
                        status=404,
                        success=False,
                        message="Ubicación no encontrada"
                    )

            update_data = {k: v for k, v in historia_data.model_dump().items() if v is not None}
            
            historia_actualizada = await self.connection.historia.update(
                where={'id': id},
                data=update_data,
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )

            historia_dict = historia_actualizada.model_dump()
            
            if historia_actualizada.ubicacion:
                from src.core.models.ubicacion_domain import UbicacionInDB
                historia_dict['ubicacion'] = UbicacionInDB.model_validate(historia_actualizada.ubicacion.model_dump())
            
            if historia_actualizada.categoria:
                from src.core.models.categoria_domain import CategoriaInDB
                historia_dict['categoria'] = CategoriaInDB.model_validate(historia_actualizada.categoria.model_dump())

            historia_with_relations = HistoriaWithRelations.model_validate(historia_dict)
            
            return Response(
                status=200,
                success=True,
                message="Historia actualizada exitosamente",
                data=historia_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar historia: {str(e)}"
            )

    async def eliminar_historia(self, id: int) -> Response:
        try:
            historia = await self.connection.historia.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Historia eliminada exitosamente",
                data=HistoriaInDB.model_validate(historia)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar historia: {str(e)}"
            )

    async def listar_historias(
        self, 
        skip: int = 0, 
        limit: int = 100,
        id_categoria: Optional[int] = None
    ) -> Response:
        try:
            where_clause = {}
            if id_categoria is not None:
                where_clause['id_categoria'] = id_categoria

            historias = await self.connection.historia.find_many(
                where=where_clause,
                skip=skip,
                take=limit,
                include={
                    'ubicacion': True,
                    'categoria': True
                },
                order={'fecha_inicio': 'desc'} 
            )

            historias_con_relaciones = []
            for historia in historias:
                historia_dict = historia.model_dump()
                
                if historia.ubicacion:
                    from src.core.models.ubicacion_domain import UbicacionInDB
                    historia_dict['ubicacion'] = UbicacionInDB.model_validate(historia.ubicacion.model_dump())
                
                if historia.categoria:
                    from src.core.models.categoria_domain import CategoriaInDB
                    historia_dict['categoria'] = CategoriaInDB.model_validate(historia.categoria.model_dump())
                
                historias_con_relaciones.append(
                    HistoriaWithRelations.model_validate(historia_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(historias_con_relaciones)} historias",
                data=historias_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar historias: {str(e)}"
            )

    async def buscar_historias_por_titulo(
        self, 
        titulo: str,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            historias = await self.connection.historia.find_many(
                where={
                    'titulo': {
                        'contains': titulo,
                        'mode': 'insensitive'
                    }
                },
                skip=skip,
                take=limit,
                include={
                    'ubicacion': True,
                    'categoria': True
                }
            )

            historias_con_relaciones = []
            for historia in historias:
                historia_dict = historia.model_dump()
                
                if historia.ubicacion:
                    from src.core.models.ubicacion_domain import UbicacionInDB
                    historia_dict['ubicacion'] = UbicacionInDB.model_validate(historia.ubicacion.model_dump())
                
                if historia.categoria:
                    from src.core.models.categoria_domain import CategoriaInDB
                    historia_dict['categoria'] = CategoriaInDB.model_validate(historia.categoria.model_dump())
                
                historias_con_relaciones.append(
                    HistoriaWithRelations.model_validate(historia_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(historias_con_relaciones)} historias con el título buscado",
                data=historias_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al buscar historias: {str(e)}"
            )