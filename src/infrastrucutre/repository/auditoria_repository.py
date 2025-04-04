from prisma import Prisma
from src.core.models.auditoria_domain import AuditoriaCreate, AuditoriaInDB, AuditoriaUpdate
from src.responses.response import Response

class AuditoriaRepository:
    
    def __init__(self, connection: Prisma):
        self.connection = connection
        
    async def create_auditoria(self, auditoria: AuditoriaCreate) -> Response:
        try:
            auditoria_db = await self.connection.auditoria.create({
                'tipo': auditoria.tipo,
                'detalle': auditoria.detalle,
                'id_usuario': auditoria.id_usuario
            })
                        
            return Response(
                status=201,
                success=True,
                message="Auditoria created successfully",
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error creating auditoria: {str(e)}"
            )
            
    async def get_all_auditorias(self) -> Response:
        try:
            auditorias_db = await self.connection.auditoria.find_many(
                include={'usuario': True}  
            )
            
            if not auditorias_db:
                return Response(
                    status=404,
                    success=False,
                    message="No auditorias found",
                    data=[]
                )
            data_auditorias = [AuditoriaInDB.model_validate(auditoria.model_dump()) for auditoria in auditorias_db]
            return Response(
                status=200,
                success=True,
                message="Auditorias found",
                data=[data_auditorias]
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error fetching auditorias: {str(e)}"
            )
            
    async def get_auditoria_by_user_id(self, id_usuario: int) -> Response:
        try:
            auditorias_db = await self.connection.auditoria.find_many(
                where={'id_usuario': id_usuario},
                include={'usuario': True} 
            )
            
            if not auditorias_db:
                return Response(
                    status=404,
                    success=False,
                    message="No auditorias found for the specified user",
                    data=[]
                )
            
            data_auditorias = [AuditoriaInDB.model_validate(auditoria.model_dump()) for auditoria in auditorias_db]
            return Response(
                status=200,
                success=True,
                message="Auditorias found",
                data=data_auditorias
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error fetching auditorias: {str(e)}"
            )
