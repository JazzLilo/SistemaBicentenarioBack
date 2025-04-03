from pydantic import BaseModel, Field
from typing import Optional
from src.core.models.ubicacion_domain import UbicacionInDB  

class CulturaBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    descripcion: str
    id_ubicacion: Optional[int] = None

class CulturaCreate(CulturaBase):
    imagen: Optional[str] = Field(None, max_length=500)

class CulturaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    imagen: Optional[str] = Field(None, max_length=500)
    descripcion: Optional[str] = None
    id_ubicacion: Optional[int] = None

class CulturaInDB(CulturaBase):
    id: int
    imagen: Optional[str] = Field(None, max_length=500)
    ubicacion: Optional[UbicacionInDB] = None

    class Config:
        from_attributes = True