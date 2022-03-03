"""
Exercise 17 - List Box
"""
# create a GUI with a List Box: First single selection
# display the chosen entries in a label: first with bind
import tkinter as tk


class ListBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.resizable(False, False)  # size can't be changed
        self.root.title("Week")
        self.langs = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        self.langs_var = tk.StringVar(value=self.langs)
        self.listbox = tk.Listbox(self.root, listvariable=self.langs_var, height=7,)
        self.listbox.bind("<<ListboxSelect>>", self.items_selected)
        self.listbox.pack()
        self.root.mainloop()

    def items_selected(self, event):
        selected_index = self.listbox.get(self.listbox.curselection())
        print("You selected:", selected_index)


ListBox()
