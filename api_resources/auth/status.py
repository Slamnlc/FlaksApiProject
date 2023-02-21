from flask import request
from flask_apispec import MethodResource, marshal_with, doc
from flask_restful import Resource

from database.models import Users
from helpers.docstings import HeaderDocString
from schemas.auth.status import LoginStatusSuccessSchema


@doc(
    tags=["Authentication"],
    description="Api to receive user auth status",
    params=HeaderDocString.get_token_doc("Provide bearer token", False),
)
@marshal_with(
    LoginStatusSuccessSchema, description="Get user auth status", code=200
)
class StatusApi(MethodResource, Resource):
    def get(self):
        auth = request.headers.get("Authorization")
        if not auth or "bearer " not in auth.lower():
            return {"status": "User not logged"}, 200
        user = Users.filter_by(access_token=auth.split(" ")[-1])
        if not user:
            return {"status": "User not logged"}, 200
        return user.to_dict(), 200
