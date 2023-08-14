#RestApi
from flask import Flask
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite:///database/quiz.db"
db.init_app(app)

