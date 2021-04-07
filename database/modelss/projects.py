from database.modelss.status import *
from database.modelss.access import *
from database.modelss.users import Users
from database.modelss.imports import *


#Projeler
class Projects(Document):
    project_id = IntField(primary_key=True)
    name       = StringField(max_length=60)
    status     = EmbeddedDocumentField(ProjectStatus, default=ProjectStatus(active=True, archieved=False))
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    user       = ReferenceField(Users)
    access     = EmbeddedDocumentField(UserAccess, default=UserAccess(user=True, admin=False))
    

    def to_json(self):
        return{
            "project_id":self.project_id,
            "name":self.name,
            "status":self.status,
            "created_at":self.created_at,
            "finished_at":self.finished_at,
            "user":self.user,
            "access":self.access
        }