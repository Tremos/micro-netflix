from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()