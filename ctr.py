from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from image import Image, filename_encypted, filename_decypted, Secret


class CTR:
    def __init__(self, key=None, iv=None):
        if key is None:
            key = os.urandom(32)
        self.key = key
        if iv is None:
            iv = os.urandom(16)
        self.iv = iv

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


if __name__ == "__main__":
    name = "data/tux.bmp"
    # encryption:
    img = Image()
    img.load_file(name)
    img_v = img.to_vector()

    ctr = CTR()

    enc_v = ctr.encrypt(img_v)
    img_enc = Image()
    img_enc.from_vector(enc_v, img.img)
    img_enc.save_file(filename_encypted(name))

    sec = ctr.key + ctr.iv
    Secret.save_secret(sec, name)

    # decryption:
    img = Image()
    img.load_file(filename_encypted(name))
    img_v = img.to_vector()

    sec = Secret.load_secret(name)
    ctr = CTR(sec[0:32],sec[32:48])

    dec_v = ctr.decrypt(img_v)
    img_dec = Image()
    img_dec.from_vector(dec_v, img.img)
    img_dec.save_file(filename_decypted(name))
