from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_participante_evento_service
from src.core.services.participante_evento_service import ParticipanteEventoService
from src.core.models.participante_evento_domain import ParticipanteEventoCreate, ParticipanteEventoUpdate
from src.responses.response import Response

participante_evento_controller = APIRouter(prefix="/api/v1/participantes_eventos", tags=["Participantes Eventos"])  

@participante_evento_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
    summary="Agregar Participante a Evento",
    response_description="Participante agregado exitosamente"
)
async def agregar_participante(
    participante: ParticipanteEventoCreate,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.agregar_participante(participante)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.get(
    "/{id_usuario}/{id_evento}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Obtener Participante por Evento"
)
async def obtener_participante(	
    id_usuario: int,
    id_evento: int,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.obtener_participante(id_usuario, id_evento)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.put(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Actualizar Asistencia",
    response_description="Asistencia actualizada exitosamente"
)
async def actualizar_asistencia(
    id_usuario: int,
    id_evento: int,
    update_data: ParticipanteEventoUpdate,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.actualizar_asistencia(id_usuario, id_evento, update_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.delete(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Eliminar Participante de Evento",
    response_description="Participante eliminado exitosamente"
)
async def eliminar_participante(
    id_usuario: int,
    id_evento: int,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.eliminar_participante(id_usuario, id_evento)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@participante_evento_controller.get(
    "/participantes",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Listar Participantes por Evento",
    response_description="Lista de participantes por evento"
)
async def listar_participantes_por_evento(
    id_evento: int,
    participante_evento_service: ParticipanteEventoService = Depends(build_participante_evento_service)
) -> Response:
    response = await participante_evento_service.listar_participantes_por_evento(id_evento)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
    
