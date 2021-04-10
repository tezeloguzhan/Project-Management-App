from api.users import UsersApi
from api.task import TasksApi,TaskApi,DeleteTaskApi,UpdateTaskApi,AddTaskApi,CommentApi
from api.project import ProjectsApi,AddProjectApi,DeleteProjectApi,UpdateProjectApi
from api.users import SignUpApi,LoginApi

def initialize_routes(api):

    #KULLANICI İŞLEMLERİ
    api.add_resource(UsersApi, '/users')#GET
    api.add_resource(SignUpApi,"/signup")#POST
    api.add_resource(LoginApi,"/login")#POST

    #İş Kayıt İşlemlerİ

    api.add_resource(TasksApi, '/tasks')#GET
    api.add_resource(AddTaskApi, '/addtask')#POST
    api.add_resource(CommentApi, '/comment')#POST
    api.add_resource(TaskApi, '/tasks/<task_id>')#GET
    api.add_resource(DeleteTaskApi, '/delete/tasks/<task_id>')#DELETE
    api.add_resource(UpdateTaskApi,'/update/tasks/<task_id>')#UPDATE
    
    
    #Proje İşlemleri

    api.add_resource(ProjectsApi, '/projects')#GET
    api.add_resource(AddProjectApi, '/addprojects')#GET
    api.add_resource(DeleteProjectApi, '/delete/project/<project_id>')#DELETE
    api.add_resource(UpdateProjectApi, '/update/project/<project_id>')#UPDATE