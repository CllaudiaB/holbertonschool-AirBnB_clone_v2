#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask

capp = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    #display Hello HBNB!
    return "<p>Hello HBNB!</p>"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
