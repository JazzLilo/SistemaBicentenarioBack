from src.core.models.biblioteca_domain import (
    BibliotecaCreate,
    BibliotecaInDB,
    BibliotecaUpdate,
    BibliotecaWithRelations
)
from src.responses.response import Response
from src.core.models.tipo_documento_domain import TipoDocumentoInDB
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.core.models.comentario_domain import ComentarioInDB
from typing import List, Optional
from src.infrastrucutre.repository.biblioteca_repository import BibliotecaRepository

class BibliotecaService:
    def __init__(self, repository: BibliotecaRepository):
        self.repository = repository
        
    
    async def crear_biblioteca(self, biblioteca: BibliotecaCreate) -> Response:
        return await self.repository.crear_biblioteca(biblioteca)
    
    async def obtener_biblioteca(self, id: int) -> Response:
        return await self.repository.obtener_biblioteca(id)
    
    async def actualizar_biblioteca(
        self, 
        id: int, 
        update_data: BibliotecaUpdate
    ) -> Response:
        return await self.repository.actualizar_biblioteca(id, update_data)
    
    async def eliminar_biblioteca(self, id: int) -> Response:
        return await self.repository.eliminar_biblioteca(id)
    
    async def listar_bibliotecas(
        self, 
        skip: int = 0, 
        limit: int = 100,
        id_tipo: Optional[int] = None,
        titulo: Optional[str] = None
    ) -> Response:
        return await self.repository.listar_bibliotecas(skip, limit, id_tipo, titulo)
    
    async def buscar_bibliotecas_por_autor(
        self, 
        autor: str,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        return await self.repository.buscar_bibliotecas_por_autor(autor, skip, limit)