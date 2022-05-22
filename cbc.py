import random
from operator import xor
from cryptography.fernet import Fernet
import sys
import math

"""
  Plain Text Block 1   |  Plain Text Block 2   |..|  Plain Text Block N   |
             |         |                |      |..|                 |     |
|IV|------->(+)        | |-|IV|------->(+)     |..|  |-|IV|------->(+)    |
             |         | |              |      |..|  |              |     |
|KEY|--->|ENCRYPT|     | | |KEY|--->|ENCRYPT|  |..|  | |KEY|--->|ENCRYPT| |
             |         | |              |      |..|  |              |     |
             |---------|-|              |------|..|--|              |     |
             |         |                |      |..|                 |     |
             v         |                v      |..|                 v     |
  Cipher Text Block 1  |  Cipher Text Block 2  |..|  Cipher Text Block N  |
"""


class CBC:
    def __init__(self, block_size):
        """
        :param block_size: Size of blocks that plain text/cipher text
        will be divided
        """
        self._block_size = block_size
        self._key = Fernet(Fernet.generate_key())
        self._iv = 0

    def encrypt(self, data):
        """
        :param data: data to encrypt
        """
        blocks_amount = math.ceil((sys.getsizeof(data) * 8) / self._block_size)
        self._iv = bytes(random.getrandbits(self._block_size))
        iv = self._iv
        cipher = []
        for _ in range(blocks_amount):
            iv = self.data_to_cipher(iv, data)
            cipher.append(iv)
        with open("encrypted.bin", 'wb') as f:
            for b in cipher:
                f.write(bytes(b))
        f.close()

    def decrypt(self):
        with open("encrypted.bin", 'rb') as f:
            data = bytes(f.read())
        f.close()
        blocks_amount = math.ceil((sys.getsizeof(data) * 8) / self._block_size)
        text = [self.cipher_to_data(self._iv, data[:self._block_size])]
        l = 0
        r = self._block_size
        for _ in range(blocks_amount):
            text.append(self.cipher_to_data(data[l:r], data[l:r]))
            l = l + self._block_size
            r = r + self._block_size
        print(text)

    def data_to_cipher(self, iv, data):
        """
        :param iv: Initialization vector
        :param data: Data to encrypt
        :return: Encrypted xor of iv and data as bytes
        """
        encrypted_data = self._key.encrypt(bytes(xor(bool(data), bool(iv))))
        return bytes(encrypted_data)

    def cipher_to_data(self, iv, cipher):
        """
        :param iv: Initialization Vector
        :param cipher: Cipher Text to encrypt
        :return: encrypted data in utf-8 format
        """
        data = self._key.decrypt(bytes(cipher))
        return xor(bool(iv), bool(data)).encode('utf-8')
