from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from src.core.models.usuario_domain import UsuarioInDB  # Asumiendo que existe
from src.core.models.ubicacion_domain import UbicacionInDB  # Asumiendo que existe

class EventoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha_hora: datetime
    id_organizador: int
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None

class EventoCreate(EventoBase):
    pass

class EventoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_hora: Optional[datetime] = None
    imagen: Optional[str] = None
    id_ubicacion: Optional[int] = None

class ParticipanteEventoInDB(BaseModel):
    id_usuario: int
    id_evento: int
    estado_asistencia: bool
    usuario: Optional[UsuarioInDB] = None

    class Config:
        from_attributes = True

class ComentarioEventoInDB(BaseModel):
    id: int
    contenido: str
    fecha: datetime
    usuario: UsuarioInDB

    class Config:
        from_attributes = True

class EventoInDB(EventoBase):
    id: int
    ubicacion: Optional[UbicacionInDB] = None
    organizador: UsuarioInDB
    participantes: List[ParticipanteEventoInDB] = []
    comentarios: List[ComentarioEventoInDB] = []

    class Config:
        from_attributes = True