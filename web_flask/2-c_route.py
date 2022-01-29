#!/usr/bin/python3
"""2-c_route module
Starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    Return value for root route
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Return value for /hbnb route
    """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """
    Return value for /c/<text>
    """
    return "C {}".format(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
