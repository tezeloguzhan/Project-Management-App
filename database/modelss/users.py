from database.modelss.access import UserAccess
from database.modelss.imports import *
from flask_bcrypt import generate_password_hash, check_password_hash
class Users(Document):
    name     = StringField(unique=False)
    email    = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access   = EmbeddedDocumentField(UserAccess, default=UserAccess(user=True, admin=False))

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