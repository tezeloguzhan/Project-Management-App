# Kullanılacak field
from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         StringField,
                         EmailField,
                         BooleanField,
                         IntField,
                         DateTimeField,
                         ReferenceField,
                         ListField)
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash


#Kullancı Erişim Ayarları
class UserAccess(EmbeddedDocument):
    user    = BooleanField(default=True)
    admin   = BooleanField(default=False)

#Proje Durum Bilgisi

class ProjectStatus(EmbeddedDocument):
    active      = BooleanField(default=True)
    archieved   = BooleanField(default=False)


class Users(Document):
    name     = StringField(unique=False)
    email    = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    access   = EmbeddedDocumentField(UserAccess, default=UserAccess(user=False, admin=True))
    tasks = ListField(ReferenceField('Task')) # one-many relationship
    
    #Şifre Hash
    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)
    check_pw_hash.__doc__ = check_password_hash.__doc__

    #Kaydetmeden önce hashle
    def save(self, *args, **kwargs):
        if self._created:
            self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)


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

#Yorumlar
class Comments(Document):
    comment_id =IntField(primary_key=True)
    content    = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    user=ReferenceField(Users)
    

Status = ('receipt', 'start', 'control', 'finish')
#Projelerin İş Kayıtları 
class Task(Document):
    task_id         = IntField(primary_key=True)
    projects        = ReferenceField(Projects)
    title           = StringField(max_length=60)
    text            = StringField(max_length=150)
    start_date      = DateTimeField(default=datetime.datetime.utcnow)
    end_date        = DateTimeField(default=datetime.datetime.utcnow)
    created_at      = DateTimeField(default=datetime.datetime.utcnow)
    finished_at     = DateTimeField(default=datetime.datetime.utcnow)
    user            = ReferenceField(Users)
    task_status     = StringField(choices=Status)
    comments        = ReferenceField(Comments)
    
    


    def to_json(self):
        return{
            "task_id":self.task_id,
            "projects":self.projects,
            "title":self.title,
            "text":self.text,
            "is_done":self.is_done,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "created_at":self.created_at,
            "finished_at":self.finished_at,
            "user":self.user,
            "task_status":self.task_status,
            "comments": self.comments
}



