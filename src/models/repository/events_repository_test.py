import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_events():
    events = {
        "uuid": "meu_uuid_id",
        "title": "meu title",
        "slug": "meu slug",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(events)
    print(response)

def test_get_event_by_id():
    event_id = "meu_uuid_id"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)