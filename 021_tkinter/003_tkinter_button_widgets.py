# Sample Tkinter app
from tkinter import *

# This has to go first. It creates a window.
root = Tk()


def myClick():
    myLabel = Label(root, text="Look I have cliked a button")
    myLabel.pack()


# Creates a button widget, padx and pady resizes the button
# Function in Tkinter is called without ()
myButton = Button(root, text="Click me", padx=50, pady=50, command=myClick, fg='blue', bg='red')
myButton.pack()


# This has to go last. It puts program into loop.
root.mainloop()