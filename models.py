"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake model"""


    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Coumn(db.Text, nullable=False)
    size = db.Coumn(db.Text, nullable=False)
    rating = db.Coumn(db.Float, nullable=False)
    image = db.Coumn(db.Text, default='https://tinyurl.com/demo-cupcake')