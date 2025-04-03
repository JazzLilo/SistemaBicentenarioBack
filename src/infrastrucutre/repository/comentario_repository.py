from typing import Optional
from prisma import Prisma
from src.core.models.comentario_domain import (
    ComentarioCreate,
    ComentarioInDB,
    ComentarioUpdate
)
from src.responses.response import Response

class ComentarioRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_comentario(self, comentario: ComentarioCreate) -> Response:
        try:
            comentario_data = {
                'contenido': comentario.contenido,
                'id_usuario': comentario.id_usuario,
                'id_biblioteca': comentario.id_biblioteca,
                'id_evento': comentario.id_evento
            }
            
            # Validar que tenga al menos una relación
            if not comentario.id_biblioteca and not comentario.id_evento:
                return Response(
                    status=400,
                    success=False,
                    message="El comentario debe estar asociado a una biblioteca o evento"
                )
            
            comentario_db = await self.connection.comentario.create(
                data=comentario_data,
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento': True
                }
            )
            return Response(
                status=201,
                success=True,
                message="Comentario creado exitosamente",
                data=ComentarioInDB.model_validate(comentario_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al crear comentario: {str(e)}"
            )

    async def obtener_comentarios(
        self,
        skip: int = 0,
        limit: int = 100,
        usuario_id: Optional[int] = None,
        biblioteca_id: Optional[int] = None,
        evento_id: Optional[int] = None
    ) -> Response:
        try:
            where_conditions = {}
            if usuario_id:
                where_conditions['id_usuario'] = usuario_id
            if biblioteca_id:
                where_conditions['id_biblioteca'] = biblioteca_id
            if evento_id:
                where_conditions['id_evento'] = evento_id

            comentarios_db = await self.connection.comentario.find_many(
                skip=skip,
                take=limit,
                where=where_conditions,
                order={'fecha': 'desc'},
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento': True
                }
            )
            comentarios = [ComentarioInDB.model_validate(c) for c in comentarios_db]
            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(comentarios)} comentarios",
                data=comentarios
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener comentarios: {str(e)}"
            )

    async def obtener_comentario_por_id(self, comentario_id: int) -> Response:
        try:
            comentario_db = await self.connection.comentario.find_unique(
                where={'id': comentario_id},
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento': True
                }
            )
            if not comentario_db:
                return Response(
                    status=404,
                    success=False,
                    message="Comentario no encontrado"
                )
            return Response(
                status=200,
                success=True,
                message="Comentario encontrado",
                data=ComentarioInDB.model_validate(comentario_db)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener comentario: {str(e)}"
            )

    async def actualizar_comentario(
        self,
        comentario_id: int,
        comentario: ComentarioUpdate
    ) -> Response:
        try:
            data = comentario.model_dump(exclude_unset=True)
            if not data:
                return Response(
                    status=400,
                    success=False,
                    message="No se proporcionaron datos para actualizar"
                )
            
            comentario_db = await self.connection.comentario.update(
                where={'id': comentario_id},
                data=data,
                include={
                    'usuario': True,
                    'biblioteca': True,
                    'evento': True
                }
            )
            return Response(
                status=200,
                success=True,
                message="Comentario actualizado exitosamente",
                data=ComentarioInDB.model_validate(comentario_db)
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al actualizar comentario: {str(e)}"
            )

    async def eliminar_comentario(self, comentario_id: int) -> Response:
        try:
            # Primero verificar si existe
            comentario = await self.connection.comentario.find_unique(
                where={'id': comentario_id}
            )
            if not comentario:
                return Response(
                    status=404,
                    success=False,
                    message="Comentario no encontrado"
                )
                
            await self.connection.comentario.delete(
                where={'id': comentario_id}
            )
            return Response(
                status=200,
                success=True,
                message="Comentario eliminado exitosamente"
            )
        except Exception as e:
            return Response(
                status=400,
                success=False,
                message=f"Error al eliminar comentario: {str(e)}"
            )