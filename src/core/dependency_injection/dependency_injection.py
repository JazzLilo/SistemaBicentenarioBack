from src.infrastrucutre.conecction import get_connection
from fastapi import Depends

from src.infrastrucutre.repository.auditoria_repository import AuditoriaRepository
from src.infrastrucutre.repository.UserRepository import UsuarioRepository
from src.infrastrucutre.repository.usuario_rol_repository import UsuarioRolRepository
from src.infrastrucutre.repository.rol_repository import RolRepository
from src.infrastrucutre.repository.presidente_repository import PresidenteRepository
from src.infrastrucutre.repository.ubicacion_respository import UbicacionRepository

from src.core.services.auditoria_service import AuditoriaService
from src.core.services.usuario_service import UsuarioService
from src.core.services.usuario_rol_sevice import UsuarioRolService
from src.core.services.rol_service import RolService
from src.core.services.presidente_service import PresidenteService
from src.core.services.ubicacion_service import UbicacionService

def build_usuario_service(
    conecction = Depends(get_connection)
):
    return UsuarioService(UsuarioRepository(conecction))

def build_usuario_rol_service(
    conecction = Depends(get_connection)
):
    return UsuarioRolService(UsuarioRolRepository(conecction))

def build_rol_service(
    conecction = Depends(get_connection)
):
    return RolService(RolRepository(conecction))

def build_auditoria_service(
    conecction = Depends(get_connection)
):
    return AuditoriaService(AuditoriaRepository(conecction))

def build_presidente_service(
    conecction = Depends(get_connection)
):
    return PresidenteService(PresidenteRepository(conecction))

def build_ubicacion_service(
    conecction = Depends(get_connection)
):
    return UbicacionService(UbicacionRepository(conecction))