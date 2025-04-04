from src.infrastrucutre.repository.auditoria_repository import AuditoriaRepository
from src.core.models.auditoria_domain import AuditoriaCreate, AuditoriaInDB, AuditoriaUpdate
from src.responses.response import Response

class AuditoriaService:
    def __init__(self, auditoria_repository: AuditoriaRepository):
        self.auditoria_repository = auditoria_repository
        
    async def create_auditoria(self, auditoria: AuditoriaCreate) -> Response:
        return await self.auditoria_repository.create_auditoria(auditoria)
    
    async def get_all_auditorias(self) -> Response:
        return await self.auditoria_repository.get_all_auditorias()
    
    async def get_auditoria_by_user_id(self, id_usuario: int) -> Response:
        return await self.auditoria_repository.get_auditoria_by_user_id(id_usuario)
