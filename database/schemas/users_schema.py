from database.modelss.users import Users
from flask_marshmallow import Marshmallow
from flask import Flask
from marshmallow import Schema, fields


class UsersSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    access = fields.Bool()
    

