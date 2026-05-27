install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload

migrate:
	alembic upgrade head

test:
	pytest -v

cov:
	pytest -v --cov=src

cov-html:
	pytest --cov=src --cov-report=html && start htmlcov/index.html

watch:
	ptw -- -v --cov=src

lint:
	ruff check .

format:
	ruff format .

fix:
	ruff check . --fix && ruff format .

docker-up:
	docker compose up -d

docker-down:
	docker compose down