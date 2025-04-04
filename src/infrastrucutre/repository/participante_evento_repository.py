from prisma import Prisma
from src.core.models.participante_evento_domain import (
    ParticipanteEventoCreate,
    ParticipanteEventoInDB,
    ParticipanteEventoUpdate,
    ParticipanteEventoWithRelations
)
from src.responses.response import Response

class ParticipanteEventoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection
        
    async def agregar_participante(self, participante: ParticipanteEventoCreate) -> Response:
        try:
            # Verificar si ya existe
            existente = await self.connection.participanteevento.find_first(
                where={
                    'id_usuario': participante.id_usuario,
                    'id_evento': participante.id_evento
                }
            )
            
            if existente:
                return Response(
                    status=400,
                    success=False,
                    message="El usuario ya es participante de este evento"
                )
                
            nuevo_participante = await self.connection.participanteevento.create(
                data=participante.model_dump()
            )
            
            return Response(
                status=201,
                success=True,
                message="Participante agregado exitosamente",
                data=ParticipanteEventoInDB.model_validate(nuevo_participante)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al agregar participante: {str(e)}"
            )
    
    async def obtener_participante(self, id_usuario: int, id_evento: int) -> Response:
        try:
            participante = await self.connection.participanteevento.find_first(
                where={
                    'id_usuario': id_usuario,
                    'id_evento': id_evento
                },
                include={
                    'usuario': True,
                    'evento': True
                }
            )
            
            if not participante:
                return Response(
                    status=404,
                    success=False,
                    message="Participante no encontrado"
                )
                
            return Response(
                status=200,
                success=True,
                message="Participante encontrado",
                data=ParticipanteEventoWithRelations.model_validate(participante)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener participante: {str(e)}"
            )
    
    async def actualizar_asistencia(
        self, 
        id_usuario: int, 
        id_evento: int, 
        update_data: ParticipanteEventoUpdate
    ) -> Response:
        try:
            participante = await self.connection.participanteevento.update(
                where={
                    'id_usuario_id_evento': {
                        'id_usuario': id_usuario,
                        'id_evento': id_evento
                    }
                },
                data={
                    'estado_asistencia': update_data.estado_asistencia
                },
                include={
                    'usuario': True,
                    'evento': True
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Asistencia actualizada exitosamente",
                data=ParticipanteEventoWithRelations.model_validate(participante)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar asistencia: {str(e)}"
            )
    
    async def eliminar_participante(self, id_usuario: int, id_evento: int) -> Response:
        try:
            participante = await self.connection.participanteevento.delete(
                where={
                    'id_usuario_id_evento': {
                        'id_usuario': id_usuario,
                        'id_evento': id_evento
                    }
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Participante eliminado exitosamente",
                data=ParticipanteEventoInDB.model_validate(participante)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar participante: {str(e)}"
            )
    
    async def listar_participantes_por_evento(self, id_evento: int) -> Response:
        try:
            participantes = await self.connection.participanteevento.find_many(
                where={
                    'id_evento': id_evento
                },
                include={
                    'usuario': True
                }
            )
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(participantes)} participantes",
                data=[ParticipanteEventoWithRelations.model_validate(p) for p in participantes]
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar participantes: {str(e)}"
            )
    
    async def listar_eventos_por_participante(self, id_usuario: int) -> Response:
        try:
            participantes = await self.connection.participanteevento.find_many(
                where={
                    'id_usuario': id_usuario
                },
                include={
                    'evento': {
                        'include': {
                            'ubicacion': True,
                            'organizador': True
                        }
                    }
                }
            )
            
            # Extraer solo los eventos con sus relaciones
            eventos = [p.evento for p in participantes if p.evento]
            
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(eventos)} eventos para el participante",
                data=eventos
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar eventos del participante: {str(e)}"
            )