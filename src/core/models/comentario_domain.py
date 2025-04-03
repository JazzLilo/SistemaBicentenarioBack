from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from src.core.models.usuario_domain import UsuarioInDB  # Asumiendo que existe
from src.core.models.biblioteca_domain import BibliotecaInDB  # Definido anteriormente
from src.core.models.evento_domain import EventoInDB  # Asumiendo que existe

class ComentarioBase(BaseModel):
    contenido: str
    id_usuario: int

class ComentarioCreate(ComentarioBase):
    id_biblioteca: Optional[int] = None
    id_evento: Optional[int] = None

class ComentarioUpdate(BaseModel):
    contenido: Optional[str] = None

class ComentarioInDB(ComentarioBase):
    id: int
    fecha: datetime
    id_biblioteca: Optional[int] = None
    id_evento: Optional[int] = None
    usuario: UsuarioInDB
    biblioteca: Optional[BibliotecaInDB] = None
    evento: Optional[EventoInDB] = None

    class Config:
        from_attributes = True