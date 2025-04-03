from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.core.models.rol_domain import RolInDB
from src.core.models.usuario_domain import UsuarioInDB

class UsuarioRolBase(BaseModel):
    id_usuario: int
    id_rol: int

class UsuarioRolCreate(UsuarioRolBase):
    pass

class UsuarioRolUpdate(BaseModel):
    id_rol: Optional[int] = None

class UsuarioRolInDB(UsuarioRolBase):
    rol: Optional[RolInDB] = None
    usuario: Optional[UsuarioInDB] = None

    class Config:
        from_attributes = True