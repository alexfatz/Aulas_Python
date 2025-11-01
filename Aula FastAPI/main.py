# inicializar: uvicorn main:aplicativo --reload

from fastapi import FastAPI
from dotenv import load_dotenv
from passlib.context import CryptContext
from os import getenv

load_dotenv()

secret_key = getenv("SECRET_KEY")
algorithm = getenv("ALGORITHM")
expire_minutes = float(getenv("EXPIRE_MINUTES"))
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

aplicativo = FastAPI()

from auth_rota import auth_router
from pedidos_rota import pedidos_router

aplicativo.include_router(auth_router)
aplicativo.include_router(pedidos_router)
