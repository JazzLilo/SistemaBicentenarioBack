from prisma import Prisma
from src.core.models.agenda_usuario_domain import (
    AgendaUsuarioCreate,
    AgendaUsuarioInDB,
    AgendaUsuarioUpdate,
    AgendaUsuarioWithRelations
)
from src.responses.response import Response
from typing import Optional

class AgendaUsuarioRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_agenda_usuario(self, agenda: AgendaUsuarioCreate) -> Response:
        try:
            if agenda.id_evento_historico == 0:
                agenda.id_evento_historico = None
            if agenda.id_evento_agendable == 0:
                agenda.id_evento_agendable = None

            if not agenda.id_evento_historico and not agenda.id_evento_agendable:
                return Response(
                    status=400,
                    success=False,
                    message="Debe proporcionar al menos un evento (histórico o agendable)"
                )

            if agenda.id_evento_historico:
                evento_historico = await self.connection.eventohistorico.find_unique(
                    where={'id': agenda.id_evento_historico}
                )
                if not evento_historico:
                    return Response(
                        status=404,
                        success=False,
                        message="Evento histórico no encontrado"
                    )

            if agenda.id_evento_agendable:
                evento_agendable = await self.connection.eventoagendable.find_unique(
                    where={'id': agenda.id_evento_agendable}
                )
                if not evento_agendable:
                    return Response(
                        status=404,
                        success=False,
                        message="Evento agendable no encontrado"
                    )

            existing = await self.connection.agendausuario.find_first(
                where={
                    'id_usuario': agenda.id_usuario,
                    'OR': [
                        {'id_evento_historico': agenda.id_evento_historico},
                        {'id_evento_agendable': agenda.id_evento_agendable}
                    ]
                }
            )

            if existing:
                return Response(
                    status=400,
                    success=False,
                    message="Esta combinación de usuario y evento ya existe en la agenda"
                )

            nueva_agenda = await self.connection.agendausuario.create(
                data={
                    'id_usuario': agenda.id_usuario,
                    'id_evento_historico': agenda.id_evento_historico,
                    'id_evento_agendable': agenda.id_evento_agendable,
                    'fecha_recordatorio': agenda.fecha_recordatorio
                }
            )
            
            return Response(
                status=201,
                success=True,
                message="Evento agregado a la agenda exitosamente",
                data=AgendaUsuarioInDB.model_validate(nueva_agenda)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al agregar evento a la agenda: {str(e)}"
            )
            
    async def obtener_agenda_por_id(self, id: int) -> Response:
        try:
            agenda = await self.connection.agendausuario.find_unique(
                where={'id': id},
                include={
                    'usuario': True,
                    'evento_historico': True,
                    'evento_agendable': True
                }
            )

            if not agenda:
                return Response(
                    status=404,
                    success=False,
                    message="Entrada de agenda no encontrada"
                )

            agenda_dict = agenda.model_dump()
            
            if agenda.usuario:
                from src.core.models.usuario_domain import UsuarioInDB
                agenda_dict['usuario'] = UsuarioInDB.model_validate(agenda.usuario.model_dump())
            
            if agenda.evento_historico:
                from src.core.models.evento_historico_domain import EventoHistoricoInDB
                agenda_dict['evento_historico'] = EventoHistoricoInDB.model_validate(agenda.evento_historico.model_dump())
            
            if agenda.evento_agendable:
                from src.core.models.evento_agendable_domain import EventoAgendableInDB
                agenda_dict['evento_agendable'] = EventoAgendableInDB.model_validate(agenda.evento_agendable.model_dump())

            agenda_with_relations = AgendaUsuarioWithRelations.model_validate(agenda_dict)
            
            return Response(
                status=200,
                success=True,
                message="Entrada de agenda encontrada",
                data=agenda_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener entrada de agenda: {str(e)}"
            )

    async def actualizar_agenda_usuario(
        self, 
        id: int, 
        update_data: AgendaUsuarioUpdate
    ) -> Response:
        try:
            agenda = await self.connection.agendausuario.update(
                where={'id': id},
                data=update_data.model_dump(exclude_none=True),
                include={
                    'usuario': True,
                    'evento_historico': True,
                    'evento_agendable': True
                }
            )

            agenda_dict = agenda.model_dump()
            
            if agenda.usuario:
                from src.core.models.usuario_domain import UsuarioInDB
                agenda_dict['usuario'] = UsuarioInDB.model_validate(agenda.usuario.model_dump())
            
            if agenda.evento_historico:
                from src.core.models.evento_historico_domain import EventoHistoricoInDB
                agenda_dict['evento_historico'] = EventoHistoricoInDB.model_validate(agenda.evento_historico.model_dump())
            
            if agenda.evento_agendable:
                from src.core.models.evento_agendable_domain import EventoAgendableInDB
                agenda_dict['evento_agendable'] = EventoAgendableInDB.model_validate(agenda.evento_agendable.model_dump())

            agenda_with_relations = AgendaUsuarioWithRelations.model_validate(agenda_dict)
            
            return Response(
                status=200,
                success=True,
                message="Entrada de agenda actualizada exitosamente",
                data=agenda_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar entrada de agenda: {str(e)}"
            )

    async def eliminar_agenda_usuario(self, id: int) -> Response:
        try:
            agenda = await self.connection.agendausuario.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Entrada de agenda eliminada exitosamente",
                data=AgendaUsuarioInDB.model_validate(agenda)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar entrada de agenda: {str(e)}"
            )

    async def listar_agendas_por_usuario(
        self, 
        id_usuario: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            agendas = await self.connection.agendausuario.find_many(
                where={'id_usuario': id_usuario},
                skip=skip,
                take=limit,
                include={
                    'evento_historico': True,
                    'evento_agendable': True
                },
                order={'fecha_recordatorio': 'asc'}  # Ordenar por fecha de recordatorio
            )

            # Convertir cada entrada de agenda
            agendas_con_relaciones = []
            for agenda in agendas:
                agenda_dict = agenda.model_dump()
                
                if agenda.evento_historico:
                    from src.core.models.evento_historico_domain import EventoHistoricoInDB
                    agenda_dict['evento_historico'] = EventoHistoricoInDB.model_validate(agenda.evento_historico.model_dump())
                
                if agenda.evento_agendable:
                    from src.core.models.evento_agendable_domain import EventoAgendableInDB
                    agenda_dict['evento_agendable'] = EventoAgendableInDB.model_validate(agenda.evento_agendable.model_dump())
                
                agendas_con_relaciones.append(
                    AgendaUsuarioWithRelations.model_validate(agenda_dict)
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(agendas_con_relaciones)} entradas en la agenda",
                data=agendas_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar entradas de agenda: {str(e)}"
            )

    async def obtener_agenda_por_evento_usuario(
        self,
        id_usuario: int,
        id_evento_historico: Optional[int] = None,
        id_evento_agendable: Optional[int] = None
    ) -> Response:
        try:
            if not id_evento_historico and not id_evento_agendable:
                return Response(
                    status=400,
                    success=False,
                    message="Debe proporcionar al menos un ID de evento"
                )

            where_clause = {'id_usuario': id_usuario}
            if id_evento_historico:
                where_clause['id_evento_historico'] = id_evento_historico
            if id_evento_agendable:
                where_clause['id_evento_agendable'] = id_evento_agendable

            agenda = await self.connection.agendausuario.find_first(
                where=where_clause,
                include={
                    'usuario': True,
                    'evento_historico': True,
                    'evento_agendable': True
                }
            )

            if not agenda:
                return Response(
                    status=404,
                    success=False,
                    message="Entrada de agenda no encontrada"
                )

            # Convertir manualmente las relaciones
            agenda_dict = agenda.model_dump()
            
            if agenda.usuario:
                from src.core.models.usuario_domain import UsuarioInDB
                agenda_dict['usuario'] = UsuarioInDB.model_validate(agenda.usuario.model_dump())
            
            if agenda.evento_historico:
                from src.core.models.evento_historico_domain import EventoHistoricoInDB
                agenda_dict['evento_historico'] = EventoHistoricoInDB.model_validate(agenda.evento_historico.model_dump())
            
            if agenda.evento_agendable:
                from src.core.models.evento_agendable_domain import EventoAgendableInDB
                agenda_dict['evento_agendable'] = EventoAgendableInDB.model_validate(agenda.evento_agendable.model_dump())

            agenda_with_relations = AgendaUsuarioWithRelations.model_validate(agenda_dict)
            
            return Response(
                status=200,
                success=True,
                message="Entrada de agenda encontrada",
                data=agenda_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al buscar entrada de agenda: {str(e)}"
            )