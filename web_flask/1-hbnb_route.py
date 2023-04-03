#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """function that display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """function that display HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
