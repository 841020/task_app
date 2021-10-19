import os

from flask import Flask

from models import init_db
from path import create_route


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    config_dt = {
        "SECRET_KEY": "dev",
        "DATABASE": "sqlite:///sample.db",
        "JSON_AS_ASCII": False
    }
    app.config.update(config_dt)

    if test_config:
        # load the test config if passed in
        test_config = {"DATABASE": "sqlite:///testing.db"}
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    create_route(app)
    init_db(app)
    app.add_url_rule("/", endpoint="index")
    return app
