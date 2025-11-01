from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import criar_sessao, verificar_token
from models import Pedido, Usuario
#from schemas import PedidoSchema


pedidos_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])


@pedidos_router.get("/")
async def pedidos():
    """Rota de pedidos principal. Autenticação necessária."""
    return {"mensagem": "Voce acessou a rota de pedidos", "autenticação": False}


@pedidos_router.post("/criar_pedido")
async def criar_pedido(usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de criação de pedido. Autenticação necessária."""
    # pedido_schema pendente
    novo_pedido = Pedido(usuario.id)
    sessao.add(novo_pedido)
    sessao.commit()
    return {"mensagem": f"Pedido {novo_pedido.id} criado com sucesso!"}


@pedidos_router.post("/cancelar_pedido/{pedido_id}")
async def cancelar_pedido(pedido_id: int, usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de cancelamento de pedido. Autenticação necessária."""
    pedido = sessao.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    if pedido.usuario_id != usuario.id and not usuario.admin:
        raise HTTPException(status_code=401, detail="Usuário não autorizado.")
    
    pedido.status = "cancelado"
    sessao.commit()
    return {
        "mensagem": f"Pedido {pedido.id} cancelado com sucesso!",
        "pedido": pedido
    }
