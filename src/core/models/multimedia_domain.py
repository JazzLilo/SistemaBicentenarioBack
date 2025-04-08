from typing import Optional
from pydantic import BaseModel
class MultimediaBase(BaseModel):
    url: str
    tipo: str
    id_evento_historico: Optional[int] = None
    id_cultura: Optional[int] = None

class MultimediaCreate(MultimediaBase):
    pass

class MultimediaUpdate(BaseModel):
    url: Optional[str] = None
    tipo: Optional[str] = None
    id_evento_historico: Optional[int] = None

class MultimediaInDB(MultimediaBase):
    id: int

    class Config:
        from_attributes = True

class MultimediaWithRelations(MultimediaInDB):
    evento_historico: Optional['EventoHistoricoInDB'] = None