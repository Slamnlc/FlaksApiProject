from flask_apispec import MethodResource, marshal_with, doc
from flask_restful import Resource

from database.models import Users
from helpers.decorators import is_login
from helpers.docstings import HeaderDocString
from helpers.helpers import get_current_token
from schemas.auth.logout import LogoutSuccessSchema
from schemas.missing_auth_header import MissAuthHeaderSchema


@doc(
    tags=["Authentication"],
    description="API to logout",
    params=HeaderDocString.get_token_doc("Provide bearer token", True),
)
@marshal_with(LogoutSuccessSchema, code=200)
@marshal_with(MissAuthHeaderSchema, code=401)
class LogoutApi(MethodResource, Resource):
    @is_login
    def post(self):
        user = Users.filter_by(access_token=get_current_token())
        user.clear_token()
        message = f"User {user.username} is successfully logged out"
        return {"message": message}, 201
