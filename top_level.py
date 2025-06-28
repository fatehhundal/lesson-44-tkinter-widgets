from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def open():
    global myimage
    myimage = ImageTk.PhotoImage(Image.open("forest.png"))
    top = Toplevel()
    top.geometry("300x400")
    Button(top, text="Close window", command=top.destroy).pack()
    Label(top, image=myimage).pack()
root.geometry("300x400")
Button(root, text="Open second window", command=open).pack()
root.mainloop()