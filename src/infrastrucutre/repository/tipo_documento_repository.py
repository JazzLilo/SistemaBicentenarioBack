from prisma import Prisma
from src.core.models.tipo_documento_domain import (
    TipoDocumentoCreate,
    TipoDocumentoInDB,
    TipoDocumentoUpdate,
    TipoDocumentoWithRelations
)
from src.core.models.biblioteca_domain import BibliotecaInDB
from src.responses.response import Response
from typing import List

class TipoDocumentoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_tipo_documento(self, tipo_doc: TipoDocumentoCreate) -> Response:
        try:
            # Check if type already exists
            existing = await self.connection.tipodocumento.find_first(
                where={'tipo': tipo_doc.tipo}
            )
            if existing:
                return Response(
                    status=400,
                    success=False,
                    message="Este tipo de documento ya existe"
                )

            nuevo_tipo = await self.connection.tipodocumento.create(
                data={'tipo': tipo_doc.tipo}
            )

            return Response(
                status=201,
                success=True,
                message="Tipo de documento creado exitosamente",
                data=TipoDocumentoInDB.model_validate(nuevo_tipo)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear tipo de documento: {str(e)}"
            )

    async def listar_tipos_documento(
        self, 
        skip: int = 0, 
        limit: int = 100,
        incluir_bibliotecas: bool = False
    ) -> Response:
        try:
            include = {'bibliotecas': True} if incluir_bibliotecas else None
            
            tipos = await self.connection.tipodocumento.find_many(
                skip=skip,
                take=limit,
                include=include,
                order={'tipo': 'asc'}  
            )

            # Convert each type
            tipos_con_relaciones = []
            for tipo in tipos:
                tipo_dict = tipo.model_dump()
                
                if incluir_bibliotecas and tipo.bibliotecas:
                    tipo_dict['bibliotecas'] = [
                        BibliotecaInDB.model_validate(b.model_dump()) 
                        for b in tipo.bibliotecas
                    ]
                
                tipos_con_relaciones.append(
                    TipoDocumentoWithRelations.model_validate(tipo_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(tipos_con_relaciones)} tipos de documento",
                data=tipos_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar tipos de documento: {str(e)}"
            )
