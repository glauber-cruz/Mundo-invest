from sqlalchemy.orm import Session

from src.infra.repositories.client_repo import ClientRepository
from src.infra.repositories.processed_events_repo import ProcessedEventsRepository


class UnitOfWork:
    def __init__(self, db: Session):
        self.session = db
        self.clients = ClientRepository(db)
        self.processed_events = ProcessedEventsRepository(db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.session.rollback()
        else:
            self.session.commit()
