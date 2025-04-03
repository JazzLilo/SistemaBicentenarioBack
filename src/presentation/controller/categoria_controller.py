from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_categoria_service
from src.core.services.categoria_service import CategoriaService
from src.core.models.categoria_domain import CategoriaCreate, CategoriaUpdate
from src.responses.response import Response

categoria_controller = APIRouter(prefix="/api/v1/categorias", tags=["Categorias"])  

@categoria_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_categoria(
    categoria_data: CategoriaCreate,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:
    
    response = await categoria_service.crear_categoria(categoria_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@categoria_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all active categories",
    response_description="List of active categories"
)
async def get_all_categorias(
    skip: int = 0,
    limit: int = 100,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:
    response = await categoria_service.obtener_categorias(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@categoria_controller.get(
    "/{categoria_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get category by ID",
    response_description="Category details"
)
async def get_categoria_by_id(
    categoria_id: int,
    include_historias: bool = False,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:

    response = await categoria_service.obtener_categoria_por_id(categoria_id, include_historias)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@categoria_controller.put(
    "/{categoria_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update category",
    response_description="Category updated successfully"
)
async def update_categoria(
    categoria_id: int,
    categoria_data: CategoriaUpdate,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:

    response = await categoria_service.actualizar_categoria(categoria_id, categoria_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@categoria_controller.delete(
    "/{categoria_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Delete category",
    response_description="Category deleted successfully"
)
async def delete_categoria(
    categoria_id: int,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:

    response = await categoria_service.eliminar_categoria(categoria_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

