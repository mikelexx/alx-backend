#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('babel.cfg')
babel = Babel(app)


@app.route('/')
def hello_world() -> str:
    """
    setup flask route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
