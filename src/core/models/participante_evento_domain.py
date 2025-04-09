from typing import Optional
from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB

class ParticipanteEventoBase(BaseModel):
    id_usuario: int
    id_evento: int
    estado_asistencia: int = 0

class ParticipanteEventoCreate(ParticipanteEventoBase):
    pass

class ParticipanteEventoUpdate(BaseModel):
    estado_asistencia: Optional[int] = None

class ParticipanteEventoInDB(ParticipanteEventoBase):
    class Config:
        from_attributes = True

class ParticipanteEventoWithRelations(ParticipanteEventoInDB):
    usuario: Optional['UsuarioInDB'] = None
    evento: Optional['EventoAgendableInDB'] = None