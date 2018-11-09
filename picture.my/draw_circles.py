from tkinter import *
import random

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

def left_click(event):
    x = event.x
    y = event.y
    r = x + 40
    r1 = y + 40
    colors = ['red', 'black']
    canv.create_oval(x, y, r, r1, fill=random.choice(colors))

def right_click(event):
    canv.delete(ALL)

canv.bind('<Button-1>', left_click)
canv.bind('<Button-3>', right_click)

mainloop()