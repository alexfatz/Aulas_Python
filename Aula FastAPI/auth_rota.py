from fastapi import APIRouter, HTTPException, Depends
from dependencies import criar_sessao, verificar_token
from models import Usuario
from main import bcrypt_context, algorithm, secret_key, expire_minutes
from schemas import UsuarioSchema, LoginSchema, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timezone, timedelta


auth_router = APIRouter(prefix="/autenticar", tags=["autenticação"])


def gerar_token(usuario_id: int, expire_time = timedelta(minutes=expire_minutes)):
    expire = datetime.now(timezone(timedelta(hours=-3))) + expire_time
    infos = {"sub": str(usuario_id), "exp": expire}
    return jwt.encode(infos, secret_key, algorithm)


def autenticar_usuario(email: str, senha: str, sessao: Session):
    usuario = sessao.query(Usuario).filter(Usuario.email == email).first()

    if not usuario or not bcrypt_context.verify(senha, usuario.senha):
        return None

    return usuario



@auth_router.get("/")
async def home():
    """Rota de autenticação principal"""
    return {"mensagem": "Você accessou a rota de autenticação"}


@auth_router.post("/criar_conta")
async def criar_conta(usuario: UsuarioSchema, sessao: Session = Depends(criar_sessao)):
    """Rota de criação de conta. Autenticação necessária."""
    registro = sessao.query(Usuario).filter(Usuario.email == usuario.email).first()

    if registro:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    
    senha_bcrypt = bcrypt_context.hash(usuario.senha)
    novo_usuario = Usuario(usuario.nome, usuario.email, senha_bcrypt, usuario.admin)

    sessao.add(novo_usuario)
    sessao.commit()

    return {"mensagem": f"Conta {novo_usuario.nome} criada com sucesso!"}



@auth_router.post("/logar")
async def logar(login: LoginSchema, sessao: Session = Depends(criar_sessao)):
    """Rota de logar. Autenticação necessária."""
    registro = autenticar_usuario(login.email, login.senha, sessao)

    if not registro:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos.")

    return {
        "access_token": gerar_token(registro.id),
        "refresh_token": gerar_token(registro.id, timedelta(days=7)),
        "token_type": "Bearer"
    }


@auth_router.post("/logar-form")
async def logar_form(login: OAuth2PasswordRequestForm = Depends(), sessao: Session = Depends(criar_sessao)):
    """Rota de logar. Autenticação necessária."""
    registro = autenticar_usuario(login.username, login.password, sessao)

    if not registro:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos.")

    return {
        "access_token": gerar_token(registro.id),
        "token_type": "Bearer"
    }


@auth_router.get("/refresh")
async def refresh_token(usuario: Usuario = Depends(verificar_token)):
    access_token = gerar_token(usuario.id)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
