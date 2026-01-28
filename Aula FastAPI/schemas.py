from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="autenticar/logar-form")


class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    admin: Optional[bool]

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True


class ItemPedidoSchema(BaseModel):
    sabor: str
    valor: float
    quantidade: int

    class Config:
        from_attributes = True


class ResponsePedidoSchema(BaseModel):
    id: int
    status: str
    valor: float
    itens: list[ItemPedidoSchema]

    class Config:
        from_attributes = True