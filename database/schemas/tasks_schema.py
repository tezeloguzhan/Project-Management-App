from flask import Flask
from marshmallow import Schema, fields
from database.schemas.users_schema import UsersSchema
from database.schemas.comment_schema import CommentSchema
import datetime


class TasksSchema(Schema):
    task_id=fields.Int()
    title = fields.Str()
    text = fields.Str()
    start_date=fields.DateTime()
    end_date=fields.DateTime()
    created_at=fields.DateTime(str(datetime.datetime.utcnow))
    finished_at=fields.DateTime()
    user=fields.Nested(UsersSchema(), dump_only=True)
    #project=fields.Nested(ProjectSchema(exclude=("email", "access")), dump_only=True)
    comments = fields.Nested(CommentSchema())
    task_status=fields.Str()
    
