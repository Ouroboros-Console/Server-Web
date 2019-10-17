from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "6fbf401890e90b47598f5wv5l290eb21"

# Setting mysql
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://lucifer680:lucifer123@db4free.net/ouroboros"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from server import routes