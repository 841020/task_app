from flask import Flask,  request

from models import get_tasks_list, add_task, get_task

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/task", methods=['POST'])
def create_task():
    data = request.json
    data_id = add_task(data)
    return get_task(data_id), 201


@app.route("/tasks", methods=['GET'])
def read_tasks():
    return get_tasks_list()


@app.route("/task", methods=['POST'])
def add_tasks():
    data = request.json
    add_task(data)
    return jsonify(json.loads(get_task(data)))
