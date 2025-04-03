from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .ubicacion_domain import UbicacionInDB
from .categoria_domain import CategoriaInDB

class HistoriaBase(BaseModel):
    titulo: str = Field(..., max_length=255)
    descripcion: str
    id_categoria: int
    id_ubicacion: Optional[int] = None

class HistoriaCreate(HistoriaBase):
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    imagen: Optional[str] = Field(None, max_length=500)

class HistoriaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=255)
    descripcion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    imagen: Optional[str] = Field(None, max_length=500)
    id_ubicacion: Optional[int] = None
    id_categoria: Optional[int] = None

class HistoriaInDB(HistoriaBase):
    id: int
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    imagen: Optional[str] = Field(None, max_length=500)
    ubicacion: Optional[UbicacionInDB] = None
    categoria: CategoriaInDB

    class Config:
        from_attributes = True

