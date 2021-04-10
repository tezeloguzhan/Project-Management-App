from marshmallow import Schema, fields
import datetime



class UsersSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    password=fields.Str()
    access = fields.Bool()
    #tasks=fields.Nested(TasksSchema, dump_only=True)

    


class ProjectsSchema(Schema):
    project_id=fields.Int()
    name = fields.Str()
    status = fields.Str()
    created_at=fields.DateTime()
    user=fields.Nested(UsersSchema(exclude=("email","password","access")), dump_only=True)
    access=fields.Bool()
    
class CommentSchema(Schema):

    comment_id=fields.Int()
    content=fields.Str()
    created_at=fields.DateTime()
    user=fields.Nested(UsersSchema(), dump_only=True)

class TasksSchema(Schema):
    task_id=fields.Int()
    projects=fields.Nested(ProjectsSchema(exclude=("access","user","created_at","status")), dump_only=True)
    title = fields.Str()
    text = fields.Str()
    start_date=fields.DateTime()
    end_date=fields.DateTime()
    created_at=fields.DateTime()
    finished_at=fields.DateTime()
    user=fields.Nested(UsersSchema(exclude=("email","password","access")), dump_only=True)
    task_status=fields.Str()
    comments=fields.Nested(CommentSchema(exclude=("comment_id","created_at")), dump_only=True)
    
