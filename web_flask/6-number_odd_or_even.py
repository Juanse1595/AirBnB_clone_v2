#!/usr/bin/python3
"""3-python_route module
Starts a Flask web application"""
from flask import Flask, render_template


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
    return f"C {text}".replace("_", " ")


@app.route("/python")
@app.route("/python/<text>") # What's with those parentesis (<text>)?
def py_text(text="is cool"):
    """
    Return value for /python/(<text>)
    """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>")
def n_int(n):
    """
    Returns 'n is a number' only if n is an integer
    """
    return "{} is an integer".format(n)


@app.route("/number_template/<int:n>")
def n_template(n):
    """
    Returns a template if n is integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    Returns a template that says if n is odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
