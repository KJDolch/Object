"""
Exercise 18 - Two Scales
"""
# create GUI with two Scales: one horizontal and one vertical
# Display the chosen values of both scales in a label on the click on a button: similar to a coordinate system
import tkinter as tk


class Coordinates:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Coordinates")
        self.v1 = tk.DoubleVar()
        self.scale1 = tk.Scale(
            self.root,
            variable=self.v1,
            from_=1,
            to=100,
            orient="horizontal",
            resolution=0.2,
        )
        self.label1 = tk.Label(self.root, text="Horizontal Scaler")
        self.scale1.pack(anchor="center")
        self.label1.pack()

        self.v2 = tk.DoubleVar()
        self.scale2 = tk.Scale(
            self.root,
            variable=self.v2,
            from_=1,
            to=100,
            orient="vertical",
            resolution=0.2,
        )
        self.label3 = tk.Label(self.root, text="Vertical Scaler")
        self.button2 = tk.Button(
            self.root, text="Display coordinates", command=self.show1, bg="blue"
        )
        self.scale2.pack(anchor="center")
        self.label3.pack()
        self.button2.pack(anchor="center")
        self.label2 = tk.Label(self.root)
        self.label2.pack()

        self.root.mainloop()

    def show1(self):
        sel = (
            "Horizontal = "
            + str(self.v1.get())
            + "\n Vertical Scale Value = "
            + str(self.v2.get())
        )
        self.label2.config(text=sel,)


Coordinates()
