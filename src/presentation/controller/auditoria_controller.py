from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_auditoria_service
from src.core.services.auditoria_service import AuditoriaService
from src.responses.response import Response
from src.core.models.auditoria_domain import AuditoriaCreate, AuditoriaInDB, AuditoriaUpdate

auditoria_controller = APIRouter(prefix="/api/v1/auditoria", tags=["Auditoria"])

@auditoria_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_auditoria(
    auditoria_data: AuditoriaCreate,
    auditoria_service: AuditoriaService = Depends(build_auditoria_service)
) -> Response:
    
    response = await auditoria_service.create_auditoria(auditoria_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@auditoria_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all auditorias",
    response_description="List of auditorias"
)

async def get_all_auditorias(
    auditoria_service: AuditoriaService = Depends(build_auditoria_service)
) -> Response:
    response = await auditoria_service.get_all_auditorias()
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response

@auditoria_controller.get(
    "/{id_usuario}",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get auditoria by user ID",
    response_description="Auditoria details"
)
async def get_auditoria_by_user_id(
    id_usuario: int,
    auditoria_service: AuditoriaService = Depends(build_auditoria_service)
) -> Response:
    response = await auditoria_service.get_auditoria_by_user_id(id_usuario)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response