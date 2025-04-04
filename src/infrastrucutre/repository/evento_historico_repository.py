from prisma import Prisma
from src.core.models.evento_historico_domain import EventoHistoricoCreate, EventoHistoricoInDB, EventoHistoricoUpdate
from src.responses.response import Response

class EventoHistoricoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection
        
    async def crear_evento_historico(self, evento_historico: EventoHistoricoCreate) -> Response:
        try:
            evento_historico_db = await self.connection.eventohistorico.create({
                'nombre': evento_historico.nombre,
                'descripcion': evento_historico.descripcion,
                'fecha_inicio': evento_historico.fecha_inicio,
                'fecha_fin': evento_historico.fecha_fin,
                'tipo': evento_historico.tipo,
                'id_ubicacion': evento_historico.id_ubicacion
            })
            evento_historico = EventoHistoricoInDB.model_validate(evento_historico_db.model_dump())
            return Response(
                status=201,
                success=True,
                message="Evento historico creado exitosamente",
                data=evento_historico
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear evento historico: {str(e)}"
            )
    
    async def obtener_eventos_historicos(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            eventos_historicos_db = await self.connection.eventohistorico.find_many(
                skip=skip,
                take=limit,
                include={
                    'ubicacion': True,
                }
            )
            eventos_historicos = [EventoHistoricoInDB.model_validate(e.model_dump()) for e in eventos_historicos_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(eventos_historicos)} eventos historicos",
                data=eventos_historicos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener eventos historicos: {str(e)}"
            )
            
    async def obtener_evento_historico_por_id(self, id: int) -> Response:
        try:
            evento_historico_db = await self.connection.eventohistorico.find_unique(
                where={
                    'id': id
                },
                include={
                    'ubicacion': False,
                    'bibliotecas': False,
                    'documentos': False,
                    'multimedia': False,
                    'categorias': False,
                    'agendas': False,
                    'comentarios': False
                }
            )
            if not evento_historico_db:
                return Response(
                    status=404,
                    success=False,
                    message="Evento historico no encontrado"
                )
            evento_historico = EventoHistoricoInDB.model_validate(evento_historico_db.model_dump())
            return Response(
                status=200,
                success=True,
                message="Evento historico encontrado",
                data=evento_historico
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener evento historico: {str(e)}"
            )
            
    async def editar_evento_historico(self, id: int, evento_historico: EventoHistoricoUpdate) -> Response:
        try:
            evento_historico_db = await self.connection.eventohistorico.update(
                where={
                    'id': id
                },
                data={
                    'nombre': evento_historico.nombre,
                    'descripcion': evento_historico.descripcion,
                    'fecha_inicio': evento_historico.fecha_inicio,
                    'fecha_fin': evento_historico.fecha_fin,
                    'tipo': evento_historico.tipo,
                    'id_ubicacion': evento_historico.id_ubicacion
                }
            )
            evento_historico = EventoHistoricoInDB.model_validate(evento_historico_db.model_dump())
            return Response(
                status=200,
                success=True,
                message="Evento historico editado exitosamente",
                data=evento_historico
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al editar evento historico: {str(e)}"
            )
    
    async def eliminar_evento_historico(self, id: int) -> Response:
        try:
            evento_historico_db = await self.connection.eventohistorico.delete(
                where={
                    'id': id
                }
            )
            evento_historico = EventoHistoricoInDB.model_validate(evento_historico_db.model_dump())
            return Response(
                status=200,
                success=True,
                message="Evento historico eliminado exitosamente",
                data=evento_historico
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar evento historico: {str(e)}"
            )
            