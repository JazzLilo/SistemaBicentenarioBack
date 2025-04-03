from typing import Optional, List
from prisma import Prisma
from src.core.models.tipodocumento_domain import (
    TipoDocumentoCreate,
    TipoDocumentoInDB,
    TipoDocumentoUpdate
)
from src.responses.response import Response

class TipoDocumentoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_tipodocumento(self, tipodocumento: TipoDocumentoCreate) -> Response:
        try:
            tipodocumento_db = await self.connection.tipodocumento.create(
                data={
                    'tipo': tipodocumento.tipo
                }
            )
            return Response(
                status=201,
                success=True,
                message="Tipo de documento creado exitosamente",
                data=TipoDocumentoInDB.model_validate(tipodocumento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear tipo de documento: {str(e)}"
            )

    async def obtener_tipodocumentos(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            tipodocumentos_db = await self.connection.tipodocumento.find_many(
                skip=skip,
                take=limit,
                order={'tipo': 'asc'}
            )
            tipodocumentos = [TipoDocumentoInDB.model_validate(t) for t in tipodocumentos_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(tipodocumentos)} tipos de documento",
                data=tipodocumentos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener tipos de documento: {str(e)}"
            )

    async def obtener_tipodocumento_por_id(self, id_tipo: int) -> Response:
        try:
            tipodocumento_db = await self.connection.tipodocumento.find_unique(
                where={'id_tipo': id_tipo}
            )
            if not tipodocumento_db:
                return Response(
                    status=404,
                    success=False,
                    message="Tipo de documento no encontrado"
                )
            return Response(
                status=200,
                success=True,
                message="Tipo de documento encontrado",
                data=TipoDocumentoInDB.model_validate(tipodocumento_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener tipo de documento: {str(e)}"
            )

    async def actualizar_tipodocumento(
        self,
        id_tipo: int,
        tipodocumento: TipoDocumentoUpdate
    ) -> Response:
        try:
            data = tipodocumento.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            tipodocumento_db = await self.connection.tipodocumento.update(
                where={'id_tipo': id_tipo},
                data=data
            )
            return Response(
                status=200,
                success=True,
                message="Tipo de documento actualizado exitosamente",
                data=TipoDocumentoInDB.model_validate(tipodocumento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar tipo de documento: {str(e)}"
            )

    async def eliminar_tipodocumento(self, id_tipo: int) -> Response:
        try:
            # Primero verificar si existe
            tipodocumento = await self.connection.tipodocumento.find_unique(
                where={'id_tipo': id_tipo}
            )
            if not tipodocumento:
                return Response(
                    status=404,
                    success=False,
                    message="Tipo de documento no encontrado"
                )
                
            await self.connection.tipodocumento.delete(
                where={'id_tipo': id_tipo}
            )
            return Response(
                status=200,
                success=True,
                message="Tipo de documento eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar tipo de documento: {str(e)}"
            )