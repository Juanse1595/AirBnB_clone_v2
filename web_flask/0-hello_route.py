#!/usr/bin/python3
"""
0th file with a basic Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Root route that returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
