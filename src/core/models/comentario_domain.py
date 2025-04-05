from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ComentarioBase(BaseModel):
    contenido: str
    id_usuario: int
    id_biblioteca: Optional[int] = None
    id_evento_agendable: Optional[int] = None
    id_evento_historico: Optional[int] = None

class ComentarioCreate(ComentarioBase):
    pass

class ComentarioUpdate(BaseModel):
    contenido: Optional[str] = None

class ComentarioInDB(ComentarioBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True

class ComentarioWithRelations(ComentarioInDB):
    usuario: 'UsuarioInDB'
    biblioteca: Optional['BibliotecaInDB'] = None
    evento_agendable: Optional['EventoAgendableInDB'] = None
    evento_historico: Optional['EventoHistoricoInDB'] = None