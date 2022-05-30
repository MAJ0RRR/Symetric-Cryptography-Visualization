from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from block_algorithm import BlockAlgorithm


class CFB(BlockAlgorithm):
    def encrypt(self, data):
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(data) + encryptor.finalize()
        return ct

    def decrypt(self, ct):
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.iv))
        decryptor = cipher.decryptor()
        result = decryptor.update(ct) + decryptor.finalize()
        return result

    def run_encryption(self, file, error):
        self.encryption(file, error, CFB)

    def run_decryption(self, file, error):
        self.decryption(file, error, CFB)