from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="My name is Roman")
myLabel3 = Label(root, text="I am 33 years old")
myLabel4 = Label(root, text="I like discgolf")

# # Position two items on different rows
# # Also label stays in the corner
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

# # myLabel1 will move to the right side
# # also keeps place when window is resized
# myLabel1.grid(row=0, column=1)
# myLabel2.grid(row=1, column=0)

# Grid places labels relative to each other
# what means that there must be something between
# columns or row to position label further
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()