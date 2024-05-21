#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


# Close SQLAlchemy Session
@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


# Route: /states_list
@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays an HTML page with a list of all State objects in DBStorage """
    states = storage.all()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
