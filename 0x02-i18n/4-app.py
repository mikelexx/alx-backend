#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, force_locale


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
    detect if the incoming request contains locale argument and
    ifs value is a supported locale, return it.
    If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    return a english and french
    translated webage
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
