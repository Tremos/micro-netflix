from sqlalchemy.orm import declared_attr

from db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
