#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask, render_template


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>")
def display_py_text(text='is cool'):
    """function that display “Python ”, followed by the value of the text
       variable (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_even(n):
    """display “n is a number” only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
