from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from image import *
import os


class CTR:
    def __init__(self, key=None, iv=None):
        if key is None:
            key = os.urandom(32)
        self.key = key
        if iv is None:
            iv = os.urandom(16)
        self.iv = iv
        self.sec = None

    def encrypt(self, data):
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return ct

    def decrypt(self, ct):
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv))
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        return result

    def run_encryption(self, file):
        # Load
        img = Image()
        img.load_file(file)
        img_v = img.to_vector()
        # Encrypt
        ctr = CTR()
        enc_v = ctr.encrypt(img_v)
        img_enc = Image()
        img_enc.from_vector(enc_v, img.img)
        img_enc.save_file(filename_encrypted(file))
        self.sec = ctr.key + ctr.iv
        Secret.save_secret(self.sec, file)

    def run_decryption(self, file):
        # Load
        img = Image()
        img.load_file(filename_encrypted(file))
        img_v = img.to_vector()
        # Decrypt
        ctr = CTR(self.sec[0:32], self.sec[32:48])
        dec_v = ctr.decrypt(img_v)
        img_dec = Image()
        img_dec.from_vector(dec_v, img.img)
        img_dec.save_file(filename_decrypted(file))
