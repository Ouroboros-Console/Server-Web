from server import db
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INT, nullable=True, primary_key=True)
    email = db.Column(db.VARCHAR, unique=True, nullable=False)
    password = db.Column(db.VARCHAR, nullable=False)
    address = db.Column(db.VARCHAR, nullable=False)
    api_key = db.Column(db.VARCHAR,nullable=False)

    def __repr__(self):
        return f"User({self.email})"


class Encrypt:
    __backend = default_backend()
    __message = None

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def __init__(self, key, iv):
        self.__key = key
        self.__iv = iv

    def set_cipher(self):
        self.__cipher = Cipher(algorithms.AES(self.__key), modes.CBC(self.__iv), backend=self.__backend)

    def set_encryptor(self):
        encryptor = self.__cipher.encryptor()
        en_key = encryptor.update(self.__message) + encryptor.finalize()
        return en_key

    def set_decryptor(self, cit):
        decryptor = self.__cipher.decryptor()
        return decryptor.update(cit) + decryptor.finalize()
