#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale() -> str:
    """
    return locale language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app)
babel.locale_selector_func = get_locale


@app.route('/')
def hello_world() -> str:
    """
    setup flask route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
