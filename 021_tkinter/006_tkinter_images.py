# Sample Tkinter app
from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
# Adding icon to program top bar
root.iconbitmap('python_icon.ico')

# Create a image variable
image1 = PhotoImage(file='python.png')

# Insert image variable into label
myLabel = Label(root, image=image1)
myLabel.pack()


button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()