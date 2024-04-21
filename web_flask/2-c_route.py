#!/usr/bin/python3
"""
1th file with a basic Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """
    Root route that returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Root route that returns 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Root route that returns the letter C with additional text
    """
    return f"C {text}".replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
