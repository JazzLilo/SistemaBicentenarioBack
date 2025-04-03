from typing import List, Optional
from prisma import Prisma
from src.core.models.evento_domain import EventoCreate, EventoInDB, EventoUpdate
from src.responses.response import Response

class EventoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_evento(self, evento: EventoCreate) -> Response:
        try:
            evento_db = await self.connection.evento.create({
                'nombre': evento.nombre,
                'descripcion': evento.descripcion,
                'fecha_hora': evento.fecha_hora,
                'id_organizador': evento.id_organizador,
                'imagen': evento.imagen,
                'id_ubicacion': evento.id_ubicacion
            }, include={
                'organizador': True,
                'ubicacion': True
            })
            
            return Response(
                status=201,
                success=True,
                message="Evento creado exitosamente",
                data=EventoInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear evento: {str(e)}"
            )

    async def obtener_evento_por_id(self, id_evento: int) -> Response:
        try:
            evento_db = await self.connection.evento.find_unique(
                where={'id': id_evento},
                include={
                    'organizador': True,
                    'ubicacion': True,
                    'participantes': {
                        'include': {
                            'usuario': True
                        }
                    },
                    'comentarios': {
                        'include': {
                            'usuario': True
                        }
                    }
                }
            )
            
            if not evento_db:
                return Response(
                    status=404,
                    success=False,
                    message="Evento no encontrado"
                )
            
            return Response(
                status=200,
                success=True,
                message="Evento obtenido exitosamente",
                data=EventoInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al obtener evento: {str(e)}"
            )

    async def actualizar_evento(self, id_evento: int, evento: EventoUpdate) -> Response:
        try:
            data = {k: v for k, v in evento.model_dump().items() if v is not None}
            
            evento_db = await self.connection.evento.update(
                where={'id': id_evento},
                data=data,
                include={
                    'organizador': True,
                    'ubicacion': True
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Evento actualizado exitosamente",
                data=EventoInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar evento: {str(e)}"
            )

    async def eliminar_evento(self, id_evento: int) -> Response:
        try:
            await self.connection.evento.delete(where={'id': id_evento})
            
            return Response(
                status=200,
                success=True,
                message="Evento eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar evento: {str(e)}"
            )

    async def listar_eventos(self) -> Response:
        try:
            eventos_db = await self.connection.evento.find_many(
                include={
                    'organizador': True,
                    'ubicacion': True
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Eventos obtenidos exitosamente",
                data=[EventoInDB.model_validate(e) for e in eventos_db]
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al listar eventos: {str(e)}"
            )