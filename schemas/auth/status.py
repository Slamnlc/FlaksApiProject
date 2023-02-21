from marshmallow import Schema
from marshmallow.fields import Boolean, Integer, String, DateTime


class LoginStatusSuccessSchema(Schema):
    id_ = Integer(data_key="id", required=False)
    can_delete = Boolean(required=False)
    role = String(required=False)
    token_expire = DateTime(required=False)
    token_updated = DateTime(required=False)
    token_valid = Boolean(required=False)
    username = String(required=False)
    status = String(required=False)
