from src.infrastrucutre.repository.biblioteca_repository import BibliotecaRepository
from src.responses.response import Response
from src.core.models.biblioteca_domain import BibliotecaCreate, BibliotecaUpdate, BibliotecaInDB
from typing import Optional

class BibliotecaService:
    
    def __init__(self, biblioteca_repository: BibliotecaRepository):
        self.biblioteca_repository = biblioteca_repository
        
    async def crear_biblioteca(self, biblioteca: BibliotecaCreate) -> Response:
        return await self.biblioteca_repository.crear_biblioteca(biblioteca)
    
    async def obtener_bibliotecas(
        self,
        skip: int = 0,
        limit: int = 100,
        tipo_id: Optional[int] = None,
        autor: Optional[str] = None
    ) -> Response:
        return await self.biblioteca_repository.obtener_bibliotecas(skip, limit, tipo_id, autor)
    
    
    async def obtener_biblioteca_por_id(self, biblioteca_id: int) -> Response:
        return await self.biblioteca_repository.obtener_biblioteca_por_id(biblioteca_id)
    
    async def actualizar_biblioteca(
        self,
        biblioteca_id: int,
        biblioteca: BibliotecaUpdate
    ) -> Response:
        return await self.biblioteca_repository.actualizar_biblioteca(biblioteca_id, biblioteca)
    
    async def eliminar_biblioteca(self, biblioteca_id: int) -> Response:
        return await self.biblioteca_repository.eliminar_biblioteca(biblioteca_id)