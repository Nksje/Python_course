# Sample Tkinter app
# * imports all classes from library
from tkinter import *

# This has to go first. It creates a window.
root = Tk()

# Title message on top of the app
root.title('This is sample app made by tkinter')

# Adding specific size to window
root.geometry('400x400')

var = StringVar()

# Creating a Label widget with text.
user_entry = Entry(root, textvariable=var)
user_entry.place(x=80, y=40)

output_label = Label(root, textvariable=var)
output_label.place(x=80, y=80)

# This has to go last. It puts program into loop.
root.mainloop()