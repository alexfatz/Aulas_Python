from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import criar_sessao, verificar_token
from models import Pedido, Usuario, Item
from schemas import ItemPedidoSchema, ResponsePedidoSchema


pedidos_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])


@pedidos_router.get("/")
async def pedidos():
    """Rota de pedidos principal. Autenticação necessária."""
    return {"mensagem": "Você acessou a rota de pedidos"}


@pedidos_router.get("/listar")
async def listar_pedidos(quantidade: int = 10, usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de listagem de pedidos. Autenticação necessária."""
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Usuário não autorizado.")
    pedidos = sessao.query(Pedido).limit(quantidade).all()

    return {"pedidos": pedidos}


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


@pedidos_router.post("/adicionar_item/{pedido_id}")
async def adicionar_item_pedido(pedido_id: int, item_pedido_schema: ItemPedidoSchema, usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de adição de item ao pedido. Autenticação necessária."""
    pedido = sessao.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    if pedido.usuario_id != usuario.id and not usuario.admin:
        raise HTTPException(status_code=401, detail="Usuário não autorizado.")
    
    novo_item = Item(pedido_id, item_pedido_schema.sabor, item_pedido_schema.valor, item_pedido_schema.quantidade)
    sessao.add(novo_item)
    pedido.calcular_valor()
    sessao.commit()

    return {
        "mensagem": f"Item adicionado ao pedido com sucesso!",
        "valor": pedido.valor
    }


@pedidos_router.post("/remover_item/{item_id}")
async def remover_item_pedido(item_id: int, usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de remoção de item do pedido. Autenticação necessária."""
    item = sessao.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado.")
    
    pedido = sessao.query(Pedido).filter(Pedido.id == item.pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    if pedido.usuario_id != usuario.id and not usuario.admin:
        raise HTTPException(status_code=401, detail="Usuário não autorizado.")
    
    sessao.delete(item)
    pedido.calcular_valor()
    sessao.commit()

    return {
        "mensagem": f"Item removido do pedido com sucesso!",
        "valor": pedido.valor,
        "pedido": pedido.itens
    }


@pedidos_router.post("/finalizar_pedido/{pedido_id}")
async def finalizar_pedido(pedido_id: int, usuario: Usuario = Depends(verificar_token), sessao: Session = Depends(criar_sessao)):
    """Rota de finalização de pedido. Autenticação necessária."""
    pedido = sessao.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        return HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    if pedido.usuario_id != usuario.id and not usuario.admin:
        return HTTPException(status_code=401, detail="Usuário não autorizado.")

    return {
        "mensagem": f"Pedido {pedido_id} finalizado com sucesso!"
    }


@pedidos_router.get("/listar/pedido/{pedido_id}")
async def listar_pedido_unico(pedido_id: int, sessao: Session = Depends(criar_sessao), usuario: Usuario = Depends(verificar_token)):
    """Rota de visualização de pedido. Autenticação necessária."""
    pedido = sessao.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        return HTTPException(status_code=404, detail="Pedido não encontrado.")
    
    if pedido.usuario_id != usuario.id and not usuario.admin:
        return HTTPException(status_code=401, detail="Usuário não autorizado.")

    return {
        "quantidade de itens": len(pedido.itens),
        "pedido": pedido
    }


@pedidos_router.get("/listar/pedidos-usuario", response_model=list[ResponsePedidoSchema])
async def listar_pedidos_usuario(sessao: Session = Depends(criar_sessao), usuario: Usuario = Depends(verificar_token)):
    """Rota de visualização de pedidos de um usuário. Autenticação necessária."""
    pedidos = sessao.query(Pedido).filter(Pedido.usuario_id == usuario.id).all()

    return pedidos
