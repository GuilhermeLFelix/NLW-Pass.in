import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_attendee():
    event_id = "meu_uuid_id"
    attendeeInfo = {
        "uuid": "meu_uuid_id_attendee",
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendeeInfo)
    print(response)

def test_get_attendee_by_id():
    attendee_id = "meu_uuid_id_attendee"
    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_by_id(attendee_id)

    print(response)