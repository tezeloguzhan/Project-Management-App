from flask import Flask, jsonify,request,make_response
from flask_mongoengine import MongoEngine
from constants import database_name,database_password
from flask_jwt_extended import JWTManager
from flask_restful import Resource,Api
from api.routes import initialize_routes
from celery import Celery
import os




"""
docker run -p 5000:5000 --rm testflaskapp
"""
app = Flask(__name__)
DB_URL="mongodb+srv://oguzhan:{}@cluster0.nupmm.mongodb.net/{}?retryWrites=true&w=majority".format(database_password,database_name)#constants.py dosyası açıp bilgilerinizi giriniz
app.config['MONGODB_HOST'] = DB_URL
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0' 
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'
db=MongoEngine()
db.init_app(app)

api = Api(app)
initialize_routes(api)

app.config["JWT_SECRET_KEY"] = "super-secret"  #Test için default değer , ürüne çıkıldığında özel key üretiniz. 
jwt = JWTManager(app)





if __name__ == "__main__":
    app.run(debug=True) #docker için host=0.0.0.0