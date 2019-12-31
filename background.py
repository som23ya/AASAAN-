import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.resizable(width=False, height=False)
root.wm_attributes("-topmost", 1)

imgpath = 'back.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=photo)


root.mainloop()