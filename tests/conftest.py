import pytest
from fastapi.testclient import TestClient

from main import create_app
from src.infra.database.database import get_db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.pool import StaticPool
from src.infra.database.database import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={"check_same_thread": False},
  poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
  db = TestingSessionLocal()
  try:
    yield db
  finally:
    db.close()


@pytest.fixture
def client():
  app = create_app()

  app.dependency_overrides[get_db] = override_get_db

  return TestClient(app)