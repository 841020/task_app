from flask import Flask, jsonify
from models import Tasks, get_tasks_list
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({
        "result": get_tasks_list()
    })
