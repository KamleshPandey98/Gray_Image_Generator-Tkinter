# Grayout Image

from tkinter import *
from Part2 import user_interface as UI


def app():
    root = Tk()
    root.geometry("600x400+300+100")
    root.resizable(False, False)
    root.title("Grey Image Generator")

    frame = UI(root)
    frame.place()

    root.mainloop()


if __name__ == '__main__':
    app()
