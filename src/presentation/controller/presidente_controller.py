from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_presidente_service
from src.core.services.presidente_service import PresidenteService
from src.core.models.presidente_domain import PresidenteCreate, PresidenteUpdate
from src.responses.response import Response

presidente_controller = APIRouter(prefix="/api/v1/presidentes", tags=["Presidentes"])

@presidente_controller.post("/", response_model=Response)
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
    summary="Get all active presidents",
    response_description="List of active presidents"
)
async def get_all_presidentes(
    skip: int = 0,
    limit: int = 100,
    partido: str = None,
    periodo_activo: bool = False,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:
    response = await presidente_service.obtener_presidentes(skip, limit, partido, periodo_activo)
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
    summary="Get president by ID",
    response_description="President details"
)
async def get_presidente_by_id(
    presidente_id: int,
    presidente_service: PresidenteService = Depends(build_presidente_service)
) -> Response:

    response = await presidente_service.obtener_presidente(presidente_id)
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
    summary="Update president by ID",
    response_description="Updated president details"
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
    summary="Delete president by ID",
    response_description="Deleted president details"
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

