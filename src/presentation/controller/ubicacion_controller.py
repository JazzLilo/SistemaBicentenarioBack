from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_ubicacion_service

from src.core.services.ubicacion_service import UbicacionService
from src.core.models.ubicacion_domain import UbicacionCreate, UbicacionUpdate
from src.responses.response import Response

ubicacion_controller = APIRouter(prefix="/api/v1/ubicaciones", tags=["Ubicaciones"])


@ubicacion_controller.post("/",response_model=Response)
async def create_ubicacion(
    ubicacion_data: UbicacionCreate,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:
    
    response = await ubicacion_service.crear_ubicacion(ubicacion_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@ubicacion_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all active locations",
    response_description="List of active locations"
)
async def get_all_ubicaciones(
    skip: int = 0,
    limit: int = 100,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:
    response = await ubicacion_service.obtener_ubicaciones(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@ubicacion_controller.get(
    "/{ubicacion_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get location by ID",
    response_description="Location details"
)
async def get_ubicacion_by_id(
    ubicacion_id: int,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:

    response = await ubicacion_service.obtener_ubicacion_por_id(ubicacion_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@ubicacion_controller.put(
    "/{ubicacion_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update location by ID",
    response_description="Updated location details"
)
async def update_ubicacion(
    ubicacion_id: int,
    ubicacion_data: UbicacionUpdate,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:

    response = await ubicacion_service.actualizar_ubicacion(ubicacion_id, ubicacion_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@ubicacion_controller.delete(
    "/{ubicacion_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete location by ID",
    response_description="Deletion confirmation"
)
async def delete_ubicacion(
    ubicacion_id: int,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:

    response = await ubicacion_service.eliminar_ubicacion(ubicacion_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
