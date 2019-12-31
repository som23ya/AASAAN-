from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

import sys
import os
root = Tk()
root.title("Voice Assistant")
root.geometry('400x400')


def helloCallBack():
    os.system('python voice_assiss.py')

    w = Label(root, text='  ').pack(side='top')

w = Label(root, text='  ').pack(side='top')
w = Label(root, text=' Try wikipedia ').pack(side='top')
w = Label(root, text=' Find a video on youtube ').pack(side='top')
w = Label(root, text=' Save a note').pack(side='top')
w = Label(root, text=' Send an email ').pack(side='top')

w = Label(root, text=' Ajtak news live').pack(side='top')
w = Label(root, text=' Whatsapp kholo ').pack(side='top')

w = Label(root, text=' Google kare what / why / how / kya / kyun').pack(side='top')
w = Label(root, text=' TV chalo kare ').pack(side='top')

w = Label(root, text=' Call  ').pack(side='top')
w = Label(root, text=' What is the time? ').pack(side='top')
w = Label(root, text=' Say BYE BYE to Aasaan').pack(side='top')
w = Label(root, text='  ').pack(side='top')
w = Label(root, text='  ').pack(side='top')
w = Label(root, text='  ').pack(side='top')



Button(root, text = 'Say Something to Aasaan!',command= helloCallBack).pack(side='top')

mainloop()