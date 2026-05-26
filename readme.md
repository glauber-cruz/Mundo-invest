# Instalação com Docker (Recomendado)

Suba toda a aplicação com um único comando:

```bash
docker compose up -d
```

A aplicação ficará disponível em:

```txt
http://localhost:8000
```

Documentação Swagger:

```txt
http://localhost:8000/docs
```

---

# Instalação Local

Clone o repositório e acesse a pasta do projeto.

## 1. Crie o ambiente virtual

```bash
python -m venv venv
```

## 2. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Execute as migrations

```bash
alembic upgrade head
```

## 5. Inicie a aplicação

```bash
uvicorn main:app --reload
```

A aplicação ficará disponível em:

```txt
http://localhost:8000
```

Documentação Swagger:

```txt
http://localhost:8000/docs
```