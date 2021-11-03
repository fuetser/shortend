from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from secrets import token_urlsafe


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", token_urlsafe(32))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///../db.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app import routes, models, errors
