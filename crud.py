from sqlmodel import Session, select
from models import Usuario

def criar_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def listar_usuarios(session: Session):
    return session.exec(select(Usuario)).all()

def buscar_usuario(session: Session, usuario_id: int):
    return session.get(Usuario, usuario_id)

def atualizar_usuario(session: Session, usuario_id: int, dados: dict):
    usuario = session.get(Usuario, usuario_id)

    if not usuario:
        return None

    for chave, valor in dados.items():
        setattr(usuario, chave, valor)

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario

def deletar_usuario(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)

    if not usuario:
        return False

    session.delete(usuario)
    session.commit()

    return True

###########################################################

from models import Papel

def criar_papel(session: Session, papel: Papel):
    session.add(papel)
    session.commit()
    session.refresh(papel)
    return papel


def listar_papeis(session: Session):
    return session.exec(select(Papel)).all()

#tentando fazer a ligação dos dois#

def adicionar_papel_usuario(session: Session, usuario_id: int, papel_id: int):
    usuario = session.get(Usuario, usuario_id)
    papel = session.get(Papel, papel_id)

    if not usuario or not papel:
        return None

    usuario.papeis.append(papel)

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario