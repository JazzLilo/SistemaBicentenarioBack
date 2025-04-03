from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UbicacionBase(BaseModel):
    nombre: str
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    descripcion: Optional[str] = None

class UbicacionCreate(UbicacionBase):
    imagen: Optional[str] = None

class UbicacionUpdate(BaseModel):
    nombre: Optional[str] = None
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    imagen: Optional[str] = None
    descripcion: Optional[str] = None

class UbicacionInDB(UbicacionBase):
    id: int
    imagen: Optional[str] = None

    class Config:
        from_attributes = True