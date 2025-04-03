from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_rol_service
from src.core.services.rol_service import RolService
from src.responses.response import Response
from src.core.models.rol_domain import RolCreate, RolInDB, RolUpdate

rol_controller = APIRouter(prefix="/api/v1/roles", tags=["Roles"])

@rol_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_role(
    role_data: RolCreate,
    usuario_rol_service: RolService = Depends(build_rol_service)
) -> Response:
    
    response = await usuario_rol_service.crear_rol(role_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@rol_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all roles",
    response_description="List of roles"
)
async def get_all_roles(
    skip: int = 0,
    limit: int = 100,
    usuario_rol_service: RolService = Depends(build_rol_service)
) -> Response:
    response = await usuario_rol_service.obtener_roles(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
