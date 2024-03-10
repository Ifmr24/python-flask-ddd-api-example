""" User Entity """
from marshmallow import Schema, fields


class IUser:
    """ User Interface """

    def __init__(self, _id, username, email, password, created_at, updated_at):
        self._id = _id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at


class UserSchema(Schema):
    """ User validation schema """
    _id = fields.Str()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()
