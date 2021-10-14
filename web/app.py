import json

from flask import Flask, jsonify, request

from models import get_tasks_list, add_task, get_task

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify(json.loads(get_tasks_list()))


@app.route("/task", methods=['POST'])
def add_tasks():
    data = request.json
    add_task(data)
    return jsonify(json.loads(get_task(data)))
