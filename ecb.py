from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from block_algorithm import BlockAlgorithm


class ECB(BlockAlgorithm):
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

    def run_encryption(self, file, error):
        self.encryption(file, error, ECB)

    def run_decryption(self, file, error):
        self.decryption(file, error, ECB)
