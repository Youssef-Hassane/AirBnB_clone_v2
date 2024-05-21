#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


# Define a route for the root URL ("/") and disable strict slashes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a string at the root URL."""
    return 'Hello HBNB!'


# Define a route for the /hbnb URL and disable strict slashes
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string at the /hbnb URL."""
    return 'HBNB'


# Define a route for the /c/<text> URL and disable strict slashes
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return a string at the /c/<text> URL."""
    return 'C {}'.format(text.replace('_', ' '))


# Define a route for the /python/(<text>) URL and disable strict slashes
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Return a string at the /python/<text> URL."""
    return 'Python {}'.format(text.replace('_', ' '))


# Define a route for the /number/<n> URL and disable strict slashes
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a string at the /number/<n> URL."""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
