# Documentation https://docs.python.org/3/library/tk.html
# Sample Tkinter app
# * imports all classes from library
import tkinter.colorchooser
from tkinter import *

# This has to go first. It creates a window.
root = Tk()

# Title message on top of the app
root.title('This is sample app made by tkinter')

# Adding specific size to window
root.geometry('400x400')

# Creating a Label widget with text.
myLabel = Label(root, text="Hello world!")
myLabel.pack()
# colour = tkinter.colorchooser.askcolor()
# print(colour)

# This has to go last. It puts program into loop.
root.mainloop()
