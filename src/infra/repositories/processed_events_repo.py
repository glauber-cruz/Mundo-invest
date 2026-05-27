from sqlalchemy.orm import Session

from src.infra.models.processed_events_model import ProcessedEventModel
from sqlalchemy import exists


class ProcessedEventsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, processed_event: ProcessedEventModel) -> ProcessedEventModel:
        self.db.add(processed_event)
        self.db.commit()
        self.db.refresh(processed_event)
        return processed_event

    def event_already_processed(self, event_id: str) -> bool:
        return self.db.query(
            exists().where(ProcessedEventModel.event_id == event_id)
        ).scalar()
