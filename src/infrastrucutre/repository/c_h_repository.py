from prisma import Prisma
from src.core.models.c_h_domain import (
    CategoriaEventoHistoricoCreate,
    CategoriaEventoHistoricoInDB,
)
from src.responses.response import Response

class CategoriaEventoHistoricoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection
        
    async def crear_relacion(self, relacion: CategoriaEventoHistoricoCreate) -> Response:
        try:
            existente = await self.connection.categoriaeventohistorico.find_first(
                where={
                    'id_evento': relacion.id_evento,
                    'id_categoria': relacion.id_categoria
                }
            )
            if existente:
                return Response(
                    status=400,
                    success=False,
                    message="La relación ya existe"
                )
                
            nueva_relacion = await self.connection.categoriaeventohistorico.create(
                data=relacion.model_dump()
            )
            
            return Response(
                status=201,
                success=True,
                message="Relación creada exitosamente",
                data=CategoriaEventoHistoricoInDB.model_validate(nueva_relacion)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear relación: {str(e)}"
            )
    
    async def obtener_por_ids(self, id_evento: int, id_categoria: int) -> Response:
        try:
            relacion = await self.connection.categoriaeventohistorico.find_first(
                where={
                    'id_evento': id_evento,
                    'id_categoria': id_categoria
                },
                include={
                    'categoria': True,
                    'evento': True
                }
            )
            
            if not relacion:
                return Response(
                    status=404,
                    success=False,
                    message="Relación no encontrada"
                )
                
            return Response(
                status=200,
                success=True,
                message="Relación encontrada",
                data=CategoriaEventoHistoricoInDB.model_validate(relacion)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener relación: {str(e)}"
            )
    
    async def obtener_categorias_por_evento(self, id_evento: int) -> Response:
        try:
            relaciones = await self.connection.categoriaeventohistorico.find_many(
                where={'id_evento': id_evento},
                include={'categoria': True}
            )
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(relaciones)} categorías para el evento",
                data=[CategoriaEventoHistoricoInDB.model_validate(r) for r in relaciones]
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener categorías: {str(e)}"
            )
    
    async def obtener_eventos_por_categoria(self, id_categoria: int) -> Response:
        try:
            relaciones = await self.connection.categoriaeventohistorico.find_many(
                where={'id_categoria': id_categoria},
                include={'evento': True}
            )
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(relaciones)} eventos para la categoría",
                data=[CategoriaEventoHistoricoInDB.model_validate(r) for r in relaciones]
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener eventos: {str(e)}"
            )
    
    async def eliminar_relacion(self, id_evento: int, id_categoria: int) -> Response:
        try:
            relacion = await self.connection.categoriaeventohistorico.delete_many(
                where={
                    'id_evento': id_evento,
                    'id_categoria': id_categoria
                }
            )
            
            if relacion.count == 0:
                return Response(
                    status=404,
                    success=False,
                    message="No se encontró la relación"
                )
                
            return Response(
                status=200,
                success=True,
                message="Relación eliminada exitosamente"
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar relación: {str(e)}"
            )