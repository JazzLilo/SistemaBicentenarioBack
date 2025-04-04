from src.infrastrucutre.conecction import get_connection
from fastapi import Depends

from src.infrastrucutre.repository.auditoria_repository import AuditoriaRepository
from src.infrastrucutre.repository.UserRepository import UsuarioRepository
from src.infrastrucutre.repository.usuario_rol_repository import UsuarioRolRepository
from src.infrastrucutre.repository.rol_repository import RolRepository
from src.infrastrucutre.repository.presidente_repository import PresidenteRepository
from src.infrastrucutre.repository.ubicacion_respository import UbicacionRepository
from src.infrastrucutre.repository.evento_historico_repository import EventoHistoricoRepository
from src.infrastrucutre.repository.categoria_repository import CategoriaRepository
from src.infrastrucutre.repository.c_h_repository import CategoriaEventoHistoricoRepository
from src.infrastrucutre.repository.multimedia_repository import MultimediaRespository
from src.core.services.evento_agendable_service import EventoAgendableRepository
from src.infrastrucutre.repository.participante_evento_repository import ParticipanteEventoRepository

from src.core.services.auditoria_service import AuditoriaService
from src.core.services.usuario_service import UsuarioService
from src.core.services.usuario_rol_sevice import UsuarioRolService
from src.core.services.rol_service import RolService
from src.core.services.presidente_service import PresidenteService
from src.core.services.ubicacion_service import UbicacionService
from src.core.services.evento_historico_service import EventoHistoricoService
from src.core.services.categoria_service import CategoriaService
from src.core.services.c_h_service import CategoriaEventoHistoricoService
from src.core.services.multimedia_service import MultimediaService
from src.core.services.evento_agendable_service import EventoAgendableService
from src.core.services.participante_evento_service import ParticipanteEventoService

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

def build_evento_historico_service(
    conecction = Depends(get_connection)
):
    return EventoHistoricoService(EventoHistoricoRepository(conecction))

def build_categoria_service(
    conecction = Depends(get_connection)
):
    return CategoriaService(CategoriaRepository(conecction))

def build_categoria_evento_historico_service (
    conecction = Depends(get_connection)
):
    return CategoriaEventoHistoricoService(CategoriaEventoHistoricoRepository(conecction))

def build_multimedia_service(
    conecction = Depends(get_connection)
):
    return MultimediaService(MultimediaRespository(conecction))

def build_evento_agendable_service(
    conecction = Depends(get_connection)
):
    return EventoAgendableService(EventoAgendableRepository(conecction))

def build_participante_evento_service(
    conecction = Depends(get_connection)
):
    return ParticipanteEventoService(ParticipanteEventoRepository(conecction))