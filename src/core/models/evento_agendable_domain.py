from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB
from src.core.models.participante_evento_domain import ParticipanteEventoInDB
from src.core.models.agenda_usuario_domain import AgendaUsuarioInDB

class EventoAgendableBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_hora: datetime
    id_ubicacion: Optional[int] = None
    id_organizador: int
    imagen: Optional[str] = None

class EventoAgendableCreate(EventoAgendableBase):
    pass

class EventoAgendableUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_hora: Optional[datetime] = None
    id_ubicacion: Optional[int] = None
    imagen: Optional[str] = None

class EventoAgendableInDB(EventoAgendableBase):
    id: int
    ubicacion: Optional['UbicacionInDB'] = None
    organizador: Optional[UsuarioInDB] = None
    class Config:
        from_attributes = True

class EventoAgendableWithRelations(EventoAgendableInDB):
    ubicacion: Optional['UbicacionInDB'] = None
    organizador: UsuarioInDB
    participantes: List['ParticipanteEventoInDB'] = []
    agendas: List['AgendaUsuarioInDB'] = []
    comentarios: List['ComentarioInDB'] = []