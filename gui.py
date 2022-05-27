from tkinter import *
from tkinter import filedialog, messagebox
import PIL
from PIL import Image, ImageTk
from ecb import ECB
from cbc import CBC
from ctr import CTR
import os

P1_X = 100  # First Image X
P2_X = 350  # Second Image X
P_Y = 50  # Image Y
RES = 150  # Resize
MENU_Y = 375  # Menu Labels Y
ACTION_X = 50  # Action Menu X
MODE_X = 450  # Mode Menu X
OFFSET = 50  # Margin


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Temat 14 - Kryptografia Symetryczna")
        self.size = 600
        self.geometry(f"{self.size}x{self.size}")
        self.resizable(False, False)
        icon = PhotoImage(file='data/icon.png')
        self.iconphoto(False, icon)
        self.configure(bg='#ede8b6')
        self.path = None

        # Default Images and  buttons
        self.open_img("data/blank.png", P1_X, P_Y)
        self.open_img("data/blank.png", P2_X, P_Y)
        Button(text="Choose file", command=self.open_img_dialog, width=12).place(x=255, y=250)
        Button(text="Run", command=self.run, width=12).place(x=255, y=300)
        Label(text="Simulate error (%)").place(x=250, y=MENU_Y)
        self.error = Scale(from_=0, to=100, orient=HORIZONTAL, width=10)
        self.error.place(x=250, y=425)

        # Action and Mode Menu
        self.action = StringVar()
        self.mode = StringVar()
        self.r = []
        Label(text="Choose Action: ").place(x=50, y=MENU_Y)
        self.r.append(Radiobutton(text="Encrypt", variable=self.action, value="encrypt", tristatevalue=0))
        self.r.append(Radiobutton(text="Decrypt", variable=self.action, value="decrypt", tristatevalue=0))
        Label(text="Choose mode: ").place(x=450, y=MENU_Y)
        self.r.append(Radiobutton(text="ECB", variable=self.mode, value="ecb", tristatevalue=0))
        self.r.append(Radiobutton(text="CBC", variable=self.mode, value="cbc", tristatevalue=0))
        self.r.append(Radiobutton(text="CTR", variable=self.mode, value="ctr", tristatevalue=0))
        self.init_radio()

    # Helper function, open dialog and return filepath
    @staticmethod
    def open_file():
        filename = filedialog.askopenfilename(title='Open')
        return filename

    # Get path of Image from dialog window and put it in default location
    def open_img_dialog(self):
        self.path = self.open_file()
        self.open_img(self.path, P1_X, P_Y)
        self.open_img("data/blank.png", P2_X, P_Y)

    # Put Image in custom location with provided path
    def open_img(self, path, x, y):
        img = PIL.Image.open(path)
        img = img.resize((RES, RES), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.place(x=x, y=y)

    # Place and deselect all radio buttons
    def init_radio(self):
        y_mode = MENU_Y + OFFSET
        y_action = MENU_Y + OFFSET
        for i in range(2):
            self.r[i].place(x=ACTION_X, y=y_action)
            y_action += OFFSET
            self.r[i].deselect()
        for i in range(2, 5):
            self.r[i].place(x=MODE_X, y=y_mode)
            y_mode += OFFSET
            self.r[i].deselect()

    def run(self):
        mode = None
        # Set up mode
        if self.mode.get() == "ecb":
            mode = ECB()
        elif self.mode.get() == "cbc":
            mode = CBC()
        elif self.mode.get() == "ctr":
            mode = CTR()
        if mode is None:
            messagebox.showerror("Error", "You have to choose a mode.")
            exit()
        # Make sure file is chosen
        if self.path is None:
            messagebox.showerror("Error", "You have to choose a file.")
            exit()
        # Set up action and run it
        if self.action.get() == "encrypt":
            mode.run_encryption(self.path, self.error.get())
            new_path = os.path.splitext(self.path)[0] + "-enc" + os.path.splitext(self.path)[1]
            self.open_img(new_path, P2_X, P_Y)
        elif self.action.get() == "decrypt":
            mode.run_decryption(self.path, self.error.get())
            new_path = os.path.splitext(self.path)[0] + "-dec" + os.path.splitext(self.path)[1]
            self.open_img(new_path, P2_X, P_Y)
        else:
            messagebox.showerror("Error", "You have to choose an action.")
            exit()

    # Run GUI
    def loop(self):
        self.mainloop()
