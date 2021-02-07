import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt import JWT


def create_app(testing=False):
    app = Flask(__name__)

    CORS(app)

    app.config.from_object("application.config.Config")

    if testing:
        app.config["TESTING"] = True
    else:
        from models import db

        db.init_app(app)

    from application.security import authenticate, identity

    jwt = JWT(app, authenticate, identity)  # /auth

    api = Api(app)

    from resources import api_bp

    app.register_blueprint(api_bp, url_prefix='/api/v1')

    # Routes
    @app.route("/health")
    def health():
        return "Ok"

    return app
