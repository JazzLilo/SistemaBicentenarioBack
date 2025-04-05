from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB

class AgendaUsuarioBase(BaseModel):
    id_usuario: int
    id_evento_historico: Optional[int] = None
    id_evento_agendable: Optional[int] = None
    fecha_recordatorio: Optional[datetime] = None

class AgendaUsuarioCreate(AgendaUsuarioBase):
    pass

class AgendaUsuarioUpdate(BaseModel):
    fecha_recordatorio: Optional[datetime] = None

class AgendaUsuarioInDB(AgendaUsuarioBase):
    id: int

    class Config:
        from_attributes = True

class AgendaUsuarioWithRelations(AgendaUsuarioInDB):
    usuario: Optional['UsuarioInDB'] = None
    evento_historico: Optional['EventoHistoricoInDB'] = None
    evento_agendable: Optional['EventoAgendableInDB'] = None