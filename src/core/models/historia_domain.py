from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from src.core.models.categoria_domain import CategoriaInDB

class HistoriaBase(BaseModel):
    titulo: str
    descripcion: str
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None
    id_categoria: int

class HistoriaCreate(HistoriaBase):
    pass

class HistoriaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None
    id_categoria: Optional[int] = None

class HistoriaInDB(HistoriaBase):
    id: int

    class Config:
        from_attributes = True

class HistoriaWithRelations(HistoriaInDB):
    ubicacion: Optional['UbicacionInDB'] = None
    categoria: 'CategoriaInDB'