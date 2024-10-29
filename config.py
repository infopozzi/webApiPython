import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["HOST"] = '0.0.0.0'
app.config["PORT"] = 8080
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# mysql://<username>:<password>@<host>/<db_name>

db = SQLAlchemy(app)
