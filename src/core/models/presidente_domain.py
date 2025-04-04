from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PresidenteBase(BaseModel):
    nombre: str
    apellido: str
    imagen: Optional[str] = None
    periodo_inicio: Optional[datetime] = None
    periodo_fin: Optional[datetime] = None
    biografia: Optional[str] = None
    partido_politico: Optional[str] = None
    politicas_clave: Optional[str] = None

class PresidenteCreate(PresidenteBase):
    pass  

class PresidenteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    imagen: Optional[str] = None
    periodo_inicio: Optional[datetime] = None
    periodo_fin: Optional[datetime] = None
    biografia: Optional[str] = None
    partido_politico: Optional[str] = None
    politicas_clave: Optional[str] = None

class PresidenteInDB(PresidenteBase):
    id: int

    class Config:
        from_attributes = True 