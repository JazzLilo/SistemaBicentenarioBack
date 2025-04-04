from prisma import Prisma
from src.core.models.evento_agendable_domain import (
    
    EventoAgendableCreate,
    EventoAgendableInDB,
    EventoAgendableUpdate,
    EventoAgendableWithRelations
)
from src.responses.response import Response

class EventoAgendableRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection
        
    async def crear_evento_agendable(self, evento: EventoAgendableCreate) -> Response:
        try:
            evento_db = await self.connection.eventoagendable.create({
                'nombre': evento.nombre,
                'descripcion': evento.descripcion,
                'fecha_hora': evento.fecha_hora,
                'id_ubicacion': evento.id_ubicacion,
                'id_organizador': evento.id_organizador,
                'imagen': evento.imagen
            })
            
            return Response(
                status=201,
                success=True,
                message="Evento agendable creado exitosamente",
                data=EventoAgendableInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear evento agendable: {str(e)}"
            )
    
    async def obtener_eventos_agendables(self, skip: int = 0, limit: int = 100) -> Response:
        try:
            eventos_db = await self.connection.eventoagendable.find_many(
                skip=skip,
                take=limit,
                include={
                    'ubicacion': True,
                    'organizador': True
                }
            )
            
            eventos = [EventoAgendableInDB.model_validate(e.model_dump()) for e in eventos_db]
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(eventos)} eventos agendables",
                data=eventos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener eventos agendables: {str(e)}"
            )
            
    async def obtener_evento_agendable_por_id(self, id: int) -> Response:
        try:
            evento_db = await self.connection.eventoagendable.find_unique(
                where={'id': id},
                include={
                    'ubicacion': True,
                    'organizador': True,
                }
            )
            
            if not evento_db:
                return Response(
                    status=404,
                    success=False,
                    message="Evento agendable no encontrado"
                )
                
            evento =[ EventoAgendableInDB.model_validate(evento_db)]
            
            return Response(
                status=200,
                success=True,
                message="Evento agendable encontrado",
                data=evento
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener evento agendable: {str(e)}"
            )
    
    async def actualizar_evento_agendable(self, id: int, evento: EventoAgendableUpdate) -> Response:
        try:
            update_data = {k: v for k, v in evento.model_dump().items() if v is not None}
            
            evento_db = await self.connection.eventoagendable.update(
                where={'id': id},
                data=update_data
            )
            
            return Response(
                status=200,
                success=True,
                message="Evento agendable actualizado exitosamente",
                data=EventoAgendableInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar evento agendable: {str(e)}"
            )
    
    async def eliminar_evento_agendable(self, id: int) -> Response:
        try:
            evento_db = await self.connection.eventoagendable.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Evento agendable eliminado exitosamente",
                data=EventoAgendableInDB.model_validate(evento_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar evento agendable: {str(e)}"
            )
    
    async def obtener_eventos_por_organizador(self, id_organizador: int) -> Response:
        try:
            eventos_db = await self.connection.eventoagendable.find_many(
                where={'id_organizador': id_organizador},
                include={
                    'ubicacion': True,
                    'organizador': True
                }
            )
            
            eventos = [EventoAgendableInDB.model_validate(e.model_dump()) for e in eventos_db]
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(eventos)} eventos para el organizador",
                data=eventos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener eventos del organizador: {str(e)}"
            )
    
    async def buscar_eventos_por_nombre(self, nombre: str) -> Response:
        try:
            eventos_db = await self.connection.eventoagendable.find_many(
                where={
                    'nombre': {
                        'contains': nombre,
                        'mode': 'insensitive'
                    }
                },
                include={
                    'ubicacion': True,
                    'organizador': True
                }
            )
            
            eventos = [EventoAgendableInDB.model_validate(e.model_dump()) for e in eventos_db]
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(eventos)} eventos con el nombre buscado",
                data=eventos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al buscar eventos: {str(e)}"
            )