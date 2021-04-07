from api.users import UsersApi

def initialize_routes(api):
    api.add_resource(UsersApi, '/users')
 