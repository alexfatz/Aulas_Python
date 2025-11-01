from models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session
from schemas import oauth2_scheme
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from main import algorithm, secret_key


def criar_sessao():
    try:
        Session = sessionmaker(db)
        session = Session()
        yield session
    finally:
        session.close()


def verificar_token(token: str = Depends(oauth2_scheme), sessao: Session = Depends(criar_sessao)):
    try:
        verif_token = jwt.decode(token, secret_key, algorithm)
        usuario_id = int(verif_token.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido.")
    
    usuario = sessao.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado.")

    return usuario