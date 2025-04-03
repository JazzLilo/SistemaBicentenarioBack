from src.infrastrucutre.conecction import get_connection
from fastapi import Depends

from src.infrastrucutre.repository.UserRepository import UsuarioRepository
from src.infrastrucutre.repository.ubicacion_repository import UbicacionRepository
from src.infrastrucutre.repository.categoria_repository import CategoriaRepository
from src.infrastrucutre.repository.historia_repository import HistoriaRepository
from src.infrastrucutre.repository.presidente_repository import PresidenteRepository
from src.infrastrucutre.repository.cultura_repository import CulturaRepository
from src.infrastrucutre.repository.evento_repository import EventoRepository
from src.infrastrucutre.repository.participante_evento_repository import ParticipanteEventoRepository
from src.infrastrucutre.repository.biblioteca_repository import BibliotecaRepository
from src.infrastrucutre.repository.comentario_repository import ComentarioRepository
from src.infrastrucutre.repository.usuario_rol_repository import UsuarioRolRepository
from src.infrastrucutre.repository.rol_repository import RolRepository

from src.core.services.usuario_service import UsuarioService
from src.core.services.ubicacion_service import UbicacionService
from src.core.services.categoria_service import CategoriaService
from src.core.services.historia_service import HistoriaService
from src.core.services.presidente_service import PresidenteService
from src.core.services.cultura_service import CulturaService
from src.core.services.evento_service import EventoService
from src.core.services.participante_evento_service import ParticipanteEventoService
from src.core.services.biblioteca_service import BibliotecaService
from src.core.services.comentario_service import ComentarioService
from src.core.services.usuario_rol_sevice import UsuarioRolService
from src.core.services.rol_service import RolService

def build_usuario_service(
    conecction = Depends(get_connection)
):
    return UsuarioService(UsuarioRepository(conecction))

def build_ubicacion_service(
    conecction = Depends(get_connection)
):
    return UbicacionService(UbicacionRepository(conecction))

def build_categoria_service(
    conecction = Depends(get_connection)
):
    return CategoriaService(CategoriaRepository(conecction))

def build_historia_service(
    conecction = Depends(get_connection)
):
    return HistoriaService(HistoriaRepository(conecction))

def build_presidente_service(
    conecction = Depends(get_connection)
):
    return PresidenteService(PresidenteRepository(conecction))

def build_cultura_service(
    conecction = Depends(get_connection)
):
    return CulturaService(CulturaRepository(conecction))

def build_evento_service(
    conecction = Depends(get_connection)
):
    return EventoService(EventoRepository(conecction))

def build_participante_evento_service(
    conecction = Depends(get_connection)
):
    return ParticipanteEventoService(ParticipanteEventoRepository(conecction))

def build_biblioteca_service(
    conecction = Depends(get_connection)
):
    return BibliotecaService(BibliotecaRepository(conecction))

def build_comentario_service(
    conecction = Depends(get_connection)
):
    return ComentarioService(ComentarioRepository(conecction))

def build_usuario_rol_service(
    conecction = Depends(get_connection)
):
    return UsuarioRolService(UsuarioRolRepository(conecction))

def build_rol_service(
    conecction = Depends(get_connection)
):
    return RolService(RolRepository(conecction))