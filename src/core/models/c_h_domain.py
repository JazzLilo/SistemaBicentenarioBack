from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.core.models.categoria_domain import CategoriaInDB

class CategoriaEventoHistoricoBase(BaseModel):
    id_evento: int
    id_categoria: int

class CategoriaEventoHistoricoCreate(CategoriaEventoHistoricoBase):
    pass

class CategoriaEventoHistoricoInDB(CategoriaEventoHistoricoBase):
    categoria: Optional[CategoriaInDB] = None
    evento: Optional[EventoHistoricoInDB] = None
    
    class Config:
        from_attributes = True