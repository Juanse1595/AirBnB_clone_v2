#!/usr/bin/python3
"""7-states_list module
Starts a Flask web application"""
from flask import Flask, render_template
from models import storage


storage_objs = storage.all()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''Sends objects to html template'''
    return render_template('7-states_list.html', objs=storage_objs)


@app.teardown_appcontext
def remove_session(self):
    '''Removes session'''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
