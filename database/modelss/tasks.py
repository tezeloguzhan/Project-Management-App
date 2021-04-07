from database.modelss.imports import *
from database.modelss.users import Users
from database.modelss.projects import Projects
from database.modelss.comments import Comments
from database.modelss.status import *

#Projelerin İş Kayıtları 
class Task(Document):
    task_id         = IntField(primary_key=True)
    title           = StringField(max_length=60)
    text            = StringField(max_length=150)
    start_date      = DateTimeField()
    end_date        = DateTimeField()
    created_at      = DateTimeField(default=datetime.datetime.utcnow)
    finished_at     = DateTimeField()
    user            = ReferenceField(Users)
    project         = ReferenceField(Projects)
    comments        = ListField(EmbeddedDocumentField(Comments))
    task_status     = EmbeddedDocumentField(TaskStatus, default=TaskStatus(receipt=True, start=False,control=False,finish=False))


    def to_json(self):
        return{
            "task_id":self.task_id,
            "title":self.title,
            "text":self.text,
            "is_done":self.is_done,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "created_at":self.created_at,
            "finished_at":self.finished_at,
            "user":self.user,
            "comments":self.comments,
            "task_status":self.task_status

        }