from src.core.models.multimedia_domain import MultimediaCreate, MultimediaInDB, MultimediaUpdate
from src.infrastrucutre.repository.multimedia_repository import MultimediaRespository
from src.responses.response import Response

class MultimediaService:
    
    def __init__(self, repository: MultimediaRespository):
        self.repository = repository
    
    async def crear_multimedia(self, multimedia: MultimediaCreate) -> Response:
        return await self.repository.crear_multimedia(multimedia)
    
    async def obtener_multimedia_por_evento_historico(self, id_evento_historico: int) -> Response:
        return await self.repository.obtener_multimedia_por_evento_historico(id_evento_historico)
    
    async def crear_multimedia_por_cultura(self, multimedia: MultimediaCreate) -> Response:
        return await self.repository.crear_multimedia_por_cultura(multimedia)
    
    async def obtener_multimedia_por_cultura(self, id: int) -> Response:
        return await self.repository.obtener_multimedia_por_cultura(id)
    
    async def eliminar_multimedia(self, id: int) -> Response:
        return await self.repository.eliminar_multimedia(id)