#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    define languages babel supports and locale
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    select most preferred language from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    setup flask route
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
