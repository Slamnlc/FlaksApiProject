from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flask_config import FlaskConfig
from helpers.helpers import create_logger

app = Flask(__name__)
app.config.from_object(FlaskConfig)
db = SQLAlchemy(app)
api = Api(app, prefix="/api")
docs = FlaskApiSpec(app)

app.app_context().push()
logger = create_logger("logger")

import api_resources  # noqa
import database.models  # noqa
