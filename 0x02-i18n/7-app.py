#!/usr/bin/env python3
"""
basic flask with babel setup
"""
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz


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
users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
    },
}


def get_user() -> Union[dict, None]:
    """
    get loged in user from database
    """
    try:
        user_id = request.args.get('login_as')
        if user_id:
            user_id = int(user_id)
            return users.get(user_id)
    except Exception as e:
        return


@babel.localeselector
def get_locale() -> str:
    """
    detect if the incoming request contains locale argument and
    ifs value is a supported locale, return it.
    If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    support_locales = app.config['LANGUAGES']
    url_locale = request.args.get('locale')
    if url_locale in support_locales:
        return url_locale
    settings_locale = g.user.get('locale') if g.user else None
    if settings_locale in app.config['LANGUAGES']:
        return settings_locale
    request_header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if request_header_locale:
        return request_header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> pytz.BaseTzInfo:
    """
    configure app to appropriate timezone
    """
    try:
        url_timezone = request.args.get('timezone')
        if url_timezone:
            validated_url_timezone = pytz.timezone(url_timezone)
            return validated_url_timezone
        settings_timezone = g.user.get('timezone') if g.user else None
        if settings_timezone:
            validated_settings_timezone = pytz.timezone(settings_timezone)
            return validated_settings_timezone
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])
    except pytz.exceptions.UnknownTimeZoneError as e:
        print(f"UnknownTimeZoneError: {e}")
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


@app.before_request
def before_request() -> None:
    """
    executed before all other functions
    """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    return a english and french
    translated webage
    """
    return render_template('7-index.html')


'''
# for testing purpose
@app.route('/current_time', methods=['GET'])
def current_time():
    timezone = get_timezone()
    current_time = datetime.now(timezone)
    return f"Current time in {timezone}:\
            {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
'''

if __name__ == '__main__':
    app.run(debug=True)
