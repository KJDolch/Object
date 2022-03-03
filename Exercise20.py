"""
Exercise 20 - Using Grid
"""
# create a GUI with Grid
# include at least 10 different elements
# one button is a must, the button should have a function assigned to him

import tkinter as tk


class Grid:
    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry("240x100")
        self.root.title("Invitation")
        self.root.resizable(0, 0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.where_L = tk.Label(self.root, text="Where:")
        self.where_L.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.where_E = tk.Entry(self.root)
        self.where_E.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        self.when_L = tk.Label(self.root, text="When:")
        self.when_L.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.when_E = tk.Entry(self.root)
        self.when_E.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.time_L = tk.Label(self.root, text="Time:")
        self.time_L.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.time_E = tk.Entry(self.root)
        self.time_E.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        self.cake_L = tk.Label(self.root, text="What cake will I bring:")
        self.cake_L.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)
        self.cake_E = tk.Entry(self.root)
        self.cake_E.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)
        self.drink_L = tk.Label(self.root, text="What drink I will bring:")
        self.drink_L.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)
        self.drink_E = tk.Entry(self.root)
        self.drink_E.grid(column=3, row=1, sticky=tk.E, padx=5, pady=5)
        self.plus1_L = tk.Label(self.root, text="Plus 1:")
        self.plus1_L.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
        self.plus1_E = tk.Entry(self.root)
        self.plus1_E.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)
        self.label1 = tk.Label(self.root, text="Will I attend: ")
        self.label1.grid(column=1, row=5)
        self.label2 = tk.Label(self.root, text="")
        self.label2.grid(column=2, row=6, sticky=tk.EW, padx=5, pady=5)

        self.yes_button = tk.Button(self.root, text="YES", command=self.answer1)
        self.yes_button.grid(column=1, row=10, sticky=tk.E, padx=5, pady=5)
        self.maybe_button = tk.Button(self.root, text="MAYBE", command=self.answer2)
        self.maybe_button.grid(column=2, row=10, sticky=tk.E, padx=5, pady=5)
        self.no_button = tk.Button(self.root, text="NO", command=self.answer3)
        self.no_button.grid(column=3, row=10, sticky=tk.E, padx=5, pady=5)
        self.root.mainloop()

    def answer1(self):
        self.label2.config(text="Yes")

    def answer2(self):
        self.label2.config(text="Maybe")

    def answer3(self):
        self.label2.config(text="No")


Grid()
