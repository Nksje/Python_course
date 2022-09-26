# Positioning and grid system
from tkinter import *

# This has to go first. It creates a window.
root = Tk()

# Creating a Label widget with text.
myLabel1 = Label(root, text="Hello world!")

# Lets add more labels
myLabel2 = Label(root, text="Second label")
myLabel3 = Label(root, text="Second label")

# Positioning in grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=4)


# This has to go last. It puts program into loop.
root.mainloop()