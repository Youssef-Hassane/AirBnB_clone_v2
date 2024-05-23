#!/usr/bin/python3
"""TASK 10 Simble flask app"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

# Create a new Flask web application
app = Flask(__name__)


# Register a new function that closes the storage
@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request"""
    storage.close()


# Define a route for '/hbnb_filters' in the Flask application
@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
    """Display a list of states and amenities"""
    # Get all states and amenities from the storage
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    # Render the template '10-hbnb_filters.html' with the states and amenities
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
