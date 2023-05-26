from db import db


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    movies = db.relationship("Movie", backref="genre")

    def __repr__(self):
        return f'<Genre "{self.name}">'
