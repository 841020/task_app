from flask import Flask,  request

from models import Tasks
from orm_controller import create_row, read_rows_list,  read_row, update_row, delete_row

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
def update_task(id=0):
    data = request.json
    update_row(Tasks, id, data)
    return read_row(Tasks, id)


@app.route("/task/<int:id>", methods=['DELETE'])
def delete_task(id=0):
    delete_row(Tasks, id)
    return '', 200
