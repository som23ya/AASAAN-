from tkinter import *
from tkinter.ttk import *
import sys
import os
# creating tkinter window
root = Tk()
root.title("Aasaan- your interactive help")
root.geometry('1000x1000')
# Adding widgets to the root window
#Label(root, text='Aasaan', font=(
  #  'Verdana', 45)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"aasaan.png")

# here, image option is used to
# set image on button
Button(root, text='Aasaan!', image=photo).pack(side=TOP)

def helloCallBack():
    os.system('python voice_tkinter.py')
Button(root, text = 'Personal Voice Assistant',command= helloCallBack).pack(side='left')

btn = Button(root, text='Search \nMy Picture', command=root.destroy)
btn.pack(side='left', fill=Y)

btn = Button(root, text='Gesture(hand) \nControl ',
             command=root.destroy)
btn.pack(side='left', fill=Y)
Button(root, text = 'Search \nHandwritten Message').pack(side='left', fill=Y )

Button(root, text = 'Voice to Letter ').pack(side='left', fill=Y )

btn = Button(root, text='Talk with Friends',)

btn.pack(side='left', fill=Y)
Button(root, text = 'Know More about\n Aasaan \n via Chatbot').pack(side='right', fill=Y )

Button(root, text = 'Developers').pack(side='right', fill=Y )


mainloop()
