from fastapi import APIRouter, Depends, HTTPException, status
from src.core.dependency_injection.dependency_injection import build_tipo_documento_service
from src.core.services.tipo_documento_service import TipoDocumentoService
from src.responses.response import Response

from src.core.models.tipo_documento_domain import TipoDocumentoCreate, TipoDocumentoInDB, TipoDocumentoUpdate


tipo_documento_controller = APIRouter(prefix="/api/v1/tipos-documento", tags=["Tipos de Documento"])

@tipo_documento_controller.post(
    "/",
    response_model=Response,
    status_code=status.HTTP_201_CREATED,
)
async def create_tipo_documento(
    tipo_documento_data: TipoDocumentoCreate,
    tipo_documento_service: TipoDocumentoService = Depends(build_tipo_documento_service)
) -> Response:
    
    response = await tipo_documento_service.crear_tipo_documento(tipo_documento_data)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response


@tipo_documento_controller.get(
    "/",
    response_model=Response,
    status_code=status.HTTP_200_OK,
    summary="Get all tipos de documento",
    response_description="List of tipos de documento"
)
async def get_all_tipos_documento(
    skip: int = 0,
    limit: int = 100,
    incluir_bibliotecas: bool = False,
    tipo_documento_service: TipoDocumentoService = Depends(build_tipo_documento_service)
) -> Response:
    response = await tipo_documento_service.listar_tipos_documento(skip, limit, incluir_bibliotecas)
    if not response.success:
        raise HTTPException(
            status_code=response.status,
            detail=response.message
        )
    return response
