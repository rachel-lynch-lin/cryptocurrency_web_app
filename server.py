from os import environ

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from sqlalchemy import distinct, extract

app = Flask(__name__)

# Secret key for flask session and the debug toolbar
app.secret_key = environ.get("FLASK_SECRET_KEY")


app.jinja_env.undefined = StrictUndefined


###############################################################################

@app.route('/')
def index():
    """Homepage"""

    return render_template('index.html')



###############################################################################

if __name__ == "__main__":
    # Set to true but only during development
    app.debug = True
    # connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")