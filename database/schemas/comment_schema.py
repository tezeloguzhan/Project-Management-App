from marshmallow import Schema, fields
class CommentSchema(Schema):
    content = fields.String()
    created_at = fields.DateTime()