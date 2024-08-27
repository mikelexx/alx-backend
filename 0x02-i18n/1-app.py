#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    config localization variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    setup flask route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
