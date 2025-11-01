from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db")
Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    status = Column(String, default="pendente")
    #itens = 


    def __init__(self, usuario_id, status="pendente"):
        self.usuario_id = usuario_id
        self.status = status


class Item(Base):
    __tablename__ = "itens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido = Column(Integer, ForeignKey("pedidos.id"))
    sabor = Column(String)
    valor = Column(Float)
    quantidade = Column(Integer)


    def __init__(self, pedido, sabor, valor, quantidade):
        self.pedido = pedido
        self.sabor = sabor
        self.valor = valor
        self.quantidade = quantidade
