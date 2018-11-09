from tkinter import *
import time
import random

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)



def draw_circle_with_random_size_and_random_color():
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    r = random.randint(20, 50)
    x1 = x + r
    y1 = y + r
    root.after(500, draw_circle_with_random_size_and_random_color)
    canv.delete(ALL)
    colors = ['red', 'black']
    canv.create_oval(x, y, x1, y1, fill=random.choice(colors))

root.after_idle(draw_circle_with_random_size_and_random_color)
root.mainloop()