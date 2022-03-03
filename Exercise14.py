"""
Exercise 14 - Options Menu
"""
# create three menus: two should contain at least seven colors, one should contain at least seven Countries
# use functions to change the background color, text color of Label and the text displayed in that label corresponding to the chosen option
import tkinter as tk


class Options:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.label2 = tk.Label(text="Text color")
        self.label2.pack(side="top")
        self.var1 = tk.StringVar()
        self.var1.set("snow")
        self.menu1 = tk.OptionMenu(
            self.root,
            self.var1,
            "light blue",
            "lawn green",
            "pale turquoise",
            "sienna1",
            "gold4",
            "orange4",
            "black",
            command=self.display_selected1,
        )
        self.menu1.pack(side="top")
        self.label3 = tk.Label(text="Background color")
        self.label3.pack(side="top")
        self.var2 = tk.StringVar()
        self.var2.set("snow")
        self.menu2 = tk.OptionMenu(
            self.root,
            self.var2,
            "light blue",
            "lawn green",
            "pale turquoise",
            "sienna1",
            "gold4",
            "orange4",
            "black",
            command=self.display_selected2,
        )
        self.menu2.pack(side="top")
        self.label4 = tk.Label(text="Countries")
        self.label4.pack(side="top")
        self.var3 = tk.StringVar()
        self.var3.set("Countries")
        self.menu3 = tk.OptionMenu(
            self.root,
            self.var3,
            "Germany",
            "France",
            "Switzerland",
            "Sweden",
            "Iceland",
            "USA",
            "Ireland",
            command=self.display_selected3,
        )
        self.menu3.pack(side="top")

        self.label1 = tk.Label(
            self.root, text=self.var3.get(), bg=self.var2.get(), fg=self.var1.get()
        )
        self.label1.pack(side="bottom")

        self.root.mainloop()

    def display_selected1(self, choice):
        choice = self.var1.get()
        print(choice)
        self.label1.config(fg=choice)

    def display_selected2(self, choice):
        self.label1.config(bg=self.var2.get())

    def display_selected3(self, choice):
        choice = self.var3.get()
        print(choice)
        self.label1.config(text=choice)


Options()
