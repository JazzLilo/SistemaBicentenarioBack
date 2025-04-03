from fastapi import APIRouter, Depends, HTTPException, status

from src.core.models.usuario_rol_domain import UsuarioRolCreate, UsuarioRolInDB
from src.core.dependency_injection.dependency_injection import build_usuario_rol_service
from src.core.services.usuario_rol_sevice import UsuarioRolService
from src.responses.response import Response

user_role_controller = APIRouter(prefix="/api/v1/user_roles", tags=["User Roles"])

@user_role_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def assign_role_to_user(
    user_role_data: UsuarioRolCreate,
    usuario_rol_service: UsuarioRolService = Depends(build_usuario_rol_service)
) -> Response:
    
    response = await usuario_rol_service.asignar_rol_a_usuario(user_role_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_role_controller.get(
    "/{id_usuario}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get roles by user ID",
    response_description="List of roles for the specified user"
)
async def get_roles_by_user(
    id_usuario: int,
    usuario_rol_service: UsuarioRolService = Depends(build_usuario_rol_service)
) -> Response:
    response = await usuario_rol_service.obtener_roles_por_usuario(id_usuario)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_role_controller.delete(
    "/{id_usuario}/{id_rol}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Remove role from user",
    response_description="Role removed successfully"
)
async def remove_role_from_user(
    id_usuario: int,
    id_rol: int,
    usuario_rol_service: UsuarioRolService = Depends(build_usuario_rol_service)
) -> Response:
    response = await usuario_rol_service.remove_rol_from_usuario(id_usuario, id_rol)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
