from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from image import Image, filename_encypted, filename_decypted, Secret

# code using already implemented mode in ciphers
# to discuss it


class ECB:
    def __init__(self,key=None):
        if key is None:
            key = os.urandom(32)
        self.key = key

    def encrypt(self,data):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return ct

    def decrypt(self,ct):
        cipher = Cipher(algorithms.AES(self.key), modes.ECB())
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        return result


if __name__ == "__main__":
    name = "data/tux.bmp"
    # encryption:
    img = Image()
    img.load_file(name)
    img_v = img.to_vector()

    ecb = ECB()

    enc_v = ecb.encrypt(img_v)
    img_enc = Image()
    img_enc.from_vector(enc_v,img.img)
    img_enc.save_file(filename_encypted(name))

    Secret.save_secret(ecb.key, name)

    # decryption:
    img = Image()
    img.load_file(filename_encypted(name))
    img_v = img.to_vector()

    ecb = ECB(Secret.load_secret(name))

    dec_v = ecb.decrypt(img_v)
    img_dec = Image()
    img_dec.from_vector(dec_v, img.img)
    img_dec.save_file(filename_decypted(name))
