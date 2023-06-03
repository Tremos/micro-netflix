from dao.models.base import BaseModel
from db import db
from dao.models.movie import Movie

class Genre(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    movies = db.relationship("Movie", backref="genre")

    def __repr__(self):
        return f'<Genre "{self.name}">'
