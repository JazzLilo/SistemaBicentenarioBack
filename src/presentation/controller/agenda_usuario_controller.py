from fastapi import APIRouter, Depends, HTTPException
from src.core.dependency_injection.dependency_injection import build_agenda_usuario_service

from src.core.models.agenda_usuario_domain import (
    AgendaUsuarioCreate,
    AgendaUsuarioInDB,
    AgendaUsuarioUpdate,
)
from src.core.services.agenda_usuario_service import AgendaUsuarioService
from src.responses.response import Response

agenda_usuario_controller = APIRouter(
    prefix="/api/v1/agendas",
    tags=["AgendaUsuario"],
)

@agenda_usuario_controller.post(
    "/",
    response_model=Response,
    status_code=201,
    summary="Crear una nueva agenda de usuario",
    response_description="Agenda de usuario creada exitosamente",
)
async def crear_agenda_usuario(
    agenda: AgendaUsuarioCreate,
    agenda_usuario_service: AgendaUsuarioService = Depends(build_agenda_usuario_service),
) -> Response:
    response = await agenda_usuario_service.crear_agenda_usuario(agenda)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message,
        )
    return response

@agenda_usuario_controller.get(
    "/{id}",
    response_model=Response,
    status_code=200,
    summary="Obtener una agenda de usuario por ID",
    response_description="Agenda de usuario obtenida exitosamente",
)
async def obtener_agenda_por_id(
    id: int,
    agenda_usuario_service: AgendaUsuarioService = Depends(build_agenda_usuario_service),
) -> Response:
    response = await agenda_usuario_service.obtener_agenda_por_id(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message,
        )
    return response

@agenda_usuario_controller.put(
    "/{id}",
    response_model=Response,
    status_code=200,
    summary="Actualizar una agenda de usuario",
    response_description="Agenda de usuario actualizada exitosamente",
)
async def actualizar_agenda_usuario(
    id: int,
    agenda: AgendaUsuarioUpdate,
    agenda_usuario_service: AgendaUsuarioService = Depends(build_agenda_usuario_service),
) -> Response:
    response = await agenda_usuario_service.actualizar_agenda_usuario(id, agenda)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message,
        )
    return response

