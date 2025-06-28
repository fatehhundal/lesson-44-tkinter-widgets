from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image")
root.geometry("1000x540")

upload = Image.open("forest.png")
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=500)
label.place(x=120, y=0)
label2 = Label(root, text="This is how you import an image into a Tkinter window")
label2.place(x=230, y=360)

root.mainloop()