# Sample Tkinter app
from tkinter import *

# This has to go first. It creates a window.
root = Tk()
root.title('Simple Calculator')

user_entry = Entry(root, width=35, borderwidth=5)
# Column span will expand widget to 3 columns
user_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# # Will take everything inputted in user_entry into variable
#user_entry.get()

def get_squares(number):
    user_entry.delete(0, END)  # Will delete contents of user_entry field
    user_entry.insert(0, int(number) ** 2)  # Will insert number square into user_entry field

# Creates a button widget, padx and pady resizes the button
# Function in Tkinter is called without ()
myButton = Button(root, text="Count squares", command= lambda: get_squares(user_entry.get()), fg='blue', bg='red')
myButton.grid(row=1, column=0)

# This has to go last. It puts program into loop.
root.mainloop()