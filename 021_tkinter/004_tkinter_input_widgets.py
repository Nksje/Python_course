# Sample Tkinter app
from tkinter import *

# This has to go first. It creates a window.
root = Tk()

user_entry = Entry(root, width=50, bg='black', fg='white', borderwidth=5)
user_entry.pack()
user_entry.insert(0, 'Please enter your name: ')

# # Will take everything inputted in user_entry into variable
#user_entry.get()

def myClick():
    myLabel = Label(root, text="Hello " + user_entry.get())
    myLabel.pack()

# Creates a button widget, padx and pady resizes the button
# Function in Tkinter is called without ()
myButton = Button(root, text="Enter your name", padx=50, pady=50, command=myClick, fg='blue', bg='red')
myButton.pack()


# This has to go last. It puts program into loop.
root.mainloop()