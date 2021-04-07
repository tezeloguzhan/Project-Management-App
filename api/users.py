from database.schemas.users_schema import UsersSchema
from flask_restful import Resource
from database.modelss.users import Users


#Kullanıcıları Görüntüleme    
class UsersApi(Resource):
    def get(self):
        users=Users.objects
        schema=UsersSchema(many=True)
        result=schema.dump(users)
        #print(result) 
        return result

class SignUpApi(Resource):
    pass 
class LoginApi(Resource):
    pass       