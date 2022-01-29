#!/usr/bin/python3
"""3-python_route module
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


@app.route("/python")
@app.route("/python/<text>")  # What's with those parentesis (<text>)?
def py_text(text="is cool"):
    """
    Return value for /python/(<text>)
    """
    return "Python {}".format(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
