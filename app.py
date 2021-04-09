from flask import Flask, jsonify,request,make_response
from flask_mongoengine import MongoEngine
from database.modelss.users import Users
#Özel Error
#from api.errors import unauthorized -- eklenecek
#Güvenlik
from constants import database_name,database_password
import datetime
#JWT İŞLEMLERİ
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from flask_restful import Resource
from flask_restful import Api
from api.routes import initialize_routes
from database.modelss.comments import Comments
from database.modelss.tasks import Task

app = Flask(__name__)
DB_URL="mongodb+srv://oguzhan:{}@cluster0.nupmm.mongodb.net/{}?retryWrites=true&w=majority".format(database_password,database_name)#constants.py dosyası açıp bilgilerinizi giriniz
app.config['MONGODB_HOST'] = DB_URL

db=MongoEngine()
db.init_app(app)

api = Api(app)
initialize_routes(api)

app.config["JWT_SECRET_KEY"] = "super-secret"  #Test için default değer , ürüne çıkıldığında özel key üretiniz. 
jwt = JWTManager(app)

""" ÖRNEK TASK VE USER OLUŞTURMA(SUPERUSER)
@app.route('/api/example_data',methods=["POST"])
def example_data():
   
    task1=Task(task_id=1,title="Konu 1",text="Açıklama 1")
    task1.save()
    new_user = Users(name="superuser",email="superuser@gmail.com", password="123456", access={"admin": True})
    new_user.save()
    return make_response('',201)
"""


if __name__ == "__main__":
    app.run(debug=True)