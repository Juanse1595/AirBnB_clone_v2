#!/usr/bin/python3
"""8-cities_by_states module
Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''Sends objects to html template'''
    state_objs = storage.all(State).values()
    return render_template('7-states_list.html', state_objs=state_objs)

@app.route('/cities_by_states')
def cities_by_states_list():
    '''Sends objects to html template'''
    state_objs = storage.all(State).values()
    return render_template('8-cities_by_states.html', state_objs=state_objs)

@app.teardown_appcontext
def remove_session(self):
    '''Removes session'''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
