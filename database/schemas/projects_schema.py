from marshmallow import Schema, fields
from database.schemas.users_schema import UsersSchema
import datetime
class ProjectsSchema(Schema):
    project_id=fields.Int()
    name = fields.Str()
    status = fields.Str()
    created_at=fields.DateTime(str(datetime.datetime.utcnow))
    user=fields.Nested(UsersSchema(), dump_only=True)
    access=fields.Str()
    
