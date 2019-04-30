"""Models and database functions for the Cryptocurrency Web App"""

from flask_sqlalchemy import SQLAlchemy

from consts import GLOBAL_CRYPTO_DATA
import requests

db = SQLAlchemy()

###############################################################################
# Model definitions

class GlobalCD(db.Model):
    """Information about crypto market"""

    __tablename__ = "globalcd"
    
    globalcd_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    coins_count = db.Column(db.Integer)
    active_markets = db.Column(db.Integer)
    total_mcap = db.Column(db.Float)
    total_volume = db.Column(db.Float)
    btc_d = db.Column(db.String)
    eth_d = db.Column(db.String)
    mcap_change = db.Column(db.String)
    volume_change = db.Column(db.String)
    avg_change_percent = db.Column(db.Float)
    volume_ath = db.Column(db.Integer)
    mcap_ath = db.Column(db.Integer)

    def get_global_crypto_data(self):
        """Display info on the Global Crypto Data"""
      
        return self.globalcd_id.split(",")[0]


###############################################################################

def connect_to_db(app, database='postgresql:///cryptocurrency'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()