from api_resources import LoginApi, StatusApi
from api_resources.auth.logout import LogoutApi
from app import api, docs


api.add_resource(LoginApi, "/login")
docs.register(LoginApi)

api.add_resource(StatusApi, "/login/status")
docs.register(StatusApi)

api.add_resource(LogoutApi, "/logout")
docs.register(LogoutApi)
