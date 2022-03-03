"""
Exercise 13 - Text fields
"""
# create a GUI that consists of a text field, five buttons and two labels
# the buttons should be able to:
# - insert some text into your text field (one at the beginning and one at the end)
# - clear the whole text field
# - print out the text into the terminal
# - display how many characters the current text has in Creating_Labels

# the second label should be used to display which button was pressed (just add a self.label2.config(text="You pressed Button ...") to your functions)
import tkinter as tk


class Exercise:
    def __init__(self):
        self.root = tk.Tk()
        self.text1 = tk.Text(self.root, spacing1=2, spacing2=2, spacing3=2)
        self.text1.pack(side="top")

        self.button1 = tk.Button(
            self.root, text="insert text at the beginning", command=self.Text_insert_b
        )
        self.button1.pack()

        self.button2 = tk.Button(
            self.root, text="insert text at the end", command=self.Text_insert_e
        )
        self.button2.pack()

        self.button3 = tk.Button(
            self.root, text="clear text field", command=self.Text_clear
        )
        self.button3.pack()

        self.button4 = tk.Button(
            self.root, text="prints text to terminal", command=self.Text_print
        )
        self.button4.pack()

        self.button5 = tk.Button(
            self.root,
            text="Display the number of the current characters",
            command=self.Text_count,
        )
        self.button5.pack()

        self.label1 = tk.Label(self.root, text="")
        self.label1.pack(side="bottom")

        self.label2 = tk.Label(self.root, text="the last button pressed")
        self.label2.pack()

        self.root.mainloop()

    def Text_clear(self):
        self.label1.config(text="")
        self.text1.delete(1.0, "end")
        self.label2.config(text="Button 3 was pressed")

    def Text_print(self):
        self.Content = self.text1.get(1.0, "end")
        print(self.Content)
        print(repr(self.Content))
        self.label2.config(text="Button 4 was pressed")

    def Text_insert_b(self):
        self.text1.insert(1.0, "This is a test\n")
        self.label2.config(text="Button 1 was pressed")

    def Text_insert_e(self):
        self.text1.insert("end", "This is the end\n")
        self.label2.config(text="Button 2 was pressed")

    def Text_count(self):
        self.label1.config(
            text=" Your text has "
            + str(len(self.text1.get(1.0, "end-1c")))
            + " characters"
        )
        self.label2.config(text="Button 5 was pressed")


Exercise()
