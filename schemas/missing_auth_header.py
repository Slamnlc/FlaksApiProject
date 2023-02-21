from marshmallow import Schema, validate
from marshmallow.fields import String


class MissAuthHeaderSchema(Schema):
    messages = [
        "Missing token",
        "Incorrect token",
        "Token expired",
        "Wrong access",
    ]
    error = String(validate=validate.OneOf(messages))  # noqa
