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


class AES256(object):
        def __init__(self, key):
            self.bs = AES.block_size
            self.key = hashlib.sha256(key.encode()).digest()

        def encrypt(self, raw):
            raw = self._pad(raw)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return base64.b64encode(iv + cipher.encrypt(raw))

        def decrypt(self, enc):
            enc = base64.b64decode(enc)
            iv = enc[:AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

        def _pad(self, s):
            return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

        @staticmethod
        def _unpad(s):
            return s[:-ord(s[len(s) - 1:])]