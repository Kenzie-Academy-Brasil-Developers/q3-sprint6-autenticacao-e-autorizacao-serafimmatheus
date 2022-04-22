from flask import Flask
from os import getenv
from app.configs import database, migration, jwt
from app import routes


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = getenv("SECRET_KEY")

    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app
