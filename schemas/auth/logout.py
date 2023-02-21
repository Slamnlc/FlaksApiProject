from marshmallow import Schema
from marshmallow.fields import String


class LogoutSuccessSchema(Schema):
    status = String(
        metadata={"default": "User {username} is successfully logged out"}
    )
