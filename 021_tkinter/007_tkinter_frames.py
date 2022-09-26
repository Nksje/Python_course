from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
root.iconbitmap('python_icon.ico')

frame = LabelFrame(root, text="This is frame", padx=50, pady=50)  # Padding inside frame, text is not compulsory
frame.pack(padx=10, pady=10)  # Padding outside frame

btn = Button(frame, text="Click me")
btn.pack()

# # Grid can be used inside frames. Putting button into root with grid will cause error
# btn = Button(frame, text="Click me").grid(row=0, column=0)
# btn2 = Button(frame, text="Click me too").grid(row=1, column=0)

root.mainloop()