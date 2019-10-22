from server import db
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class User(db.Model):
    __tablename__ = 'user'
    email = db.Column(db.VARCHAR, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.VARCHAR, nullable=False)
    address = db.Column(db.VARCHAR, nullable=False)
    api_key = db.Column(db.BLOB, nullable=False)
    en_key = db.Column(db.VARCHAR, nullable=False)
    iv = db.Column(db.BLOB, nullable=False)

    def __repr__(self):
        return f"User({self.id})"

# Create a Crypto class which will enrypt and decrypt
class AES256(object):
        
