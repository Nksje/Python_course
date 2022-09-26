from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('This is sample app made by tkinter')
root.iconbitmap('python_icon.ico')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def clicked():
    messagebox.showinfo('This is popup window', 'Some text inside')

    # If statement to get values from askyesno window
    response = messagebox.askyesno('This is popup window', 'Some text inside')
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()

    # askokcancel will return 1 or 0
    response = messagebox.askokcancel('This is popup window', 'Some text inside')
    Label(root, text=response).pack()


Button(root, text='Click me', command=clicked).pack()



root.mainloop()