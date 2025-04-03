from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RolBase(BaseModel):
    nombre_rol: str
    descripcion: Optional[str] = None

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombre_rol: Optional[str] = None
    descripcion: Optional[str] = None

class RolInDB(RolBase):
    id: int

    class Config:
        from_attributes = True

class RolWithUsers(RolInDB):
    usuarios: List['UsuarioRolInDB']