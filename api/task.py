from flask import Flask, request
from database.schemas import UsersSchema,TasksSchema,CommentSchema,ProjectsSchema
from flask_restful import Resource
from database.models import Task,Users,Comments,Projects
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.errors import unaccess

#Task Görüntüleme    
class TasksApi(Resource):
    def get(self):
        tasks=Task.objects
        schema=TasksSchema(many=True)
        result=schema.dump(tasks)
        #print(result) 
        return result

#ID numarasına göre görüntüleme
class TaskApi(Resource):
    def get(self,task_id):
        each_task=Task.objects(task_id=task_id).first()
        schema=TasksSchema(many=False)
        result=schema.dump(each_task)
        return result
    
#Task Ekleme
class AddTaskApi(Resource):    

    @jwt_required()
    def post(self):
         user_id = get_jwt_identity()
         projects=Projects.objects.first()
         comments=Comments.objects.first()
         req_data = request.get_json() or None
         user = Users.objects.get(id=user_id)
         schema=TasksSchema()
         data=schema.dump(req_data)
         model = Task(**data,user=user,projects=projects,comments=comments)
         model.save()
         return data

#Task Silme
class DeleteTaskApi(Resource):
    @jwt_required()
    def delete(self,task_id):
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        if authorized:
            each_task=Task.objects.get(task_id=task_id).delete()
            
        else:
            return unaccess()

#Task Güncelleme
class UpdateTaskApi(Resource):
    @jwt_required()

    def put(self,task_id):

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        
        if authorized:
        
            each_task=Task.objects.get(task_id=task_id)
            req_data = request.get_json() or None
            update_task=Task.objects.get(task_id=task_id).update(**req_data)
            return update_task
        else:
            return unaccess()

class CommentApi(Resource):
    @jwt_required()
    def post(self):
         user_id = get_jwt_identity()
         comments=Comments.objects
         req_data = request.get_json() or None
         user = Users.objects.get(id=user_id)
         schema=CommentSchema()
         data=schema.dump(req_data)
         model = Comments(**data,user=user)
         model.save()
         return data




        
