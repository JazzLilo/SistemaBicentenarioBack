from typing import Optional, List
from pydantic import BaseModel
from src.core.models.evento_historico_domain import EventoHistoricoInDB
class CategoriaBase(BaseModel):
    nombre_categoria: str
    descripcion: Optional[str] = None

class CategoriaInDB(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

class CategoriaWithRelations(CategoriaInDB):
    historias: List['HistoriaInDB'] = []
    eventos: List['EventoHistoricoInDB'] = []