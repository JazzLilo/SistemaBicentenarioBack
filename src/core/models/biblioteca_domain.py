from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .tipodocumento_domain import TipoDocumentoInDB

class BibliotecaBase(BaseModel):
    titulo: str
    autor: str
    id_tipo: int

class BibliotecaCreate(BibliotecaBase):
    imagen: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    edicion: Optional[str] = None
    fuente: Optional[str] = None
    enlace: Optional[str] = None

class BibliotecaUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    imagen: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    edicion: Optional[str] = None
    id_tipo: Optional[int] = None
    fuente: Optional[str] = None
    enlace: Optional[str] = None

class BibliotecaInDB(BibliotecaBase):
    id: int
    imagen: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    edicion: Optional[str] = None
    fuente: Optional[str] = None
    enlace: Optional[str] = None
    tipo: TipoDocumentoInDB

    class Config:
        from_attributes = True