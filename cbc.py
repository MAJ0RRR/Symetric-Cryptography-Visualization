from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from image import *
import os


class CBC:
    def __init__(self, key=None, iv=None):
        if key is None:
            key = os.urandom(32)
        self.key = key
        if iv is None:
            iv = os.urandom(16)
        self.iv = iv

    def encrypt(self, data):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return ct

    def decrypt(self, ct):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        return result

    @staticmethod
    def run_encryption(file):
        pass

    @staticmethod
    def run_decryption(file):
        pass
