from typing import Optional, List
from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombre_categoria: str
    descripcion: Optional[str] = None

class CategoriaInDB(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

class CategoriaWithRelations(CategoriaInDB):
    historias: List['HistoriaInDB'] = []
    eventos: List['CategoriaEventoHistoricoInDB'] = []