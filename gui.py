from tkinter import *
from tkinter import filedialog
import PIL.Image
from PIL import ImageTk


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Kryptografia symetryczna - Temat 14")
        self.root.geometry("600x600")
        self.root.configure(bg='#0BB5FF')
        self.btn = Button(self.root, text='open image', command=self.open_img).grid(row=1, columnspan=4)

    def loop(self):
        self.root.mainloop()

    @staticmethod
    def openfilename():
        filename = filedialog.askopenfilename(title='Open')
        return filename

    def open_img(self):
        x = self.openfilename()
        img = PIL.Image.open(x)
        img = img.resize((150, 150), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self.root, image=img)
        panel.image = img
        panel.grid(row=2)
