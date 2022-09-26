from tkinter import *


# Using INT variable in radio buttons
root = Tk()
root.title('This is sample app made by tkinter')
root.iconbitmap('python_icon.ico')

# Defining variable IntVar will tell program that choice value is integer
choice = IntVar()

# Default value can be added with set command
choice.set('2')


def choice_done(value):
    myLabel = Label(root, text=value).pack()

# Variable can be added to radio button in order to call it later
Radiobutton(root, text='Choice 1', variable=choice, value=1).pack()
Radiobutton(root, text='Choice 2', variable=choice, value=2).pack()

# Adding a command to do something while clicked
Radiobutton(root, text='Choice 3', variable=choice, value=3, command=lambda: choice_done(choice.get())).pack()
Radiobutton(root, text='Choice 4', variable=choice, value=4, command=lambda: choice_done(choice.get())).pack()

myLabel = Label(root, text=choice.get()).pack()


root.mainloop()


# # String variable sample
# root = Tk()
# root.title('This is sample app made by tkinter')
# root.iconbitmap('python_icon.ico')
#
# modes = [
#     ('One', 'One'),
#     ('Two', 'Two'),
#     ('Three', 'Three'),
# ]
#
# choice = StringVar()
# choice.set('One')
#
# for text, mode in modes:
#     Radiobutton(root, text=text, variable=choice, value=mode).pack(anchor=W)
#
# def choice_done(value):
#     myLabel = Label(root, text=value).pack()
#
# myLabel = Label(root, text=choice.get()).pack()
#
# myButton = Button(root, text='Click me', command=lambda: choice_done(choice.get())).pack()
#
#
# root.mainloop()