from src.infrastrucutre.repository.tipo_documento_repository import TipoDocumentoRepository
from src.core.models.tipo_documento_domain import (
    TipoDocumentoCreate,
    TipoDocumentoInDB,
    TipoDocumentoUpdate,
    TipoDocumentoWithRelations
)
from src.core.models.biblioteca_domain import BibliotecaInDB
from src.responses.response import Response
from typing import List


class TipoDocumentoService:
    
    def __init__(self, tipo_documento_repository: TipoDocumentoRepository):
        self.tipo_documento_repository = tipo_documento_repository
        
    async def crear_tipo_documento(self, tipo_doc: TipoDocumentoCreate) -> Response:
        return await self.tipo_documento_repository.crear_tipo_documento(tipo_doc)
    
    async def listar_tipos_documento(
        self, 
        skip: int = 0, 
        limit: int = 100,
        incluir_bibliotecas: bool = False
    ) -> Response:
        return await self.tipo_documento_repository.listar_tipos_documento(
            skip=skip,
            limit=limit,
            incluir_bibliotecas=incluir_bibliotecas
        )