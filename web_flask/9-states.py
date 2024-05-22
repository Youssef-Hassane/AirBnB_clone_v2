#!/usr/bin/python3
""" Module to start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
@app.teardown_appcontext
def shutdown_session(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


# Create a route for /states and /states/<state_id>
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
# Define a function to handle the /states and /states/<state_id> routes
def handle_states(state_id=None):
    """List states and render template"""
    # Get all states from storage
    states = storage.all(State)
    # Check if a specific state_id is provided
    if state_id is not None:
        # Prepend 'State.' to the state_id
        state_id = 'State.' + state_id
    # Render the template with the states and state_id variables
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
