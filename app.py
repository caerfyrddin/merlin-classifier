from src.app import App
from flask import Flask, request

flask = Flask(__name__)
App().init(flask)

@App.instance.flask.route("/")
def index():
    html = "Welcome to " + App.instance.name + "</p>"
    return html