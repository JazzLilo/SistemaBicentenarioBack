from typing import List, Optional
from pydantic import BaseModel

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

class TipoDocumentoWithRelations(TipoDocumentoInDB):
    bibliotecas: List['BibliotecaInDB'] = []