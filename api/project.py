
from database.models import Projects,Users,Task
from database.schemas import ProjectsSchema
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask import request
from flask_restful import Resource
from api.errors import unaccess


class ProjectsApi(Resource):
    
    def get(self):

        projects=Projects.objects
        schema=ProjectsSchema(many=True)
        result=schema.dump(projects)
        #print(result) 
        return result

class ProjectApi(Resource):
    def get(self,project_id):
        each_project=Projects.objects(project_id=project_id).first()
        schema=ProjectsSchema(many=False)
        result=schema.dump(each_project)
        return result


class AddProjectApi(Resource):    

    @jwt_required()
    def post(self):
         user_id = get_jwt_identity()
         req_data = request.get_json() or None
         user = Users.objects.get(id=user_id)
         schema=ProjectsSchema()
         data=schema.dump(req_data)
         model = Projects(**data,user=user)
         model.save()
         return data

class DeleteProjectApi(Resource):
    @jwt_required()
    def delete(self,project_id):
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        if authorized:
            each_project=Projects.objects.get(project_id=project_id).delete()
            
        else:
            return unaccess()

class UpdateProjectApi(Resource):
    @jwt_required()

    def put(self,project_id):

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        
        if authorized:
        
            each_project=Projects.objects.get(project_id=project_id)
            req_data = request.get_json() or None
            update_project=Projects.objects.get(project_id=project_id).update(**req_data)
            return update_project
        else:
            return unaccess()