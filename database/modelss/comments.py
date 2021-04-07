from database.modelss.imports import *
#Yorumlar
class Comments(EmbeddedDocument):
    content    = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)