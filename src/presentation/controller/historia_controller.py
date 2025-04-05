from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_historia_service
from src.core.services.historia_service import HistoriaService
from src.core.models.historia_domain import (
    HistoriaCreate,
    HistoriaInDB,
    HistoriaUpdate,
    HistoriaWithRelations
)
from src.responses.response import Response

historia_controller = APIRouter(prefix="/api/v1/historias", tags=["Historias"])

@historia_controller.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Crear Historia",
    response_description="Historia creada"
)
async def create_historia(
    historia_data: HistoriaCreate,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.crear_historia(historia_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Obtener Historia por ID",
    response_description="Historia encontrada"
)
async def get_historia_by_id(
    id: int,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.obtener_historia_por_id(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Actualizar Historia",
    response_description="Historia actualizada"
)
async def update_historia(
    id: int,
    historia_data: HistoriaUpdate,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.actualizar_historia(id, historia_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar Historia",
    response_description="Historia eliminada"
)
async def delete_historia(
    id: int,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.eliminar_historia(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Listar Historias",
    response_description="Lista de historias"
)
async def get_all_historias(
    skip: int = 0,
    limit: int = 100,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.listar_historias(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@historia_controller.get(
    "/search",
    status_code=status.HTTP_200_OK,
    summary="Buscar Historias por Título",
    response_description="Lista de historias encontradas"
)
async def search_historias_by_title(
    titulo: str,
    skip: int = 0,
    limit: int = 100,
    historia_service: HistoriaService = Depends(build_historia_service)
):
    response = await historia_service.buscar_historias_por_titulo(titulo, skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response