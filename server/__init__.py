from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "6fbf401890e90b47598f5wv5l290eb21"

# Change URI to your specific database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../test.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from server import routes
