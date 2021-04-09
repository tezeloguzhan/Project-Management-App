from flask import Flask
from marshmallow import Schema, fields


class UsersSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    password=fields.Str()
    access = fields.Bool()


    

