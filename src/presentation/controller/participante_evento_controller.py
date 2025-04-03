from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_participante_evento_service

from src.core.services.participante_evento_service import ParticipanteEventoService
from src.core.models.participante_evento_domain import ParticipanteEventoCreate, ParticipanteEventoUpdate
from src.responses.response import Response

participante_evento_controller = APIRouter(prefix="/api/v1/participantes-evento", tags=["Participantes Evento"])

@participante_evento_controller.post("/", response_model=Response)
async def create_participante_evento(
    participante_data: ParticipanteEventoCreate,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    
    response = await participante_evento_service.registrar_participante(participante_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all event participants",
    response_description="List of event participants"
)
async def get_all_participantes_evento(
    evento_id: int,
    skip: int = 0,
    limit: int = 100,
    confirmados: bool = None,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.obtener_participantes_evento(evento_id, skip, limit, confirmados)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.get(
    "/usuario/{usuario_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get events by user ID",
    response_description="List of events by user ID"
)
async def get_eventos_usuario(
    usuario_id: int,
    skip: int = 0,
    limit: int = 100,
    confirmados: bool = None,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.obtener_eventos_usuario(usuario_id, skip, limit, confirmados)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.put(
    "/{usuario_id}/{evento_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update attendance status",
    response_description="Attendance status updated successfully"
)
async def update_asistencia(
    usuario_id: int,
    evento_id: int,
    participante_data: ParticipanteEventoUpdate,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    
    response = await participante_evento_service.actualizar_asistencia(usuario_id, evento_id, participante_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.delete(
    "/{usuario_id}/{evento_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete participant from event",
    response_description="Participant deleted successfully"
)
async def delete_participante_evento(
    usuario_id: int,
    evento_id: int,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    
    response = await participante_evento_service.eliminar_participante(usuario_id, evento_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
