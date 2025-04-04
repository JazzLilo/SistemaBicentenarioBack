from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_multimedia_service
from src.core.services.multimedia_service import MultimediaService
from src.responses.response import Response

from src.core.models.multimedia_domain import MultimediaCreate, MultimediaInDB, MultimediaUpdate

multimedia_controller = APIRouter(prefix="/api/v1/multimedia", tags=["Multimedia"])

@multimedia_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_multimedia(
    multimedia_data: MultimediaCreate,
    multimedia_service: MultimediaService = Depends(build_multimedia_service)
) -> Response:
    
    response = await multimedia_service.crear_multimedia(multimedia_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@multimedia_controller.get(
    "/evento_historico/{id_evento_historico}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all multimedia by evento historico",
    response_description="List of multimedia"
)
async def get_multimedia_by_evento_historico(
    id_evento_historico: int,
    multimedia_service: MultimediaService = Depends(build_multimedia_service)
) -> Response:
    response = await multimedia_service.obtener_multimedia_por_evento_historico(id_evento_historico)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@multimedia_controller.delete(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete multimedia",
    response_description="Multimedia deleted"
)
async def delete_multimedia(
    id: int,
    multimedia_service: MultimediaService = Depends(build_multimedia_service)
) -> Response:
    response = await multimedia_service.eliminar_multimedia(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
