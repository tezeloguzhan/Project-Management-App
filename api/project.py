
from database.modelss.projects import Projects
from database.schemas.projects_schema import ProjectsSchema
from database.modelss.users import Users
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask import request
class Projects(Resource):
    
    def get(self):

        projects=Projects.objects
        schema=ProjectsSchema(many=True)
        result=schema.dump(projects)
        #print(result) 
        return result


class AddProject(Resource):    

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
