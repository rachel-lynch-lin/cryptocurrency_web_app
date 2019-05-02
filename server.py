#!/usr/bin/env python3.6

from os import environ

# Import requirements
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sqlalchemy import distinct, extract

# Import model and database functions from model.py
from model import GlobalCD
from model import connect_to_db, db


app = Flask(__name__)

# Secret key for flask session and the debug toolbar
app.secret_key = environ.get("FLASK_SECRET_KEY")


app.jinja_env.undefined = StrictUndefined


###############################################################################

@app.route('/')
def index():
    """Homepage"""

    globalcd = GlobalCD.query.all()

    return render_template('index.html',
                           globalcd=globalcd)



###############################################################################

if __name__ == "__main__":
    # Set to true but only during development
    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar

    app.run(port=5000, host="0.0.0.0")