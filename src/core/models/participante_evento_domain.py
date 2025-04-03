from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB  
from src.core.models.evento_domain import EventoInDB  
from typing import Optional

class ParticipanteEventoBase(BaseModel):
    id_usuario: int
    id_evento: int

class ParticipanteEventoCreate(ParticipanteEventoBase):
    estado_asistencia: bool = False

class ParticipanteEventoUpdate(BaseModel):
    estado_asistencia: Optional[bool] = None

class ParticipanteEventoInDB(ParticipanteEventoBase):
    estado_asistencia: bool
    usuario: Optional[UsuarioInDB] = None
    evento: Optional[EventoInDB] = None

    class Config:
        from_attributes = True