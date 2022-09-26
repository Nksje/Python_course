from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
root.geometry('400x400')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

menu_list = ['Monday',
             'Tuesday',
             'Wednesday',
             'Thursday',
             'Friday',
             'Saturday',
             'Sunday']

# Drop down menu
clicked = StringVar()
clicked.set('Monday')
# dropdown = OptionMenu(root, clicked, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
dropdown = OptionMenu(root, clicked, *menu_list)
dropdown.pack()

myButton = Button(root, text='Show selection', command=show).pack()

root.mainloop()