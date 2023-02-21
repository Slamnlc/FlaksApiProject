from datetime import datetime, timedelta

from marshmallow import Schema, validate
from marshmallow.fields import String, DateTime

from config import Config
from helpers.helpers import generate_token


class LoginSuccessSchema(Schema):
    expire_time = datetime.now() + timedelta(minutes=Config.API_EXPIRE_MIN)
    token_expire = DateTime(metadata={"default": expire_time})
    token = String(metadata={"default": generate_token()})


class LoginFailSchema(Schema):
    messages = [
        "User not found",
        "Incorrect password",
        "Missing credentials",
    ]
    error = String(validate=validate.OneOf(messages))  # noqa
