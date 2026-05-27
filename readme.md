# Rodando a aplicação

## Com Docker (Recomendado)

Suba toda a aplicação com um único comando:

```bash
make docker-up
# ou
docker compose up -d
```

A API estará disponível em:

```txt
http://localhost:8000
```

Documentação Swagger:

```txt
http://localhost:8000/docs
```

---

## Local

### 1. Crie o ambiente virtual

```bash
python -m venv venv
```

### 2. Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
make install
# ou
pip install -r requirements.txt
```

### 4. Crie o .env

Use o .example.env como base. o ENV=dev para ele ler o arquivo ".env"

### 5. Execute as migrations

```bash
make migrate
# ou
alembic upgrade head
```

### 6. Inicie a aplicação

```bash
make run
# ou
uvicorn main:app --reload
```

A API estará disponível em:

```txt
http://localhost:8000
```

Documentação Swagger:

```txt
http://localhost:8000/docs
```

---

# Rodando testes

## Executar testes

```bash
make test
# ou
pytest -v
```

## Executar testes com coverage

```bash
make cov
# ou
pytest -v --cov=src
```

## Executar testes em watch mode

```bash
make watch
# ou
ptw -- -v --cov=src
```

## Gerar relatório HTML de coverage

```bash
make cov-html
# ou
pytest --cov=src --cov-report=html
```

O relatório será gerado em:

```txt
htmlcov/index.html
```

# Lint

Para rodar lint basta executar

```bash
make lint
#ou
ruff check .
```

# Exemplos de endpoints

## 1. Criar cliente

```bash
curl -X POST "http://localhost:8000/clients/" \
  -H "Content-Type: application/json" \
  -d '{
    "cliente_nome": "Joao da Silva",
    "cliente_email": "joao.silva@gmail.com",
    "tipo_solicitacao": "Solicitacao de credito",
    "valor_patrimonio": 100000.00
  }'
```

### 2. Webhook de atualizacao de card (Pipefy)

```bash
curl -X POST "http://localhost:8000/webhooks/pipefy/card-updated" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": "evt_123",
    "card_id": "card_123",
    "cliente_email": "joao.silva@gmail.com",
    "timestamp": "2021-01-01T00:00:00Z"
  }'
```
