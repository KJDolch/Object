"""
Exercise 16 - Radio Buttons with Button Box
"""
import tkinter as tk


class Radio:
    def __init__(self):
        self.root = tk.Tk()
        self.var = tk.IntVar()
        self.var.set(1)
        self.label1 = tk.Label(self.root, text="Pick one of the following")
        self.label1.pack()
        self.radio1 = tk.Radiobutton(
            self.root,
            text="Monday",
            variable=self.var,
            value=1,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio1.pack(anchor="w")
        self.radio2 = tk.Radiobutton(
            self.root,
            text="Tuesday",
            variable=self.var,
            value=2,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio2.pack(anchor="w")
        self.radio3 = tk.Radiobutton(
            self.root,
            text="Wednesday",
            variable=self.var,
            value=3,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio3.pack(anchor="w")
        self.radio4 = tk.Radiobutton(
            self.root,
            text="Thursday",
            variable=self.var,
            value=4,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio4.pack(anchor="w")
        self.radio5 = tk.Radiobutton(
            self.root,
            text="Friday",
            variable=self.var,
            value=5,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio5.pack(anchor="w")
        self.radio6 = tk.Radiobutton(
            self.root,
            text="Saturday",
            variable=self.var,
            value=6,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio6.pack(anchor="w")
        self.radio7 = tk.Radiobutton(
            self.root,
            text="Sunday",
            variable=self.var,
            value=7,
            command=self.ShowChoice,
            indicator=0,
            width=20,
        )
        self.radio7.pack(anchor="w")
        self.root.mainloop()

    def ShowChoice(self):
        print(self.var.get())


Radio()
