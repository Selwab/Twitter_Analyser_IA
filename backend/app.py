from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import click
import sqlalchemy
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from models import db
from seeds import *

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_sentiment_table(db)
        seed_image_table(db)
    app.run(debug=True, port=8000)