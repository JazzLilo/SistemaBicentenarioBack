from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_presidente_service
from src.core.services.presidente_service import PresidenteService
from src.responses.response import Response

from src.core.models.presidente_domain import PresidenteCreate, PresidenteInDB, PresidenteUpdate

presidente_controller = APIRouter(prefix="/api/v1/presidentes", tags=["Presidentes"])

@presidente_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_presidente(
    presidente_data: PresidenteCreate,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    
    response = await presidente_service.crear_presidente(presidente_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@presidente_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all presidentes",
    response_description="List of presidentes"
)
async def get_all_presidentes(
    skip: int = 0,
    limit: int = 100,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    response = await presidente_service.obtener_presidentes(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@presidente_controller.get(
    "/{presidente_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get presidente by ID",
    response_description="Presidente details"
)
async def get_presidente_by_id(
    presidente_id: int,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    response = await presidente_service.obtener_presidente_por_id(presidente_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@presidente_controller.put(
    "/{presidente_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update presidente",
    response_description="Updated presidente details"
)
async def update_presidente(
    presidente_id: int,
    presidente_data: PresidenteUpdate,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    response = await presidente_service.actualizar_presidente(presidente_id, presidente_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@presidente_controller.delete(
    "/{presidente_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete presidente",
    response_description="Delete confirmation"
)
async def delete_presidente(
    presidente_id: int,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    response = await presidente_service.eliminar_presidente(presidente_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
