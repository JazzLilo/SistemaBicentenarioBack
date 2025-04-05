from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from src.core.models.biblioteca_domain import BibliotecaInDB
from src.core.models.multimedia_domain import MultimediaInDB
from src.core.models.agenda_usuario_domain import AgendaUsuarioInDB
from src.core.models.comentario_domain import ComentarioInDB
from src.core.models.biblioteca_domain import BibliotecaInDB


class EventoHistoricoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_inicio: datetime
    fecha_fin: Optional[datetime] = None
    tipo: str
    id_ubicacion: Optional[int] = None

class EventoHistoricoCreate(EventoHistoricoBase):
    pass

class EventoHistoricoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    tipo: Optional[str] = None
    id_ubicacion: Optional[int] = None

class EventoHistoricoInDB(EventoHistoricoBase):
    id: int
    ubicacion: Optional['UbicacionInDB'] = None

    class Config:
        from_attributes = True

class EventoHistoricoWithRelations(EventoHistoricoInDB):
    ubicacion: Optional['UbicacionInDB'] = None
    bibliotecas: List['BibliotecaInDB'] = []
    documentos: List['BibliotecaInDB'] = []
    multimedia: List['MultimediaInDB'] = []
    agendas: List['AgendaUsuarioInDB'] = []
    comentarios: List['ComentarioInDB'] = []