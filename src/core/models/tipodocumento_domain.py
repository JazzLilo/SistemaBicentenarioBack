from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TipoDocumentoBase(BaseModel):
    tipo: str

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumentoUpdate(BaseModel):
    tipo: Optional[str] = None

class TipoDocumentoInDB(TipoDocumentoBase):
    id_tipo: int

    class Config:
        from_attributes = True