from prisma import Prisma
from src.core.models.rol_domain import RolCreate, RolInDB, RolUpdate
from src.responses.response import Response

class RolRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_rol(self, rol: RolCreate) -> Response:
        try:
            rol_db = await self.connection.rol.create({
                'nombre_rol': rol.nombre_rol,
                'descripcion': rol.descripcion
            })
            rol = [RolInDB.model_validate(rol_db.model_dump())]
            return Response(
                status=201,
                success=True,
                message="Rol creado exitosamente",
                data=rol
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear rol: {str(e)}"
            )

    async def obtener_roles(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            roles_db = await self.connection.rol.find_many(
                skip=skip,
                take=limit,
                include={
                    'usuarios': False 
                }
            )
            roles = [RolInDB.model_validate(r.model_dump()) for r in roles_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(roles)} roles",
                data=roles
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener roles: {str(e)}"
            )