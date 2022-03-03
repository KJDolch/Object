"""
Exercise 15 - Ckecks
"""
# create a GUI with: 1 Button, 5 Labels, 5 Check Buttons
# On Button click the current status of the fice Check Buttons should be displayed in the corresponding Label
import tkinter as tk


class Check:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")

        self.label1 = tk.Label(self.root, text="")
        self.label1.pack(side="top")
        self.label2 = tk.Label(self.root, text="")
        self.label2.pack(side="top")
        self.label3 = tk.Label(self.root, text="")
        self.label3.pack(side="top")
        self.label4 = tk.Label(self.root, text="")
        self.label4.pack(side="top")
        self.label5 = tk.Label(self.root, text="")
        self.label5.pack(side="top")

        self.checkValue1 = tk.BooleanVar()
        self.checkValue1.set(True)
        self.check1 = tk.Checkbutton(
            self.root, text="Check Box 1", var=self.checkValue1
        )
        self.check1.pack()
        self.checkValue2 = tk.BooleanVar()
        self.checkValue2.set(True)
        self.check2 = tk.Checkbutton(
            self.root, text="Check Box 2", var=self.checkValue2
        )
        self.check2.pack()
        self.checkValue3 = tk.BooleanVar()
        self.checkValue3.set(True)
        self.check3 = tk.Checkbutton(
            self.root, text="Check Box 3", var=self.checkValue3
        )
        self.check3.pack()
        self.checkValue4 = tk.BooleanVar()
        self.checkValue4.set(True)
        self.check4 = tk.Checkbutton(
            self.root, text="Check Box 4", var=self.checkValue4
        )
        self.check4.pack()
        self.checkValue5 = tk.BooleanVar()
        self.checkValue5.set(True)
        self.check5 = tk.Checkbutton(
            self.root, text="Check Box 5", var=self.checkValue5
        )
        self.check5.pack()

        self.button1 = tk.Button(
            self.root,
            text="Check your input",
            command=self.Print_Check1,
            width=80,
            fg="blue",
            bg="grey",
        )
        self.button1.pack(side="bottom")

        self.root.mainloop()

    def Print_Check1(self):
        Checking1 = self.checkValue1.get()
        Checking2 = self.checkValue2.get()
        Checking3 = self.checkValue3.get()
        Checking4 = self.checkValue4.get()
        Checking5 = self.checkValue5.get()
        if Checking1:
            self.label1.config(text="Check Box is " + str(Checking1))
        else:
            self.label1.config(text="Check Box is " + str(Checking1))
        if Checking2:
            self.label2.config(text="Check Box is " + str(Checking2))
        else:
            self.label2.config(text="Check Box is " + str(Checking2))
        if Checking3:
            self.label3.config(text="Check Box is " + str(Checking3))
        else:
            self.label3.config(text="Check Box is " + str(Checking3))
        if Checking4:
            self.label4.config(text="Check Box is " + str(Checking4))
        else:
            self.label4.config(text="Check Box is " + str(Checking4))
        if Checking5:
            self.label5.config(text="Check Box is " + str(Checking5))
        else:
            self.label5.config(text="Check Box is " + str(Checking5))


Check()
