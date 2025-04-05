from fastapi    import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_comentario_service
from src.core.services.comentario_service import ComentarioService
from src.responses.response import Response

from src.core.models.comentario_domain import (
    ComentarioCreate,
    ComentarioInDB,
    ComentarioUpdate,
    ComentarioWithRelations
)

comentario_controller = APIRouter(prefix="/api/v1/comentarios", tags=["Comentarios"])

@comentario_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_comentario(
    comentario_data: ComentarioCreate,
    comentario_service: ComentarioService = Depends(build_comentario_service)
) -> Response:
    
    response = await comentario_service.crear_comentario(comentario_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@comentario_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all comentarios",
    response_description="List of comentarios"
)
async def get_all_comentarios(
    skip: int = 0,
    limit: int = 100,
    id_biblioteca: int = None,
    id_evento_agendable: int = None,
    id_evento_historico: int = None,
    comentario_service: ComentarioService = Depends(build_comentario_service)
) -> Response:
    response = await comentario_service.listar_comentarios_por_entidad(
        id_biblioteca, id_evento_agendable, id_evento_historico, skip, limit
    )
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@comentario_controller.get(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get comentario by ID",
    response_description="Comentario details"
)
async def get_comentario_by_id(
    id: int,
    comentario_service: ComentarioService = Depends(build_comentario_service)
) -> Response:
    response = await comentario_service.obtener_comentario(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@comentario_controller.put(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update comentario",
    response_description="Comentario updated successfully"
)
async def update_comentario(
    id: int,
    comentario_data: ComentarioUpdate,
    comentario_service: ComentarioService = Depends(build_comentario_service)
) -> Response:
    response = await comentario_service.actualizar_comentario(id, comentario_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@comentario_controller.delete(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete comentario",
    response_description="Comentario deleted successfully"
)
async def delete_comentario(
    id: int,
    comentario_service: ComentarioService = Depends(build_comentario_service)
) -> Response:
    response = await comentario_service.eliminar_comentario(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
