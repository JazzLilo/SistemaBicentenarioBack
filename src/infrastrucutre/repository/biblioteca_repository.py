from prisma import Prisma
from src.core.models.biblioteca_domain import (
    BibliotecaCreate,
    BibliotecaInDB,
    BibliotecaUpdate,
    BibliotecaWithRelations
)
from src.responses.response import Response
from src.core.models.tipo_documento_domain import TipoDocumentoInDB
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.core.models.comentario_domain import ComentarioInDB
from typing import List, Optional

class BibliotecaRepository:
    def __init__(self, connection: Prisma):
        self.connection = connection

    async def crear_biblioteca(self, biblioteca: BibliotecaCreate) -> Response:
        try:
            tipo_doc = await self.connection.tipodocumento.find_unique(
                where={'id_tipo': biblioteca.id_tipo}
            )
            if not tipo_doc:
                return Response(
                    status=404,
                    success=False,
                    message="Tipo de documento no encontrado"
                )

            nueva_biblioteca = await self.connection.biblioteca.create({
                'titulo': biblioteca.titulo,
                'autor': biblioteca.autor,
                'imagen': biblioteca.imagen,
                'fecha_publicacion': biblioteca.fecha_publicacion,
                'edicion': biblioteca.edicion,
                'id_tipo': biblioteca.id_tipo,
                'fuente': biblioteca.fuente,
                'enlace': str(biblioteca.enlace) if biblioteca.enlace else None
            })

            return Response(
                status=201,
                success=True,
                message="Documento bibliográfico creado exitosamente",
                data=[BibliotecaInDB.model_validate(nueva_biblioteca)]
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al crear documento bibliográfico: {str(e)}"
            )

    async def obtener_biblioteca(self, id: int) -> Response:
        try:
            biblioteca = await self.connection.biblioteca.find_unique(
                where={'id': id},
                include={
                    'tipo': True,
                    'eventos_historicos': True,
                    'comentarios': True
                }
            )

            if not biblioteca:
                return Response(
                    status=404,
                    success=False,
                    message="Documento bibliográfico no encontrado"
                )

            biblio_dict = biblioteca.model_dump()
            
            if biblioteca.tipo:
                
                biblio_dict['tipo'] = TipoDocumentoInDB.model_validate(biblioteca.tipo.model_dump())
            
            if biblioteca.eventos_historicos:
                
                biblio_dict['eventos_historicos'] = [
                    EventoHistoricoInDB.model_validate(e.model_dump())
                    for e in biblioteca.eventos_historicos
                ]
            
            if biblioteca.comentarios:
                
                biblio_dict['comentarios'] = [
                    ComentarioInDB.model_validate(c.model_dump())
                    for c in biblioteca.comentarios
                ]

            biblio_with_relations = BibliotecaWithRelations.model_validate(biblio_dict)
            
            return Response(
                status=200,
                success=True,
                message="Documento bibliográfico encontrado",
                data=biblio_with_relations
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al obtener documento bibliográfico: {str(e)}"
            )

    async def actualizar_biblioteca(
        self, 
        id: int, 
        update_data: BibliotecaUpdate
    ) -> Response:
        try:
           
            existing = await self.connection.biblioteca.find_unique(
                where={'id': id}
            )
            if not existing:
                return Response(
                    status=404,
                    success=False,
                    message="Documento bibliográfico no encontrado"
                )

            if update_data.id_tipo is not None:
                tipo_doc = await self.connection.tipodocumento.find_unique(
                    where={'id_tipo': update_data.id_tipo}
                )
                if not tipo_doc:
                    return Response(
                        status=404,
                        success=False,
                        message="Nuevo tipo de documento no encontrado"
                    )

            update_values = {k: v for k, v in update_data.model_dump().items() if v is not None}
            if 'enlace' in update_values and update_values['enlace']:
                update_values['enlace'] = str(update_values['enlace'])
            
            biblioteca_actualizada = await self.connection.biblioteca.update(
                where={'id': id},
                data=update_values,
                include={
                    'tipo': True,
                }
            )

            biblio_dict = biblioteca_actualizada.model_dump()
            
            if biblioteca_actualizada.tipo:
                
                biblio_dict['tipo'] = TipoDocumentoInDB.model_validate(biblioteca_actualizada.tipo.model_dump())
            
          

            
            return Response(
                status=200,
                success=True,
                message="Documento bibliográfico actualizado exitosamente",
                data=biblio_dict
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al actualizar documento bibliográfico: {str(e)}"
            )

    async def eliminar_biblioteca(self, id: int) -> Response:
        try:
            
            eventos = await self.connection.eventohistorico.find_many(
                where={'bibliotecas': {'some': {'id': id}}},
                take=1
            )
            if eventos:
                return Response(
                    status=400,
                    success=False,
                    message="No se puede eliminar, hay eventos históricos asociados a este documento"
                )

            biblioteca_eliminada = await self.connection.biblioteca.delete(
                where={'id': id}
            )
            
            return Response(
                status=200,
                success=True,
                message="Documento bibliográfico eliminado exitosamente",
                data=BibliotecaInDB.model_validate(biblioteca_eliminada)
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al eliminar documento bibliográfico: {str(e)}"
            )

    async def listar_bibliotecas(
        self, 
        skip: int = 0, 
        limit: int = 100,
        id_tipo: Optional[int] = None,
        titulo: Optional[str] = None
    ) -> Response:
        try:
            where_clause = {}
            if id_tipo:
                where_clause['id_tipo'] = id_tipo
            if titulo:
                where_clause['titulo'] = {
                    'contains': titulo,
                    'mode': 'insensitive'
                }

            bibliotecas = await self.connection.biblioteca.find_many(
                where=where_clause,
                skip=skip,
                take=limit,
                include={'tipo': True},
                order={'titulo': 'asc'} 
            )

            bibliotecas_con_relaciones = []
            for biblio in bibliotecas:
                biblio_dict = biblio.model_dump()
                
                if biblio.tipo:
                    
                    biblio_dict['tipo'] = TipoDocumentoInDB.model_validate(biblio.tipo.model_dump())
                
                bibliotecas_con_relaciones.append(
                    biblio_dict
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(bibliotecas_con_relaciones)} documentos bibliográficos",
                data=bibliotecas_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al listar documentos bibliográficos: {str(e)}"
            )

    async def buscar_bibliotecas_por_autor(
        self, 
        autor: str,
        skip: int = 0,
        limit: int = 100
    ) -> Response:
        try:
            bibliotecas = await self.connection.biblioteca.find_many(
                where={
                    'autor': {
                        'contains': autor,
                        'mode': 'insensitive'
                    }
                },
                skip=skip,
                take=limit,
                include={'tipo': True}
            )

            bibliotecas_con_relaciones = []
            for biblio in bibliotecas:
                biblio_dict = biblio.model_dump()
                
                if biblio.tipo:
                    
                    biblio_dict['tipo'] = TipoDocumentoInDB.model_validate(biblio.tipo.model_dump())
                
                bibliotecas_con_relaciones.append(
                    BibliotecaWithRelations(
                        **biblio_dict,
                        eventos_historicos=[],
                        comentarios=[]
                    )
                )

            return Response(
                status=200,
                success=True,
                message=f"Se encontraron {len(bibliotecas_con_relaciones)} documentos del autor",
                data=bibliotecas_con_relaciones
            )
        except Exception as e:
            return Response(
                status=500,
                success=False,
                message=f"Error al buscar documentos por autor: {str(e)}"
            )