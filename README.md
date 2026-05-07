# POAS---Ecommerce

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Isa-fee/POAS---Ecommerce.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd POAS---Ecommerce
```

---

# Criar ambiente virtual (venv)

## Windows

```bash
python -m venv env
```

---

# Ativar ambiente virtual

## Windows

```bash
.\env\Scripts\activate
```

Após ativar, deverá aparecer algo parecido com:

```bash
(env)
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
