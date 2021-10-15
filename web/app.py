import os

from flask import Flask, request

from models import Tasks, init_db
from orm_controller import create_row, read_rows_list,  read_row, update_row, delete_row


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    config_dt = {
        "SECRET_KEY": "dev",
        "DATABASE": "sqlite:///sample.db"
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

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/task", methods=['POST'])
    def create_task():
        data = request.json
        data_id = create_row(Tasks, data)
        return read_row(Tasks, data_id), 201

    @app.route("/tasks", methods=['GET'])
    def read_tasks():
        return read_rows_list(Tasks)

    @app.route("/task/<int:id>", methods=['PUT'])
    def update_task(id=0):
        data = request.json
        update_row(Tasks, id, data)
        return read_row(Tasks, id)

    @app.route("/task/<int:id>", methods=['DELETE'])
    def delete_task(id=0):
        delete_row(Tasks, id)
        return '', 200
    init_db(app)
    app.add_url_rule("/", endpoint="index")
    return app
