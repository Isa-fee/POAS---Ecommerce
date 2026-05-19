from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from database import engine, get_session
import models
import crud
from models import Usuario, Papel, Produto, Categoria, Pedido

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

#usuarios

@app.post("/usuarios")
def criar_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    return crud.criar_usuario(session, usuario)

@app.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):
    return crud.listar_usuarios(session)

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    return crud.buscar_usuario(session, usuario_id)

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados: dict, session: Session = Depends(get_session)):
    return crud.atualizar_usuario(session, usuario_id, dados)

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, session: Session = Depends(get_session)):
    return crud.deletar_usuario(session, usuario_id)

#papeis

@app.post("/papeis")
def criar_papel(papel: Papel, session: Session = Depends(get_session)):
    return crud.criar_papel(session, papel)

@app.get("/papeis")
def listar_papeis(session: Session = Depends(get_session)):
    return crud.listar_papeis(session)


#os dois

@app.post("/usuarios/{usuario_id}/papeis/{papel_id}")
def adicionar_papel_usuario(usuario_id: int, papel_id: int, session: Session = Depends(get_session)):
    return crud.adicionar_papel_usuario(session, usuario_id, papel_id)


#produtos

@app.post("/produtos")
def criar_produto(produto: Produto, session: Session = Depends(get_session)):
    return crud.criar_produto(session, produto)

@app.get("/produtos")
def listar_produtos(session: Session = Depends(get_session)):
    return crud.listar_produtos(session)

@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, dados: dict, session: Session = Depends(get_session)):
    return crud.atualizar_produto(session, produto_id, dados)

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, session: Session = Depends(get_session)):
    return crud.deletar_produto(session, produto_id)


#categorias

@app.post("/categorias")
def criar_categoria(categoria: Categoria, session: Session = Depends(get_session)):
    return crud.criar_categoria(session, categoria)

@app.get("/categorias")
def listar_categorias(session: Session = Depends(get_session)):
    return crud.listar_categorias(session)

@app.put("/categorias/{categoria_id}")
def atualizar_categoria(categoria_id: int, dados: dict, session: Session = Depends(get_session)):
    return crud.atualizar_categoria(session, categoria_id, dados)

@app.delete("/categorias/{categoria_id}")
def deletar_categoria(categoria_id: int, session: Session = Depends(get_session)):
    return crud.deletar_categoria(session, categoria_id)



#os dois

@app.post("/produtos/{produto_id}/categorias/{categoria_id}")
def adicionar_categoria_produto(produto_id: int, categoria_id: int, session: Session = Depends(get_session)):
    return crud.adicionar_categoria_produto(session, produto_id, categoria_id)


#pedidos

@app.post("/pedidos")
def criar_pedido(pedido: Pedido, session: Session = Depends(get_session)):
    return crud.criar_pedido(session, pedido)

@app.get("/pedidos")
def listar_pedidos(session: Session = Depends(get_session)):
    return crud.listar_pedidos(session)

@app.put("/pedidos/{pedido_id}")
def atualizar_pedido(pedido_id: int, dados: dict, session: Session = Depends(get_session)):
    return crud.atualizar_pedido(session, pedido_id, dados)

@app.delete("/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int, session: Session = Depends(get_session)):
    return crud.deletar_pedido(session, pedido_id)