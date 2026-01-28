from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import declarative_base, relationship


db = create_engine("sqlite:///banco.db")
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String)
    email: str = Column(String)
    senha: str = Column(String)
    admin: bool = Column(Boolean, default=False)

    def __init__(self, nome: str, email: str, senha: str, admin: bool =False):
        self.nome: str = nome
        self.email: str = email
        self.senha: str = senha
        self.admin: bool = admin


class Pedido(Base):
    __tablename__ = "pedidos"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id: int = Column(Integer, ForeignKey("usuarios.id"))
    status: str = Column(String, default="pendente")
    valor: float = Column(Float)
    itens = relationship("Item", cascade="all, delete") 


    def __init__(self, usuario_id: int, status: str = "pendente", valor: float = 0.0):
        self.usuario_id: int = usuario_id
        self.status: str = status
        self.valor: float = valor


    def calcular_valor(self):
        self.valor = sum(item.valor * item.quantidade for item in self.itens)


class Item(Base):
    __tablename__ = "itens"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id: int = Column(Integer, ForeignKey("pedidos.id"))
    sabor: str = Column(String)
    valor: float = Column(Float)
    quantidade: int = Column(Integer)


    def __init__(self, pedido_id: int, sabor: str, valor: float, quantidade: int):
        self.pedido_id: int = pedido_id
        self.sabor: str = sabor
        self.valor: float = valor
        self.quantidade: int = quantidade
