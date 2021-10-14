from flask import Flask,  request

from models import Tasks
from orm_controller import read_rows_list, create_row, read_row, update_row

app = Flask(__name__)


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
def update_task(id):
    data = request.json
    update_row(Tasks, id, data)
    return read_row(Tasks, id)


# @app.route("/task/<int:id>", methods=['DELETE'])
# def delete_task():
#     pass


@app.route("/task", methods=['POST'])
def add_tasks():
    data = request.json
    add_task(data)
    return jsonify(json.loads(get_task(data)))
