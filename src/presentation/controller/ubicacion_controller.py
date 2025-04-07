from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_ubicacion_service
from src.core.models.ubicacion_domain import UbicacionCreate, UbicacionInDB, UbicacionUpdate
from src.core.services.ubicacion_service import UbicacionService
from src.responses.response import Response


ubicacion_controller = APIRouter(prefix="/api/v1/ubicaciones", tags=["Ubicaciones"])

@ubicacion_controller.post(
    "/",
    response_model=Response,
)
async def create_location(
    location_data: UbicacionCreate,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:
    response = await ubicacion_service.crear_ubicacion(location_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@ubicacion_controller.put(
    "/{id_ubicacion}",
    response_model=Response,
)
async def update_location(
    id_ubicacion: int,
    location_data: UbicacionInDB,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:
    response = await ubicacion_service.actualizar_ubicacion(id_ubicacion, location_data)
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
    summary="Get all locations",
    response_description="List of locations"
)
async def get_all_locations(
    skip: int = 0,
    limit: int = 100,
    tipo: str = None,
    ubicacion_service: UbicacionService = Depends(build_ubicacion_service)
) -> Response:
    response = await ubicacion_service.obtener_ubicaciones(skip, limit, tipo)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response