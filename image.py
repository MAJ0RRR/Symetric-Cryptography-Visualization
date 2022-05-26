from skimage.io import imread, imsave
from numpy import reshape, frombuffer


def filename_encrypted(file):
    file_name = file.split('.')[0]
    file_type = file.split('.')[1]
    if file_type != "bmp":
        file_type = "bmp"
    file_enc = file_name + "-enc." + file_type
    return file_enc


def filename_decrypted(file):
    file_name = file.split('.')[0]
    file_type = file.split('.')[1]
    file_dec = file_name + "-dec." + file_type
    return file_dec


class Image:
    def __init__(self):
        self.img = None
        self.shape = None

    def load_file(self, file):
        self.img = imread(fname=file)
        self.shape = self.img.shape

    def to_vector(self):
        img_vector = reshape(self.img, -1)
        img_vector = img_vector.tobytes()
        return img_vector

    def from_vector(self, img_vector, original_img):
        img_v = frombuffer(img_vector, dtype=original_img.dtype)
        self.img = reshape(img_v, original_img.shape)

    def save_file(self, file):
        imsave(fname=file, arr=self.img)


class Secret:
    @staticmethod
    def save_secret(secret, file):
        sec_file = open(file + ".secret", "wb")
        sec_file.write(secret)
        sec_file.close()

    @staticmethod
    def load_secret(file):
        sec_file = open(file + ".secret", "rb")
        secret = sec_file.readline()
        sec_file.close()
        return secret
