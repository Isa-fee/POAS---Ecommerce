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

#produtos e categorias

class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = "produto_categorias"

    produto_id: Optional[int] = Field(
        default=None,
        foreign_key="produtos.id",
        primary_key=True
    )
    categoria_id: Optional[int] = Field(
        default=None,
        foreign_key="categorias.id",
        primary_key=True
    )


class Produto(SQLModel, table=True):
    __tablename__ = "produtos"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    preco: float
    criado_em: datetime = Field(default_factory=datetime.utcnow)

    categorias: List["Categoria"] = Relationship(
        back_populates="produtos",
        link_model=ProdutoCategoria)


class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str

    produtos: List[Produto] = Relationship(
        back_populates="categorias",
        link_model=ProdutoCategoria)


class Pedido(SQLModel, table=True):
    __tablename__ = "pedidos"

    id: Optional[int] = Field(default=None, primary_key=True)

    usuario_id: int = Field(foreign_key="usuarios.id")

    total: float
    status: str

    criado_em: datetime = Field(default_factory=datetime.utcnow)


class Pagamento(SQLModel, table=True):
    __tablename__ = "pagamentos"

    id: Optional[int] = Field(default=None, primary_key=True)

    pedido_id: int = Field(foreign_key="pedidos.id")

    valor: float
    metodo: str
    status: str

    pago_em: datetime = Field(default_factory=datetime.utcnow)


class Endereco(SQLModel, table=True):
    __tablename__ = "enderecos"

    id: Optional[int] = Field(default=None, primary_key=True)

    usuario_id: int = Field(foreign_key="usuarios.id")

    rua: str
    cidade: str
    estado: str
    cep: str

class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacoes"

    id: Optional[int] = Field(default=None, primary_key=True)

    usuario_id: int = Field(foreign_key="usuarios.id")
    produto_id: int = Field(foreign_key="produtos.id")

    nota: int
    comentario: str

    criado_em: datetime = Field(default_factory=datetime.utcnow)


class Estoque(SQLModel, table=True):
    __tablename__ = "estoque"

    id: Optional[int] = Field(default=None, primary_key=True)

    produto_id: int = Field(
        foreign_key="produtos.id",
        unique=True
    )

    quantidade: int

    atualizado_em: datetime = Field(default_factory=datetime.utcnow)

#tabela para os pedisos e itens

class ItemPedido(SQLModel, table=True):
    __tablename__ = "itens_pedido"

    id: Optional[int] = Field(default=None, primary_key=True)

    pedido_id: int = Field(
        foreign_key="pedidos.id"
    )

    produto_id: int = Field(
        foreign_key="produtos.id"
    )

    quantidade: int
    preco: float