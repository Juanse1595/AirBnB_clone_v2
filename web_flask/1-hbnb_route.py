#!/usr/bin/python3
'''1-hbnb_route
Starts a Flask web application'''
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


if __name__ == '__main__':
    app.run(host="0.0.0.0")
