from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl
from src.core.models.tipo_documento_domain import TipoDocumentoInDB
from src.core.models.comentario_domain import ComentarioInDB

class BibliotecaBase(BaseModel):
    titulo: str
    autor: str
    imagen: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    edicion: Optional[str] = None
    id_tipo: int
    fuente: Optional[str] = None
    enlace: Optional[HttpUrl] = None  # Validates URL format

class BibliotecaCreate(BibliotecaBase):
    pass

class BibliotecaUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    imagen: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    edicion: Optional[str] = None
    id_tipo: Optional[int] = None
    fuente: Optional[str] = None
    enlace: Optional[HttpUrl] = None

class BibliotecaInDB(BibliotecaBase):
    id: int

    class Config:
        from_attributes = True

class BibliotecaWithRelations(BibliotecaInDB):
    tipo: 'TipoDocumentoInDB'
    eventos_historicos: List['EventoHistoricoInDB'] = []
    comentarios: List['ComentarioInDB'] = []