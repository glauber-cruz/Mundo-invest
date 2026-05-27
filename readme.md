# Instalação com Docker (Recomendado)

Suba toda a aplicação com um único comando:

```bash
make docker-up
```

ou

```bash
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

# Instalação Local

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
make install
```

ou

```bash
pip install -r requirements.txt
```

## 4. Execute as migrations

```bash
make migrate
```

ou

```bash
alembic upgrade head
```

## 5. Inicie a aplicação

```bash
make run
```

ou

```bash
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

# Testes

## Executar testes

```bash
make test
```

## Executar testes com coverage

```bash
make cov
```

## Executar testes em watch mode

```bash
make watch
```

## Gerar relatório HTML de coverage

```bash
make cov-html
```

O relatório será gerado em:

```txt
htmlcov/index.html
```