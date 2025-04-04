from fastapi import APIRouter, Depends
from src.core.models.c_h_domain import CategoriaEventoHistoricoCreate
from src.core.dependency_injection.dependency_injection import build_categoria_evento_historico_service 
from src.core.services.c_h_service import CategoriaEventoHistoricoService
from src.responses.response import Response

categoriaHistoria_controller = APIRouter(prefix="/categoria-evento-historico", tags=["Relaciones Categoría-Evento"])

@categoriaHistoria_controller.post("/", response_model=Response)
async def crear_relacion(
    relacion: CategoriaEventoHistoricoCreate,
    service: CategoriaEventoHistoricoService = Depends(build_categoria_evento_historico_service)
):
    return await service.crear_relacion(relacion)

@categoriaHistoria_controller.get("/evento/{id_evento}/categoria/{id_categoria}", response_model=Response)
async def obtener_relacion(
    id_evento: int,
    id_categoria: int,
    service: CategoriaEventoHistoricoService = Depends(build_categoria_evento_historico_service)
):
    return await service.obtener_por_ids(id_evento, id_categoria)

@categoriaHistoria_controller.get("/evento/{id_evento}/categorias", response_model=Response)
async def obtener_categorias_de_evento(
    id_evento: int,
    service: CategoriaEventoHistoricoService = Depends(build_categoria_evento_historico_service)
):
    return await service.obtener_categorias_por_evento(id_evento)

@categoriaHistoria_controller.delete("/evento/{id_evento}/categoria/{id_categoria}", response_model=Response)
async def eliminar_relacion(
    id_evento: int,
    id_categoria: int,
    service: CategoriaEventoHistoricoService = Depends(build_categoria_evento_historico_service)
):
    return await service.eliminar_relacion(id_evento, id_categoria)