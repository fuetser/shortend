from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "a;sdgoharpgihaeprih"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app import routes, models

db.create_all()
