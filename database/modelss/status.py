from database.modelss.imports import *
#Proje Durum Bilgisi
class ProjectStatus(EmbeddedDocument):
    active      = BooleanField(default=True)
    archieved   = BooleanField(default=False)

#Task Durum Bilgisi
class TaskStatus(EmbeddedDocument):
    receipt = BooleanField(default=True)
    start   = BooleanField(default=False)
    control = BooleanField(default=False)
    finish  = BooleanField(default=False)