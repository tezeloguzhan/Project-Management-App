from database.schemas import UsersSchema
from flask_restful import Resource
from database.models import Users
from flask_jwt_extended import create_access_token, create_refresh_token,get_jwt_identity,jwt_required,JWTManager
from flask import Flask,request,jsonify
from api.errors import unauthorized
import datetime

""" Admin Girişi
"email":"adminuser@gmail.com",
"password":"123456"
"""

#Kullanıcıları Görüntüleme    
class UsersApi(Resource):
    def get(self):
        users=Users.objects
        schema=UsersSchema(many=True)
        result=schema.dump(users)
        #print(result) 
        return result

#Kullanıcı Kayıt 
class SignUpApi(Resource):
    def post(self,*args, **kwargs):
        req_data = request.get_json() or None
        schema=UsersSchema()
        data=schema.dump(req_data)
        model = Users(**data)
        model.save()
        
class LoginApi(Resource):
    def post(self):
        req_data = request.get_json() or None
        user = Users.objects.get(email=req_data.get('email'))
        auth_success = user.check_pw_hash(req_data.get('password'))
        if not auth_success:
            return unauthorized()
        else:
                expiry = datetime.timedelta(days=5)
                access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
                refresh_token = create_refresh_token(identity=str(user.id))
                return jsonify({'result': {'access_token': access_token,
                                        'refresh_token': refresh_token,
                                        'logged_in_as': f"{user.email}"}})

#Login Bilgisi
    #"email":"testuser1@gmail.com",
    #"password":"123456"


