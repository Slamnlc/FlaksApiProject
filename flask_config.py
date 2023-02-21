from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from config import DatabaseConfig


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = DatabaseConfig.CONNECTION_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APISPEC_SPEC = APISpec(
        title="My Flask Service",
        version="v1.0",
        plugins=[MarshmallowPlugin()],
        openapi_version="2.0.0",
    )
    APISPEC_SWAGGER_URL = "/swagger.json/"
    APISPEC_SWAGGER_UI_URL = "/swagger/"
