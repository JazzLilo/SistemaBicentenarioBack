from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_evento_agendable_service
from src.core.services.evento_agendable_service import EventoAgendableService
from src.core.models.evento_agendable_domain import EventoAgendableCreate, EventoAgendableUpdate
from src.responses.response import Response

evento_agendable_controller = APIRouter(prefix="/api/v1/eventos-agendables", tags=["Eventos Agendables"])

@evento_agendable_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_evento_agendable(
    evento: EventoAgendableCreate,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.crear_evento_agendable(evento)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_agendable_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all events",
    response_description="List of events"
)
async def get_all_eventos_agendables(
    skip: int = 0,
    limit: int = 100,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.obtener_eventos_agendables(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_agendable_controller.get(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get event by ID",
    response_description="Event details"
)
async def get_evento_agendable_by_id(
    id: int,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.obtener_evento_agendable_por_id(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_agendable_controller.put(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update event",
    response_description="Updated event details"
)
async def update_evento_agendable(
    id: int,
    evento: EventoAgendableUpdate,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.actualizar_evento_agendable(id, evento)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_agendable_controller.delete(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete event",
    response_description="Event deletion status"
)
async def delete_evento_agendable(
    id: int,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.eliminar_evento_agendable(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@evento_agendable_controller.get(
    "/organizador/{id_organizador}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get events by organizer ID",
    response_description="List of events by organizer"
)
async def get_eventos_agendables_por_organizador(
    id_organizador: int,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.obtener_eventos_agendables_por_organizador(id_organizador)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@evento_agendable_controller.get(
    "/categoriasEve/{id}",
    response_model=Response,  # Agregar response model
    status_code=status.HTTP_200_OK,  # Especificar código de estado
    summary="Get categories",
    response_description="List of categories"
)
async def get_categories(
    id: int,
    evento_agendable_service: EventoAgendableService = Depends(build_evento_agendable_service)
) -> Response:
    response = await evento_agendable_service.obtener_categorias()
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

# El resto de los endpoints mantienen su orden original...
