from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()


slide_var_1 = StringVar()
slide_var_2 = StringVar()
def slide():
    slide_var_1.set(horizontal.get())
    slide_var_2.set(vertical.get())

my_label_1 = Label(root, textvariable=slide_var_1)
my_label_1.pack()
my_label_2 = Label(root, textvariable=slide_var_2)
my_label_2.pack()


my_button = Button(root, text='Click me', command=slide).pack()
root.mainloop()