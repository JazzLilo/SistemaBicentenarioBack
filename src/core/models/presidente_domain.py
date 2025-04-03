from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PresidenteBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    partido_politico: Optional[str] = Field(None, max_length=100)
    politicas_clave: Optional[str] = None

class PresidenteCreate(PresidenteBase):
    imagen: Optional[str] = Field(None, max_length=500)
    periodo_inicio: Optional[datetime] = None
    periodo_fin: Optional[datetime] = None
    biografia: Optional[str] = None

class PresidenteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    imagen: Optional[str] = Field(None, max_length=500)
    periodo_inicio: Optional[datetime] = None
    periodo_fin: Optional[datetime] = None
    biografia: Optional[str] = None
    partido_politico: Optional[str] = Field(None, max_length=100)
    politicas_clave: Optional[str] = None

class PresidenteInDB(PresidenteBase):
    id: int
    imagen: Optional[str] = Field(None, max_length=500)
    periodo_inicio: Optional[datetime] = None
    periodo_fin: Optional[datetime] = None
    biografia: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True