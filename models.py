from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


#tabela que liga usuários e papeis
class UsuarioPapel(SQLModel, table=True):
    __tablename__ = "usuario_papeis"

    usuario_id: Optional[int] = Field(
        default=None,
        foreign_key="usuarios.id",
        primary_key=True
    )
    papel_id: Optional[int] = Field(
        default=None,
        foreign_key="papeis.id",
        primary_key=True
    )


class Papel(SQLModel, table=True):
    __tablename__ = "papeis"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(unique=True, index=True)

    usuarios: List["Usuario"] = Relationship(
        back_populates="papeis",
        link_model=UsuarioPapel
    )


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True, index=True)
    senha_hash: str
    criado_em: datetime = Field(default_factory=datetime.utcnow)

    papeis: List[Papel] = Relationship(
        back_populates="usuarios",
        link_model=UsuarioPapel
    )

class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True, index=True)
    senha_hash: str
    criado_em: datetime = Field(default_factory=datetime.utcnow)

    papeis: List[Papel] = Relationship(
        back_populates="usuarios",
        link_model=UsuarioPapel
    )