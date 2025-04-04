from prisma import Prisma
from src.core.models.presidente_domain import PresidenteCreate, PresidenteInDB, PresidenteUpdate
from src.responses.response import Response


class PresidenteRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_presidente(self, presidente: PresidenteCreate) -> Response:
        try:
            presidente_db = await self.connection.presidente.create({
                'nombre': presidente.nombre,
                'apellido': presidente.apellido,
                'imagen': presidente.imagen,
                'periodo_inicio': presidente.periodo_inicio,
                'periodo_fin': presidente.periodo_fin,
                'biografia': presidente.biografia,
                'partido_politico': presidente.partido_politico,
                'politicas_clave': presidente.politicas_clave
            })
            presidente = [PresidenteInDB.model_validate(presidente_db.model_dump())]
            return Response(
                status=201,
                success=True,
                message="Presidente creado exitosamente",
                data=presidente
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear presidente: {str(e)}"
            )
            
    async def obtener_presidentes(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            presidentes_db = await self.connection.presidente.find_many(
                skip=skip,
                take=limit,
                include={
                    'usuarios': False 
                }
            )
            presidentes = [PresidenteInDB.model_validate(p.model_dump()) for p in presidentes_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(presidentes)} presidentes",
                data=presidentes
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener presidentes: {str(e)}"
            )
    
    async def obtener_presidente_por_id(self, presidente_id: int) -> Response:
        try:
            presidente_db = await self.connection.presidente.find_unique(
                where={
                    'id': presidente_id
                }
            )
            if not presidente_db:
                return Response(
                    status=404,
                    success=False,
                    message="Presidente no encontrado",
                    data=None
                )
            presidente = PresidenteInDB.model_validate(presidente_db.model_dump())
            return Response(
                status=200,
                success=True,
                message="Presidente encontrado",
                data=presidente
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener presidente: {str(e)}"
            )
    
    async def actualizar_presidente(self, presidente_id: int, presidente: PresidenteUpdate) -> Response:
        try:
            presidente_db = await self.connection.presidente.update(
                where={
                    'id': presidente_id
                },
                data=presidente.model_dump(exclude_unset=True)
            )
            presidente = PresidenteInDB.model_validate(presidente_db.model_dump())
            return Response(
                status=200,
                success=True,
                message="Presidente actualizado exitosamente",
                data=presidente
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar presidente: {str(e)}"
            )

    async def eliminar_presidente(self, presidente_id: int) -> Response:
        try:
            presidente_db = await self.connection.presidente.delete(
                where={
                    'id': presidente_id
                }
            )
            return Response(
                status=200,
                success=True,
                message="Presidente eliminado exitosamente",
                data=presidente_db
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar presidente: {str(e)}"
            )