from typing import Optional
from pydantic import BaseModel

class CulturaBase(BaseModel):
    nombre: str
    descripcion: str
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None

class CulturaCreate(CulturaBase):
    pass

class CulturaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None

class CulturaInDB(CulturaBase):
    id: int

    class Config:
        from_attributes = True

class CulturaWithRelations(CulturaInDB):
    ubicacion: Optional['UbicacionInDB'] = None