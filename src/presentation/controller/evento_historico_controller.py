from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_evento_historico_service
from src.core.services.evento_historico_service import EventoHistoricoService
from src.responses.response import Response
from src.core.models.evento_historico_domain import EventoHistoricoCreate, EventoHistoricoInDB, EventoHistoricoUpdate

eventoHistorico_controller = APIRouter(prefix="/api/v1/eventos_historicos", tags=["Eventos Historicos"])

@eventoHistorico_controller.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new event",
    response_description="Event created successfully"
)
async def create_evento_historico(
    evento_historico_data: EventoHistoricoCreate,
    evento_historico_service: EventoHistoricoService = Depends(build_evento_historico_service)
):
    
    response = await evento_historico_service.crear_evento_historico(evento_historico_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@eventoHistorico_controller.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get all events",
    response_description="List of events"
)
async def get_all_eventos_historicos(
    skip: int = 0,
    limit: int = 100,
    evento_historico_service: EventoHistoricoService = Depends(build_evento_historico_service)
):
    response = await evento_historico_service.obtener_eventos_historicos(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@eventoHistorico_controller.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get event by ID",
    response_description="Event details"
)
async def get_evento_historico_by_id(
    id: int,
    evento_historico_service: EventoHistoricoService = Depends(build_evento_historico_service)
):
    response = await evento_historico_service.obtener_evento_historico_por_id(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@eventoHistorico_controller.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Update event by ID",
    response_description="Event updated successfully"
)
async def update_evento_historico(
    id: int,
    evento_historico_data: EventoHistoricoUpdate,
    evento_historico_service: EventoHistoricoService = Depends(build_evento_historico_service)
):
    response = await evento_historico_service.actualizar_evento_historico(id, evento_historico_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@eventoHistorico_controller.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete event by ID",
    response_description="Event deleted successfully"
)
async def delete_evento_historico(
    id: int,
    evento_historico_service: EventoHistoricoService = Depends(build_evento_historico_service)
):
    response = await evento_historico_service.eliminar_evento_historico(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
