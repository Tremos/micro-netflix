from db import db


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    movies = db.relationship("Movie", backref="director")

    def __repr__(self):
        return f'<Director "{self.name}">'
