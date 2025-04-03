from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_evento_service
from src.core.services.evento_service import EventoService
from src.core.models.evento_domain import EventoCreate, EventoUpdate
from src.responses.response import Response

evento_controller = APIRouter(prefix="/api/v1/eventos", tags=["Eventos"])

@evento_controller.post("/", response_model=Response)
async def create_evento(
    evento_data: EventoCreate,
    evento_service: EventoService = Depends(build_evento_service)
) -> Response:
    
    response = await evento_service.crear_evento(evento_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all events",
    response_description="List of events"
)
async def get_all_eventos(  
    skip: int = 0,
    limit: int = 100,
    organizador_id: int = None,
    ubicacion_id: int = None,
    fecha_inicio: str = None,
    fecha_fin: str = None,
    evento_service: EventoService = Depends(build_evento_service)
) -> Response:
    response = await evento_service.obtener_eventos(
        skip, limit, organizador_id, ubicacion_id, fecha_inicio, fecha_fin
    )
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@evento_controller.get(
    "/{evento_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get event by ID",
    response_description="Event details"
)
async def get_evento_by_id(
    evento_id: int,
    evento_service: EventoService = Depends(build_evento_service)
) -> Response:

    response = await evento_service.obtener_evento(evento_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_controller.put(
    "/{evento_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update event by ID",
    response_description="Updated event details"
)
async def update_evento_by_id(
    evento_id: int,
    evento_data: EventoUpdate,
    evento_service: EventoService = Depends(build_evento_service)
) -> Response:

    response = await evento_service.actualizar_evento(evento_id, evento_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_controller.delete(
    "/{evento_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete event by ID",
    response_description="Event deletion confirmation"
)
async def delete_evento_by_id(
    evento_id: int,
    evento_service: EventoService = Depends(build_evento_service)
) -> Response:

    response = await evento_service.eliminar_evento(evento_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

