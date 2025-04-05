from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_biblioteca_service
from src.core.services.biblioteca_service import BibliotecaService

from src.responses.response import Response
from src.core.models.biblioteca_domain import (
    BibliotecaCreate,
    BibliotecaInDB,
    BibliotecaUpdate,
    BibliotecaWithRelations
)

biblioteca_controller = APIRouter(prefix="/api/v1/bibliotecas", tags=["Bibliotecas"])

@biblioteca_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_biblioteca(
    biblioteca_data: BibliotecaCreate,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    
    response = await biblioteca_service.crear_biblioteca(biblioteca_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@biblioteca_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all bibliotecas",
    response_description="List of bibliotecas"
)
async def get_all_bibliotecas(
    skip: int = 0,
    limit: int = 100,
    id_tipo: int = None,
    titulo: str = None,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    response = await biblioteca_service.listar_bibliotecas(skip, limit, id_tipo, titulo)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@biblioteca_controller.get(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get biblioteca by ID",
    response_description="Biblioteca details"
)
async def get_biblioteca_by_id(
    id: int,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    response = await biblioteca_service.obtener_biblioteca(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@biblioteca_controller.put(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update biblioteca",
    response_description="Updated biblioteca details"
)
async def update_biblioteca(
    id: int,
    biblioteca_data: BibliotecaUpdate,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    response = await biblioteca_service.actualizar_biblioteca(id, biblioteca_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@biblioteca_controller.delete(
    "/{id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete biblioteca",
    response_description="Biblioteca deletion status"
)
async def delete_biblioteca(
    id: int,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    response = await biblioteca_service.eliminar_biblioteca(id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@biblioteca_controller.get(
    "/search",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Search bibliotecas by author",
    response_description="List of bibliotecas by author"
)
async def search_bibliotecas_by_author(
    autor: str,
    skip: int = 0,
    limit: int = 100,
    biblioteca_service: BibliotecaService = Depends(build_biblioteca_service)
) -> Response:
    response = await biblioteca_service.buscar_bibliotecas_por_autor(autor, skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

