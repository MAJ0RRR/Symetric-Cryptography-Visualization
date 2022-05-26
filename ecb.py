from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from image import *
import os


class ECB:
    def __init__(self, key=None):
        if key is None:
            key = os.urandom(32)
        self.key = key

    def encrypt(self, data):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return ct

    def decrypt(self, ct):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        return result

    @staticmethod
    def run_encryption(file):
        # Load
        img = Image()
        img.load_file(file)
        img_v = img.to_vector()
        # Encrypt
        ecb = ECB()
        enc_v = ecb.encrypt(img_v)
        img_enc = Image()
        img_enc.from_vector(enc_v, img.img)
        img_enc.save_file(filename_encrypted(file))
        Secret.save_secret(ecb.key, file)

    @staticmethod
    def run_decryption(file):
        # Load
        img = Image()
        img.load_file(filename_encrypted(file))
        img_v = img.to_vector()
        # Decrypt
        ecb = ECB(Secret.load_secret(file))
        dec_v = ecb.decrypt(img_v)
        img_dec = Image()
        img_dec.from_vector(dec_v, img.img)
        img_dec.save_file(filename_decrypted(file))
