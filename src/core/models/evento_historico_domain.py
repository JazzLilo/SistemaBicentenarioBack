from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from src.core.models.ubicacion_domain import UbicacionInDB

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
    ubicacion: Optional[UbicacionInDB] = None

    class Config:
        from_attributes = True

class EventoHistoricoWithRelations(EventoHistoricoInDB):
    ubicacion: Optional['UbicacionInDB'] = None
    bibliotecas: List['BibliotecaInDB'] = []
    documentos: List['BibliotecaInDB'] = []
    multimedia: List['MultimediaInDB'] = []
    categorias: List['CategoriaEventoHistoricoInDB'] = []
    agendas: List['AgendaUsuarioInDB'] = []
    comentarios: List['ComentarioInDB'] = []