"""
Exercise 19 - Message Boxes
"""
# create a GUI with three message Boxes
# should have different formats
# should contain texts of different lengths
import tkinter as tk


class Message:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Start in den Tag")
        self.m1 = "Guten Morgäääääääääähn!"
        self.msg1 = tk.Message(self.root, text=self.m1)
        self.msg1.config(
            bg="LightSteelBlue1",
            fg="yellow",
            width=1000,
            font=("calibri", 24, "italic"),
        )
        self.msg1.pack(side="top")

        self.m2 = "Starte den Tag mit viel Elan, stets guter Laune und Humor."
        self.msg2 = tk.Message(self.root, text=self.m2)
        self.msg2.config(bg="magenta3", fg="gray61", font=("calibri", 24, "bold"))
        self.msg2.pack()

        self.m3 = "Und im Zweifel:\n Esse Schokolade!"
        self.msg3 = tk.Message(self.root, text=self.m3)
        self.msg3.config(
            bg="seashell3", fg="chocolate3", font=("calibri", 40), width=1000
        )
        self.msg3.pack(side="bottom")

        self.root.mainloop()


Message()
