from prisma import Prisma
from src.core.models.comentario_domain import (
    ComentarioCreate,
    ComentarioInDB,
    ComentarioUpdate,
    ComentarioWithRelations
)
from src.core.models.biblioteca_domain import BibliotecaInDB
from src.core.models.usuario_domain import UsuarioInDB
from src.core.models.evento_agendable_domain import EventoAgendableInDB
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.responses.response import Response
from typing import Optional

class ComentarioRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_comentario(self, comentario: ComentarioCreate) -> Response:
        try:
            parent_entities = sum([
                1 if comentario.id_biblioteca is not None else 0,
                1 if comentario.id_evento_agendable is not None else 0,
                1 if comentario.id_evento_historico is not None else 0
            ])
            
            if parent_entities != 1:
                return Response(
                    status=400,
                    success=False,
                    message="El comentario debe estar asociado a exactamente una entidad (biblioteca, evento agendable o evento histórico)"
                )

            usuario = await self.connection.usuario.find_unique(
                where={'id': comentario.id_usuario}
            )
            if not usuario:
                return Response(
                    status=404,
                    success=False,
                    message="Usuario no encontrado"
                )

            # Verify parent entity exists
            if comentario.id_biblioteca:
                parent = await self.connection.biblioteca.find_unique(
                    where={'id': comentario.id_biblioteca}
                )
                entity_type = "biblioteca"
            elif comentario.id_evento_agendable:
                parent = await self.connection.eventoagendable.find_unique(
                    where={'id': comentario.id_evento_agendable}
                )
                entity_type = "evento agendable"
            else:
                parent = await self.connection.eventohistorico.find_unique(
                    where={'id': comentario.id_evento_historico}
                )
                entity_type = "evento histórico"

            if not parent:
                return Response(
                    status=404,
                    success=False,
                    message=f"{entity_type.capitalize()} no encontrado"
                )

            nuevo_comentario = await self.connection.comentario.create({
                'contenido': comentario.contenido,
                'id_usuario': comentario.id_usuario,
                'id_biblioteca': comentario.id_biblioteca,
                'id_evento_agendable': comentario.id_evento_agendable,
                'id_evento_historico': comentario.id_evento_historico
            })

            return Response(
                status=201,
                success=True,
                message="Comentario creado exitosamente",
                data=ComentarioInDB.model_validate(nuevo_comentario)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear comentario: {str(e)}"
            )

    async def obtener_comentario(self, id: int) -> Response:
        try:
            comentario = await self.connection.comentario.find_unique(
                where={'id': id},
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento_agendable': True,
                    'evento_historico': True
                }
            )

            if not comentario:
                return Response(
                    status=404,
                    success=False,
                    message="Comentario no encontrado"
                )

            comentario_dict = comentario.model_dump()
            
            if comentario.usuario:
                
                comentario_dict['usuario'] = UsuarioInDB.model_validate(comentario.usuario.model_dump())
            
            if comentario.biblioteca:
                
                comentario_dict['biblioteca'] = BibliotecaInDB.model_validate(comentario.biblioteca.model_dump())
            
            if comentario.evento_agendable:
                
                comentario_dict['evento_agendable'] = EventoAgendableInDB.model_validate(comentario.evento_agendable.model_dump())
            
            if comentario.evento_historico:
                
                comentario_dict['evento_historico'] = EventoHistoricoInDB.model_validate(comentario.evento_historico.model_dump())

            comentario_with_relations = ComentarioWithRelations.model_validate(comentario_dict)
            
            return Response(
                status=200,
                success=True,
                message="Comentario encontrado",
                data=comentario_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener comentario: {str(e)}"
            )

    async def actualizar_comentario(
        self, 
        id: int, 
        update_data: ComentarioUpdate
    ) -> Response:
        try:
            existing = await self.connection.comentario.find_unique(
                where={'id': id}
            )
            if not existing:
                return Response(
                    status=404,
                    success=False,
                    message="Comentario no encontrado"
                )

            if any([
                update_data.id_usuario is not None,
                update_data.id_biblioteca is not None,
                update_data.id_evento_agendable is not None,
                update_data.id_evento_historico is not None
            ]):
                return Response(
                    status=400,
                    success=False,
                    message="No se pueden modificar las relaciones del comentario"
                )

            comentario_actualizado = await self.connection.comentario.update(
                where={'id': id},
                data={'contenido': update_data.contenido},
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento_agendable': True,
                    'evento_historico': True
                }
            )

            comentario_dict = comentario_actualizado.model_dump()
            
            if comentario_actualizado.usuario:
                
                comentario_dict['usuario'] = UsuarioInDB.model_validate(comentario_actualizado.usuario.model_dump())
            
            if comentario_actualizado.biblioteca:
                
                comentario_dict['biblioteca'] = BibliotecaInDB.model_validate(comentario_actualizado.biblioteca.model_dump())
            
            if comentario_actualizado.evento_agendable:
                
                comentario_dict['evento_agendable'] = EventoAgendableInDB.model_validate(comentario_actualizado.evento_agendable.model_dump())
            
            if comentario_actualizado.evento_historico:
                
                comentario_dict['evento_historico'] = EventoHistoricoInDB.model_validate(comentario_actualizado.evento_historico.model_dump())

            comentario_with_relations = ComentarioWithRelations.model_validate(comentario_dict)
            
            return Response(
                status=200,
                success=True,
                message="Comentario actualizado exitosamente",
                data=comentario_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar comentario: {str(e)}"
            )

    async def eliminar_comentario(self, id: int) -> Response:
        try:
            comentario = await self.connection.comentario.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Comentario eliminado exitosamente",
                data=ComentarioInDB.model_validate(comentario)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar comentario: {str(e)}"
            )

    async def listar_comentarios_por_entidad(
        self,
        id_biblioteca: Optional[int] = None,
        id_evento_agendable: Optional[int] = None,
        id_evento_historico: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            parent_entities = sum([
                1 if id_biblioteca is not None else 0,
                1 if id_evento_agendable is not None else 0,
                1 if id_evento_historico is not None else 0
            ])
            
            if parent_entities != 1:
                return Response(
                    status=400,
                    success=False,
                    message="Debe especificar exactamente una entidad padre (biblioteca, evento agendable o evento histórico)"
                )

            where_clause = {}
            if id_biblioteca:
                where_clause['id_biblioteca'] = id_biblioteca
            elif id_evento_agendable:
                where_clause['id_evento_agendable'] = id_evento_agendable
            else:
                where_clause['id_evento_historico'] = id_evento_historico

            comentarios = await self.connection.comentario.find_many(
                where=where_clause,
                skip=skip,
                take=limit,
                include={'usuario': True},
                order={'fecha': 'desc'} 
            )

            comentarios_con_relaciones = []
            for comentario in comentarios:
                comentario_dict = comentario.model_dump()
                
                if comentario.usuario:
                    from src.core.models.usuario_domain import UsuarioInDB
                    comentario_dict['usuario'] = UsuarioInDB.model_validate(comentario.usuario.model_dump())
                
                comentarios_con_relaciones.append(
                    ComentarioWithRelations(
                        **comentario_dict,
                        biblioteca=None,
                        evento_agendable=None,
                        evento_historico=None
                    )
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(comentarios_con_relaciones)} comentarios",
                data=comentarios_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar comentarios: {str(e)}"
            )

    async def listar_comentarios_por_usuario(
        self,
        id_usuario: int,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            comentarios = await self.connection.comentario.find_many(
                where={'id_usuario': id_usuario},
                skip=skip,
                take=limit,
                include={
                    'biblioteca': True,
                    'evento_agendable': True,
                    'evento_historico': True
                },
                order={'fecha': 'desc'}
            )

            comentarios_con_relaciones = []
            for comentario in comentarios:
                comentario_dict = comentario.model_dump()
                
                if comentario.biblioteca:
                    
                    comentario_dict['biblioteca'] = BibliotecaInDB.model_validate(comentario.biblioteca.model_dump())
                
                if comentario.evento_agendable:
                    comentario_dict['evento_agendable'] = EventoAgendableInDB.model_validate(comentario.evento_agendable.model_dump())
                
                if comentario.evento_historico:
                    comentario_dict['evento_historico'] = EventoHistoricoInDB.model_validate(comentario.evento_historico.model_dump())
                
                comentarios_con_relaciones.append(
                    ComentarioWithRelations(
                        **comentario_dict,
                        usuario=None 
                    )
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(comentarios_con_relaciones)} comentarios del usuario",
                data=comentarios_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar comentarios del usuario: {str(e)}"
            )