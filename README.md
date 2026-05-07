# POAS---Ecommerce

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

---

## 2. Entrar na pasta do projeto

```bash
cd nome-do-projeto
```

---

# Criar ambiente virtual (venv)

## Windows

```bash
python -m venv venv
```

---

# Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

Após ativar, deverá aparecer algo parecido com:

```bash
(venv)
```

no terminal.

---

# Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Configurar banco de dados MySQL

Abrir o MySQL Workbench e executar:

```sql
CREATE DATABASE ecommerce;
```

---

# Configurar conexão com banco

No arquivo `database.py`, alterar:

```python
DATABASE_URL = "mysql+pymysql://root:SUA_SENHA@localhost/ecommerce"
```

Substituir:

```python
SUA_SENHA
```

pela senha do seu MySQL.

---

# Rodar o projeto

```bash
uvicorn main:app --reload
```

---

# Acessar a API

## Swagger UI

Abrir no navegador:

```text
http://127.0.0.1:8000/docs
```

---

# Estrutura do projeto

```text
projeto/
│
├── main.py
├── models.py
├── crud.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

---
