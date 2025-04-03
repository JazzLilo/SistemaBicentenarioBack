from typing import Optional
from prisma import Prisma
from src.core.models.favorito_domain import (
    FavoritoCreate,
    FavoritoInDB,
    FavoritoUpdate
)
from src.responses.response import Response

class FavoritoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_favorito(self, favorito: FavoritoCreate) -> Response:
        try:
            # Verificar si ya existe
            existe = await self.connection.favorito.find_first(
                where={
                    'id_usuario': favorito.id_usuario,
                    'id_referenciado': favorito.id_referenciado
                }
            )
            if existe:
                return Response(
                    status=400,
                    success=False,
                    message="Este elemento ya está en favoritos"
                )

            favorito_db = await self.connection.favorito.create(
                data={
                    'id_usuario': favorito.id_usuario,
                    'id_referenciado': favorito.id_referenciado
                },
                include={'usuario': True}
            )
            return Response(
                status=201,
                success=True,
                message="Elemento agregado a favoritos",
                data=FavoritoInDB.model_validate(favorito_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al agregar a favoritos: {str(e)}"
            )

    async def obtener_favoritos_usuario(
        self,
        usuario_id: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            favoritos_db = await self.connection.favorito.find_many(
                skip=skip,
                take=limit,
                where={'id_usuario': usuario_id},
                order={'id': 'desc'},
                include={'usuario': True}
            )
            favoritos = [FavoritoInDB.model_validate(f) for f in favoritos_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(favoritos)} favoritos",
                data=favoritos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener favoritos: {str(e)}"
            )

    async def verificar_favorito(
        self,
        usuario_id: int,
        referenciado_id: int
    ) -> Response:
        try:
            favorito = await self.connection.favorito.find_first(
                where={
                    'id_usuario': usuario_id,
                    'id_referenciado': referenciado_id
                }
            )
            return Response(
                status=200,
                success=True,
                message="Verificación completada",
                data={'es_favorito': favorito is not None}
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al verificar favorito: {str(e)}"
            )

    async def eliminar_favorito(
        self,
        usuario_id: int,
        referenciado_id: int
    ) -> Response:
        try:
            # Primero verificar si existe
            favorito = await self.connection.favorito.find_first(
                where={
                    'id_usuario': usuario_id,
                    'id_referenciado': referenciado_id
                }
            )
            if not favorito:
                return Response(
                    status=404,
                    success=False,
                    message="Favorito no encontrado"
                )
                
            await self.connection.favorito.delete(
                where={'id': favorito.id}
            )
            return Response(
                status=200,
                success=True,
                message="Elemento eliminado de favoritos"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar de favoritos: {str(e)}"
            )