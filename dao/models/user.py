from dao.models.base import BaseModel
from db import db


class User (BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pw_hash = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)

    def __repr__(self):
        return f'<User "{self.email}", "{self.name} {self.surname}">'

