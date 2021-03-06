from flask import Flask

from .extensions import api
from .extensions import cors
from resources.game import game_ns

DEFAULT_HOST = "0.0.0.0"


def register_namespaces():
    """ Registers namespaces to the API for swagger documentation"""
    api.add_namespace(game_ns)


def initialize_extensions(app):
    """
    Initializes the given Flask app with the extensions listed below:
    Api - Flask RESTplus api

    Args:
        app: Constructed Flask app
    """
    api.init_app(app=app)
    cors.init_app(app=app)


def create_app():
    """
    Creates Flask app with initialized extensions
    Returns:
        Flask app with initialized extensions (Flask RESTplus, Flask SQLAlchemy, etc)
    """
    app = Flask(__name__)
    initialize_extensions(app=app)
    register_namespaces()
    return app


if __name__ == "__main__":
    _app = create_app()
    _app.run(host=DEFAULT_HOST, debug=True)
