#!/usr/bin/python3
"""Starts flask web app."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns custom text"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ returns custom text"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays integers only"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ displays html page if int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
