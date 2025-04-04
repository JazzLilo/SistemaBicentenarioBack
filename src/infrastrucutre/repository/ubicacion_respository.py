from prisma import Prisma
from src.core.models.ubicacion_domain import UbicacionCreate, UbicacionInDB, UbicacionUpdate
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
            
            id_ubicacion = ubicacion_db.id
            
            return Response(
                status=201,
                success=True,   
                message="Ubicación creada exitosamente",
                data=id_ubicacion
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear ubicación: {str(e)}"
            )
    
    async def obtener_ubicaciones(self, skip: int = 0, limit: int = 100, tipo:str = None) -> Response:
        try:
            include_options = {
                'historias': False,
                'culturas': False,
                'eventos_historicos': False,
                'eventos_agendables': False
            }

            filtros = {}

            if tipo in include_options:
                filtros[f"{tipo}.some"] = {}  
                include_options[tipo] = True  

            ubicaciones_db = await self.connection.ubicacion.find_many(
                where=filtros,
                skip=skip,
                take=limit,
                include=include_options
            )

            ubicaciones = [UbicacionInDB.model_validate(u.model_dump()) for u in ubicaciones_db]
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(ubicaciones)} ubicaciones con {tipo}" if tipo else "Se encontraron ubicaciones",
                data=ubicaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener ubicaciones: {str(e)}"
            )

        