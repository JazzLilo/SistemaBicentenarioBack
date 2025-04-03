from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre_categoria: str
    descripcion: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre_categoria: Optional[str] = None
    descripcion: Optional[str] = None

class CategoriaInDB(CategoriaBase):
    id: int
    class Config:
        from_attributes = True

class CategoriaWithHistorias(CategoriaInDB):
    historias: list['HistoriaInDB'] 