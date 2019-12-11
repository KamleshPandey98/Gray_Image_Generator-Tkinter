from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import messagebox


class user_interface(Frame):
    """docstring for user_interface"""

    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.heading = Label(self.root, text="Image Converter", bg="#333945", fg="white", font="Courier 20 bold")
        self.heading.place(x=0, y=10, width=600, height=50)

        self.word_enter = Label(self.root, text="Select Image             : ", fg="black", font="Times 13 bold")
        self.word_enter.place(x=20, y=100)

        self.word_enter1 = Label(self.root, text="Output Destination : ", fg="black", font="Times 13 bold")
        self.word_enter1.place(x=20, y=130)

        self.entry1 = Text(self.root)
        self.entry1.place(x=180, y=100, height=25, width=300)

        self.entry2 = Text(self.root)
        self.entry2.place(x=180, y=130, height=25, width=300)

        self.next_btn = Button(self.root, text="Select", bg="#535C68", fg="white", command=lambda: self.next_click(),
                               font="Courier 13 bold")

        self.next_btn.place(x=500, y=100, width=80, height=25)

        self.gen_btn = Button(self.root, text="Select", bg="#535C68", fg="white",
                              command=lambda: self.gen_img(), font="Courier 13 bold")
        self.gen_btn.place(x=500, y=130, width=80, height=25)

        self.gen_btn2 = Button(self.root, text="Convert", bg="#535C68", fg="white",
                               command=lambda: self.cvt(), font="Courier 13 bold")
        self.gen_btn2.place(x=250, y=200, width=80, height=25)

        self.author = Label(root, text="Designed & Developed by - Kamlesh Pandey \u00A9 2019", font="Times 10")
        self.author.place(x=160, y=380)

    def next_click(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.entry1.insert(INSERT, self.root.filename)

    def gen_img(self):
        self.root.dir = filedialog.askdirectory()
        self.entry2.insert(INSERT, self.root.dir)

    def cvt(self):
        try:
            file = self.root.filename
            cv2.imwrite(self.root.dir + "\\test.jpg", cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2GRAY))
            cv2.imshow('Original image', cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2GRAY))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            messagebox.showerror("Something Went Wrong !")
