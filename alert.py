from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! A virus has been found.")

button = Button(root, text="Scan for viruses", command=msg)
button.place(x=40, y=80)

root.mainloop()