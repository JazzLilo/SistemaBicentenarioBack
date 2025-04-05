from typing import Optional, List
from pydantic import BaseModel
from src.core.models.historia_domain import HistoriaInDB
from src.core.models.cultura_domain import CulturaInDB
from src.core.models.evento_historico_domain import EventoHistoricoInDB
from src.core.models.evento_agendable_domain import EventoAgendableInDB

class UbicacionBase(BaseModel):
    nombre: str
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    imagen: Optional[str] = None
    descripcion: Optional[str] = None

class UbicacionCreate(UbicacionBase):
    pass

class UbicacionUpdate(BaseModel):
    nombre: Optional[str] = None
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    imagen: Optional[str] = None
    descripcion: Optional[str] = None

class UbicacionInDB(UbicacionBase):
    id: int

    class Config:
        from_attributes = True

class UbicacionWithRelations(UbicacionInDB):
    historias: list['HistoriaInDB'] = []
    culturas: list['CulturaInDB'] = []
    eventos_historicos: list['EventoHistoricoInDB'] = []
    eventos_agendables: list['EventoAgendableInDB'] = []