#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """function that display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """function that display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """function that display “C ” followed by the value of the text variable
       (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
