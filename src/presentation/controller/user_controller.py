from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependency_injection.dependency_injection import build_usuario_service
from src.core.services.usuario_service import UsuarioService
from src.core.models.usuario_domain import UsuarioCreate, UsuarioUpdate
from src.responses.response import Response
from src.presentation.dto.user_dto import UserLoginDTO, UserLogOutDTO, UserUpdatePasswordDTO, UserCodeDTO, UserResetPasswordDTO, UserDeactivateDTO

user_controller = APIRouter(prefix="/api/v1/users", tags=["Users"])

@user_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_data: UsuarioCreate,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:
    
    response = await usuario_service.crear_usuario(user_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all active users",
    response_description="List of active users"
)
async def get_all_users(
    skip: int = 0,
    limit: int = 100,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:
    response = await usuario_service.listar_usuarios(skip, limit)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@user_controller.get(
    "/email/{email}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get user by email",
    response_description="User details"
)
async def get_user_by_email(
    email: str,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.obtener_usuario_por_email(email)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.put(
    "/{user_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update user information",
    response_description="Updated user details"
)
async def update_user(
    user_id: int,
    user_data: UsuarioUpdate,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.actualizar_usuario(user_id, user_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.delete(
    "/{user_id}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Deactivate user",
    response_description="Deactivation confirmation"
)
async def deactivate_user(
    user_id: int,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.desactivar_usuario(user_id)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.post(
    "/verify_code",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Verify user code",
    response_description="Verification result"
)
async def verify_code(
    code_user: UserCodeDTO,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.verificar_codigo(code_user.email, code_user.code)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@user_controller.post(
    "/authenticate",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Authenticate user",
    response_description="Authentication result"
)
async def authenticate_user(
    usuario : UserLoginDTO,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.autenticar_usuario(usuario.email, usuario.password)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.post(
    "/unauthenticate",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Unauthenticate user",
    response_description="Unauthentication result"
)
async def unauthenticate_user(
    user : UserLogOutDTO,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.unauthenticate_usuario(user.email)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.put(
    "/update_password/{user_email}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Update user password",
    response_description="Password update result"
)
async def update_password(
    user_email: str,
    user: UserUpdatePasswordDTO,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.actualizar_contrasena(user_email, user.old_password, user.new_password)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.get(
    "/verify_email/{email}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Verify if email exists",
    response_description="Email existence result"
)
async def verify_email(
    email: str,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.veryficar_exist_email(email)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
@user_controller.post(
    "/verify_email_for_recovery",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Verify email for password recovery",
    response_description="Email verification result"
)
async def verify_email_for_recovery(
    email: str,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.verificar_email_for_recovery(email)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@user_controller.put(
    "/reset_password/{email}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Reset user password",
    response_description="Password reset result"
)
async def reset_password(
    email: str,
    user: UserResetPasswordDTO,
    usuario_service: UsuarioService = Depends(build_usuario_service)
) -> Response:

    response = await usuario_service.reset_password(email, user.new_password)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
