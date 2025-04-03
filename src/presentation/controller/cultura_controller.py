from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_cultura_service
from src.core.services.cultura_service import CulturaService
from src.core.models.cultura_domain import CulturaCreate, CulturaUpdate
from src.responses.response import Response

cultura_controller = APIRouter(prefix="/api/v1/culturas", tags=["Culturas"])

@cultura_controller.post("/", response_model=Response)
async def create_cultura(
    cultura_data: CulturaCreate,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    
    response = await cultura_service.crear_cultura(cultura_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all cultures",
    response_description="List of cultures"
)
async def get_all_culturas(
    skip: int = 0,
    limit: int = 100,
    ubicacion_id: int = None,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.obtener_culturas(skip, limit, ubicacion_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.get(
    "/{cultura_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get culture by ID",
    response_description="Culture details"
)
async def get_cultura_by_id(
    cultura_id: int,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:

    response = await cultura_service.obtener_cultura(cultura_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@cultura_controller.put(
    "/{cultura_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update culture by ID",
    response_description="Updated culture details"
)
async def update_cultura(
    cultura_id: int,
    cultura_data: CulturaUpdate,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    
    response = await cultura_service.actualizar_cultura(cultura_id, cultura_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.delete(
    "/{cultura_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete culture by ID",
    response_description="Deleted culture details"
)
async def delete_cultura(
    cultura_id: int,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    
    response = await cultura_service.eliminar_cultura(cultura_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
