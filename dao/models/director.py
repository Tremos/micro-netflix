from dao.models.base import BaseModel
from .movie import Movie
from db import db


class Director(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    movies = db.relationship("Movie", backref="director")

    def __repr__(self):
        return f'<Director "{self.name}">'
