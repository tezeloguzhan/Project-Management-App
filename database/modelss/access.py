
from database.modelss.imports import *
#Kullancı Erişim Ayarları
class UserAccess(EmbeddedDocument):
    user    = BooleanField(default=True)
    admin   = BooleanField(default=False)
