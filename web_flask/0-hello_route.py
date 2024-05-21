#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


# Define a route for the root URL ("/") and disable strict slashes
@app.route('/', strict_slashes=False)
def hello():
    """Return a string at the root URL."""
    return 'Hello HBNB!'


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
