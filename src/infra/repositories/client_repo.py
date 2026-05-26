from sqlalchemy.orm import Session

from src.infra.models.client_model import ClientModel
from sqlalchemy import exists

class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, client: ClientModel) -> ClientModel:
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def email_already_exists(self, email: str) -> bool:
      return self.db.query(
        exists().where(
            ClientModel.cliente_email == email
        )
      ).scalar()

    def get_by_email(self, email: str) -> ClientModel | None:
      return self.db.query(ClientModel).filter(ClientModel.cliente_email == email).first()

    def update(self, client: ClientModel) -> ClientModel:
      client = self.db.merge(client)
      self.db.commit()
      self.db.refresh(client)
      return client