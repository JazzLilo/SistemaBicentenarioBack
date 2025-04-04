from typing import Optional
from pydantic import BaseModel

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