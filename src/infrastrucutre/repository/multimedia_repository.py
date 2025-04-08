from src.core.models.multimedia_domain import MultimediaBase, MultimediaCreate, MultimediaInDB, MultimediaUpdate
from src.responses.response import Response
from prisma import Prisma

class MultimediaRespository:
    
    def __init__(self, connection: Prisma):
        self.connection = connection
    
    async def crear_multimedia(self, multimedia: MultimediaCreate) -> Response:
        try:
            multimedia_db = await self.connection.multimedia.create({
                'url': multimedia.url,
                'tipo': multimedia.tipo,
                'id_evento_historico': multimedia.id_evento_historico
            })
            multimedia = [MultimediaInDB.model_validate(multimedia_db.model_dump())]
            return Response(
                status=201,
                success=True,
                message="Multimedia creada exitosamente",
                data=multimedia
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear multimedia: {str(e)}"
            )
            
    
    async def obtener_multimedia_por_evento_historico(self, id_evento_historico: int) -> Response:
        try:
            multimedia_db = await self.connection.multimedia.find_many(
                where={
                    'id_evento_historico': id_evento_historico
                },
                include={
                    'evento_historico': False 
                }
            )
            multimedia = [MultimediaInDB.model_validate(m.model_dump()) for m in multimedia_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(multimedia)} multimedia",
                data=multimedia
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener multimedia: {str(e)}"
            )
    
    async def crear_multimedia_por_cultura(self, multimedia: MultimediaCreate) -> Response:
        try:
            multimedia_db = await self.connection.multimedia.create({
                'url': multimedia.url,
                'tipo': multimedia.tipo,
                'id_cultura': multimedia.id_evento_historico
            })
            multimedia = [MultimediaInDB.model_validate(multimedia_db.model_dump())]
            return Response(
                status=201,
                success=True,
                message="Multimedia creada exitosamente",
                data=multimedia
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear multimedia: {str(e)}"
            )
    
    async def obtener_multimedia_por_cultura(self, id_cultura: int) -> Response:  
        try:
            multimedia_db = await self.connection.multimedia.find_many(
                where={
                    'id_cultura': id_cultura
                }
            )
            multimedia = [MultimediaInDB.model_validate(m.model_dump()) for m in multimedia_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(multimedia)} multimedia",
                data=multimedia
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener multimedia: {str(e)}"
            )
  
    async def eliminar_multimedia(self, id: int) -> Response:
        try:
            multimedia_db = await self.connection.multimedia.delete(
                where={
                    'id': id
                }
            )
            multimedia = [MultimediaInDB.model_validate(multimedia_db.model_dump())]
            return Response(
                status=200,
                success=True,
                message="Multimedia eliminada exitosamente",
                data=multimedia
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar multimedia: {str(e)}"
            )
            