from tkinter import *
import time

def digital():
    d=time.strftime("%H:%M:%S")
    clock.config(text=d)
    clock.after(200,digital)

root=Tk()
root.title("Digital clock")
root.resizable(0,0)
clock=Label(root,font=('Cambria',50,'bold'),bg='white')
clock.pack()
digital()
root.mainloop()