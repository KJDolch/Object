"""
Exercise 12 - Creating Labels
"""
# create a GUI that contains three different Labels
# at least two of them should get their text from the construction of the GUI
# the last one should get the text by simply adding it as an attribute in the definition of the constructor
import tkinter as tk


class Creating_Labels:
    def __init__(self, arg_text3):
        self.root = tk.Tk()
        self.root.title("Creating Labels")
        self.label1 = tk.Label(self.root, text="This is label1")
        self.label1.pack(side="top")

        self.label2 = tk.Label(self.root, text="And label2")
        self.label2.pack(side="right")

        self.label3 = tk.Label(self.root, text=arg_text3)
        self.label3.pack(side="bottom")

        self.root.mainloop()


Creating_Labels("Third Label")
