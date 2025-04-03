from typing import List, Optional
from prisma import Prisma
from src.core.models.participante_evento_domain import (
    ParticipanteEventoCreate,
    ParticipanteEventoInDB,
    ParticipanteEventoUpdate
)
from src.responses.response import Response

class ParticipanteEventoRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def agregar_participante(self, participante: ParticipanteEventoCreate) -> Response:
        try:
            participante_db = await self.connection.participanteevento.create({
                'id_usuario': participante.id_usuario,
                'id_evento': participante.id_evento,
                'estado_asistencia': participante.estado_asistencia
            }, include={
                'usuario': True,
                'evento': True
            })
            
            return Response(
                status=201,
                success=True,
                message="Participante agregado exitosamente",
                data=ParticipanteEventoInDB.model_validate(participante_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al agregar participante: {str(e)}"
            )

    async def actualizar_asistencia(self, id_usuario: int, id_evento: int, 
                                  participante: ParticipanteEventoUpdate) -> Response:
        try:
            data = {k: v for k, v in participante.model_dump().items() if v is not None}
            
            participante_db = await self.connection.participanteevento.update(
                where={
                    'id_usuario_id_evento': {
                        'id_usuario': id_usuario,
                        'id_evento': id_evento
                    }
                },
                data=data,
                include={
                    'usuario': True,
                    'evento': True
                }
            )
            
            return Response(
                status=200,
                success=True,
                message="Asistencia actualizada exitosamente",
                data=ParticipanteEventoInDB.model_validate(participante_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar asistencia: {str(e)}"
            )

    async def eliminar_participante(self, id_usuario: int, id_evento: int) -> Response:
        try:
            await self.connection.participanteevento.delete(
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
                message="Participante eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar participante: {str(e)}"
            )

    async def obtener_participantes_evento(self, id_evento: int) -> Response:
        try:
            participantes_db = await self.connection.participanteevento.find_many(
                where={'id_evento': id_evento},
                include={'usuario': True}
            )
            
            return Response(
                status=200,
                success=True,
                message="Participantes obtenidos exitosamente",
                data=[ParticipanteEventoInDB.model_validate(p) for p in participantes_db]
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al obtener participantes: {str(e)}"
            )

    async def verificar_participante(self, id_usuario: int, id_evento: int) -> Response:
        try:
            participante_db = await self.connection.participanteevento.find_unique(
                where={
                    'id_usuario_id_evento': {
                        'id_usuario': id_usuario,
                        'id_evento': id_evento
                    }
                },
                include={'usuario': True}
            )
            
            if not participante_db:
                return Response(
                    status=404,
                    success=False,
                    message="Participante no encontrado"
                )
            
            return Response(
                status=200,
                success=True,
                message="Participante encontrado",
                data=ParticipanteEventoInDB.model_validate(participante_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al verificar participante: {str(e)}"
            )