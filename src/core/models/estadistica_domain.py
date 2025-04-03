from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .usuario_domain import UsuarioInDB  # Asumiendo que existe

class EstadisticaTipo(str, Enum):
    Visita = "Visita"
    Consulta = "Consulta"
    Busqueda = "Busqueda"

class EstadisticaBase(BaseModel):
    tipo: EstadisticaTipo
    detalle: Optional[str] = None
    id_usuario: Optional[int] = None

class EstadisticaCreate(EstadisticaBase):
    pass

class EstadisticaUpdate(BaseModel):
    detalle: Optional[str] = None

class EstadisticaInDB(EstadisticaBase):
    id: int
    fecha: datetime
    usuario: Optional[UsuarioInDB] = None

    class Config:
        from_attributes = True