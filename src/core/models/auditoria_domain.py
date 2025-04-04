from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from src.core.models.usuario_domain import UsuarioInDB 

class AuditoriaBase(BaseModel):
    tipo: str
    detalle: Optional[str] = None
    id_usuario: Optional[int] = None

class AuditoriaCreate(AuditoriaBase):
    pass 

class AuditoriaUpdate(BaseModel):
    tipo: Optional[str] = None
    detalle: Optional[str] = None
    id_usuario: Optional[int] = None

class AuditoriaInDB(AuditoriaBase):
    id: int
    fecha: datetime
    usuario: Optional[UsuarioInDB] = None 

    class Config:
        from_attributes = True  