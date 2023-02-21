from flask import request
from flask_apispec import MethodResource, doc, marshal_with
from flask_restful import Resource

from app import logger
from database.models import Users
from helpers.docstings import HeaderDocString
from helpers.helpers import hash_text
from schemas.auth.login import LoginSuccessSchema, LoginFailSchema


@doc(
    tags=["Authentication"],
    description="Api to login",
    params=HeaderDocString.get_basic_doc(),
)
@marshal_with(LoginSuccessSchema, description="Success login", code=200)
@marshal_with(LoginFailSchema, description="Login error", code=401)
class LoginApi(MethodResource, Resource):
    def post(self):
        auth = request.authorization
        if not auth:
            return {"error": "Missing credentials"}, 401
        if auth.type != "basic":
            return {"error": "Wrong auth type (accept only basic)"}, 401
        user = Users.filter_by(username=auth.username)
        if not user:
            return {"error": "User not found"}, 401
        if user.password != hash_text(auth.password):
            return {"error": "Incorrect password"}, 401
        token = user.create_token()
        logger.info(f"Successfully logged to user {user.username}")
        return {"token_expire": user.token_expire, "token": token}
