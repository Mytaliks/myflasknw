from blog.app import app
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, my dear friends"


@app.route('/user')
def user():
    return 'My!'


if __name__ == '__main__':
    app.run(debug=True)
