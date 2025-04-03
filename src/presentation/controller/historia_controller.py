from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_historia_service

from src.core.services.historia_service import HistoriaService
from src.core.models.historia_domain import HistoriaCreate, HistoriaUpdate
from src.responses.response import Response

historia_controller = APIRouter(prefix="/api/v1/historias", tags=["Historias"])

@historia_controller.post("/", response_model=Response)
async def create_historia(
    historia_data: HistoriaCreate,
    historia_service: HistoriaService = Depends(build_historia_service)
) -> Response:
    
    response = await historia_service.crear_historia(historia_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@historia_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all active stories",
    response_description="List of active stories"
)
async def get_all_historias(
    skip: int = 0,
    limit: int = 100,
    categoria_id: int = None,
    ubicacion_id: int = None,
    historia_service: HistoriaService = Depends(build_historia_service)
) -> Response:
    response = await historia_service.obtener_historias(skip, limit, categoria_id, ubicacion_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.get(
    "/{historia_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get story by ID",
    response_description="Story details"
)
async def get_historia_by_id(
    historia_id: int,
    historia_service: HistoriaService = Depends(build_historia_service)
) -> Response:

    response = await historia_service.obtener_historia_por_id(historia_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.put(
    "/{historia_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update story by ID",
    response_description="Updated story details"
)
async def update_historia(
    historia_id: int,
    historia_data: HistoriaUpdate,
    historia_service: HistoriaService = Depends(build_historia_service)
) -> Response:
    
    response = await historia_service.actualizar_historia(historia_id, historia_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.delete(
    "/{historia_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete story by ID",
    response_description="Deletion confirmation"
)
async def delete_historia(
    historia_id: int,
    historia_service: HistoriaService = Depends(build_historia_service)
) -> Response:
    
    response = await historia_service.eliminar_historia(historia_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
