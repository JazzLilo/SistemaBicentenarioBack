from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_cultura_service
from src.core.models.cultura_domain import CulturaCreate, CulturaUpdate, CulturaInDB
from src.core.services.cultura_service import CulturaService
from src.responses.response import Response
from typing import Optional


cultura_controller = APIRouter(prefix="/api/v1/culturas", tags=["Culturas"])

@cultura_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new culture",
    response_description="Culture created successfully"
)
async def create_culture(
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
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get culture by ID",
    response_description="Culture retrieved successfully"
)
async def get_culture_by_id(
    id: int,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.obtener_cultura_por_id(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.put(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update culture",
    response_description="Culture updated successfully"
)
async def update_culture(
    id: int,
    cultura_data: CulturaUpdate,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.actualizar_cultura(id, cultura_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.delete(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete culture",
    response_description="Culture deleted successfully"
)
async def delete_culture(
    id: int,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.eliminar_cultura(id)
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
    summary="List cultures",
    response_description="List of cultures retrieved successfully"
)
async def list_cultures(
    skip: int = 0,
    limit: int = 100,
    nombre: Optional[str] = None,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.listar_culturas(skip, limit, nombre)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@cultura_controller.get(
    "/ubicacion/{id_ubicacion}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get cultures by location ID",
    response_description="List of cultures by location retrieved successfully"
)
async def get_cultures_by_location(
    id_ubicacion: int,
    skip: int = 0,
    limit: int = 100,
    cultura_service: CulturaService = Depends(build_cultura_service)
) -> Response:
    response = await cultura_service.buscar_culturas_por_ubicacion(id_ubicacion, skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

