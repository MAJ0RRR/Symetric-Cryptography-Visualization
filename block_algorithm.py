from abc import ABC, abstractmethod
from image_loader import *
import os


class BlockAlgorithm(ABC):

    def __init__(self, key=None, iv=None):
        if key is None:
            key = os.urandom(32)
        self.key = key
        if iv is None:
            iv = os.urandom(16)
        self.iv = iv
        self.sec = None

    @staticmethod
    def save_file(enc_v, file, img):
        if img is None:
            with open(file, "wb") as txt_file:
                txt_file.write(enc_v)
        else:
            ldr = ImageLoader()
            ldr.from_vector(enc_v, img)
            ldr.save_file(file)



    @staticmethod
    def load_file(error, file):
        if file.split('.')[1] == "txt":
            ldr = TxtLoader()
        else:
            ldr = ImageLoader()

        ldr.load_file(file)
        v = ldr.simulate_error(file, error)
        return ldr.img, v

    def encryption(self, file, error, mode):
        img, v = self.load_file(error, file)
        m = mode()
        enc_v = m.encrypt(v)
        self.save_file(enc_v, filename_encrypted(file), img)
        self.sec = m.key + m.iv
        Secret.save_secret(self.sec, filename_encrypted(file))

    def decryption(self, file, error, mode):
        img, v = self.load_file(error, file)
        # Decrypt
        sec = Secret.load_secret(file)
        m = mode(sec[0:32], sec[32:48])
        dec_v = m.decrypt(v)
        self.save_file(dec_v, filename_decrypted(file), img)