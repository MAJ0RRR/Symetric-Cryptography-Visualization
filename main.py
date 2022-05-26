from ecb import ECB
from ctr import CTR
from gui import GUI

if __name__ == "__main__":
    ecb = ECB()
    ecb.run_encryption("data/tux.bmp")
    ecb.run_decryption("data/tux.bmp")

    ctr = CTR()
    ctr.run_encryption("data/tux.bmp")
    ctr.run_decryption("data/tux.bmp")

    gui = GUI()
    gui.loop()
