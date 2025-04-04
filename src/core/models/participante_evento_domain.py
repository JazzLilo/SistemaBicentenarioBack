from typing import Optional
from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB
from src.core.models.evento_agendable_domain import EventoAgendableInDB

class ParticipanteEventoBase(BaseModel):
    id_usuario: int
    id_evento: int
    estado_asistencia: bool = False

class ParticipanteEventoCreate(ParticipanteEventoBase):
    pass

class ParticipanteEventoUpdate(BaseModel):
    estado_asistencia: Optional[bool] = None

class ParticipanteEventoInDB(ParticipanteEventoBase):
    class Config:
        from_attributes = True

class ParticipanteEventoWithRelations(ParticipanteEventoInDB):
    usuario: Optional['UsuarioInDB'] = None
    evento: Optional['EventoAgendableInDB'] = None