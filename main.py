from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session
from database import engine, get_session
import models
import crud
from models import Usuario, Papel

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

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