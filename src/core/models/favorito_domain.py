from pydantic import BaseModel
from .usuario_domain import UsuarioInDB  # Asumiendo que existe

class FavoritoBase(BaseModel):
    id_usuario: int
    id_referenciado: int

class FavoritoCreate(FavoritoBase):
    pass

class FavoritoUpdate(BaseModel):
    # Normalmente no se actualizan los favoritos, solo se crean/eliminan
    pass

class FavoritoInDB(FavoritoBase):
    id: int
    usuario: UsuarioInDB

    class Config:
        from_attributes = True