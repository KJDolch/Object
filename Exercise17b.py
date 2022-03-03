"""
Exercise 17 - List Box with multiple selections
"""
# create a GUI with a List Box: multiple selections
# display the chosen entries in a label: with the help of a button
import tkinter as tk


class ListBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.root.title("Breakfast")
        self.langs = [
            "Coffee",
            "Tea",
            "Bread",
            "Jam",
            "Honey",
            "Apple",
            "Croissant",
            "Youghrt",
            "Juice",
        ]
        self.langs_var = tk.StringVar(value=self.langs)
        self.listbox = tk.Listbox(
            self.root,
            listvariable=self.langs_var,
            height=9,
            selectmode="multiple",
            selectbackground="blue",
            selectforeground="snow",
            activestyle="dotbox",
        )
        self.button1 = tk.Button(
            self.root, text="Click Me", command=self.items_selected
        )
        self.listbox.pack(fill="both")
        self.button1.pack()
        self.root.mainloop()

    def items_selected(self):
        foodlist = []
        selected_indices = self.listbox.curselection()
        for i in selected_indices:
            index = self.listbox.get(i)
            foodlist.append(index)
        for elem in foodlist:
            print("You selected:", elem)


ListBox()
