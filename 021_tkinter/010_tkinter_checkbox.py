from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
root.geometry('400x400')

def show_check_status():
    myLable = Label(root, text=var.get()).pack()


# Using IntVar checkbox
var = IntVar()
chk_box = Checkbutton(root, text="Check me", variable=var).pack()

# Using StringVar checkbox
var = StringVar()
chk_box = Checkbutton(root, text="Check me", variable=var, onvalue='ON', offvalue='OFF')
# chk_box.deselect()  # Needs to escape glitch with selected checkbox
chk_box.pack()

myLable = Label(root, text=var.get()).pack()

myButton = Button(root, text='Show check status', command=show_check_status).pack()

root.mainloop()