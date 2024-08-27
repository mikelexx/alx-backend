#!/usr/bin/env python3
"""
basic flask setup
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """
    setup flask route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
