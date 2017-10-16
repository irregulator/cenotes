from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    DEFAULT_MAX_VISITS = 1
    DEFAULT_VISITS_COUNT = 0

    id = db.Column(db.Integer, primary_key=True)
    max_visits = db.Column(db.Integer, default=DEFAULT_MAX_VISITS)
    visits_count = db.Column(db.Integer, default=DEFAULT_VISITS_COUNT)
    payload = db.Column(db.Binary, nullable=False)
    expiration_date = db.Column(db.Date)

    def __init__(self, payload, max_visits=DEFAULT_MAX_VISITS,
                 visits_count=DEFAULT_VISITS_COUNT, expiration_date=None):
        try:
            self.payload = payload.encode()
        except AttributeError:
            self.payload = payload
        self.expiration_date = expiration_date or date.today()
        self.max_visits = max_visits
        self.visits_count = visits_count

    @property
    def iso_expiration_date(self):
        return (self.expiration_date.isoformat()
                if self.expiration_date else None)


def create_new_note(cen_parameters, payload):
    new_note = Note(payload)
    new_note.expiration_date = cen_parameters.expiration_date
    new_note.visits_count = cen_parameters.visits_count
    new_note.max_visits = cen_parameters.max_visits
    db.session.add(new_note)
    db.session.commit()
    return new_note
