from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIn
from sqlalchemy.exc import IntegrityError
from src.errors.error_types.http_conflict import HttpConflictError

class CheckInRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIn (
                        attendeeId = attendee_id
                    )
                )

                database.session.add(check_in)
                database.session.commit()

                return attendee_id
            except IntegrityError:
                raise HttpConflictError('Check In já cadastrado!')
            except Exception as ex:
                database.session.rollback()
                raise ex