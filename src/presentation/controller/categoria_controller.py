from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_categoria_service
from src.core.services.categoria_service import CategoriaService
from src.responses.response import Response

categoria_controller = APIRouter(prefix="/api/v1/categorias", tags=["Categorias"])

@categoria_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all categorias",
    response_description="List of categorias"
)
async def get_all_categorias(
    skip: int = 0,
    limit: int = 100,
    categoria_service: CategoriaService = Depends(build_categoria_service)
) -> Response:
    response = await categoria_service.get_categorias(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response