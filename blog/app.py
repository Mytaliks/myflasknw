from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, my dear friends"


@app.route('/user')
def user():
    return 'My user!'