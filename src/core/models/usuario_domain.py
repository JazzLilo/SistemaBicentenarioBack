from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator


class UsuarioBase(BaseModel):
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    correo: str
    genero: str
    telefono: str
    pais: str
    ciudad: str
    imagen: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    contrasena: str

    @validator('contrasena')
    def validar_contrasena(cls, v):
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        return v

class UsuarioLogin(BaseModel):
    correo: str
    contrasena: str
    
class UsuarioCodeValidation(BaseModel):
    correo: str
    codeValidacion: str

class UsuarioResetPassword(BaseModel):
    correo: str
    contrasena: str
    codeValidacion: str

class UsuarioRole(BaseModel):
    id: int
    roles: list[str]
    

    

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidoPaterno: Optional[str] = None
    apellidoMaterno: Optional[str] = None
    genero: Optional[str] = None
    telefono: Optional[str] = None
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    imagen: Optional[str] = None

class UsuarioInDB(UsuarioBase):
    id: int
    estado: bool
    email_verified_at: Optional[datetime] = None
    ultimoIntentoFallido: Optional[datetime] = None
    cantIntentos: Optional[int] = None
    
class UsuarioResponse(UsuarioInDB):
    roles: list[str]

class UsuarioCreateResponse(UsuarioInDB):
    verification_token: str     

    class Config:
        from_attributes = True
        