from flask import Flask, request
from flask_restful import Resource, Api
from database.schemas.users_schema import UsersSchema
from database.schemas.tasks_schema import TasksSchema
from flask_restful import Resource
from database.modelss.tasks import Task,Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.errors import unaccess
def serialize_tasks(tasks):
    schema = TasksSchema()
    result = schema.dump(tasks)
    return result
#Task Görüntüleme    
class TasksApi(Resource):
    def get(self):
        tasks=Task.objects
        schema=TasksSchema(many=True)
        result=schema.dump(tasks)
        #print(result) 
        return result
    
   
class AddTaskApi(Resource):    

    @jwt_required()
    def post(self):
         user_id = get_jwt_identity()
         req_data = request.get_json() or None
         user = Users.objects.get(id=user_id)
         schema=TasksSchema()
         data=schema.dump(req_data)
         model = Task(**data,user=user)
         model.save()
         return data

class TaskApi(Resource):
    def get(self,task_id):
        each_task=Task.objects(task_id=task_id).first()
        schema=TasksSchema(many=False)
        result=schema.dump(each_task)
        return result

class DeleteTaskApi(Resource):
    @jwt_required()
    def delete(self,task_id):
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        if authorized:
            each_task=Task.objects.get(task_id=task_id).delete()
            
        else:
            return unaccess()
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




            

         
        
