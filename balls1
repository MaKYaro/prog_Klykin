from tkinter import *
import time
import random

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

position = 0
Score = 0
Error = 0

def draw_circle_with_random_size_and_random_color():
    global x
    x = random.randint(0, 800)
    global y
    y = random.randint(0, 600)
    global r
    r = random.randint(20, 50)
    global x1
    x1 = x + r
    global y1
    y1 = y + r
    root.after(2000, draw_circle_with_random_size_and_random_color)
    canv.delete(ALL)
    colors = ['red', 'black']
    canv.create_oval(x, y, x1, y1, fill=random.choice(colors))
    global Score
    canv.create_text(100, 40, text=Score, font='Arial 25')
    canv.create_text(45, 40, text="Score", font='Arial 25')
    global Error
    canv.create_text(100, 70, text=Error, font='Arial 25')
    canv.create_text(40, 70, text="Error", font='Arial 25')


def inside(event):
    root.after(0, inside)
    global x_mouse
    global x
    global y
    global x1
    global y1
    x_mouse = event.x
    y_mouse = event.y
    if x < x_mouse < x1 and y < y_mouse < y1:
        global position
        position = 1
    else:
        position = 0


def counter():
    root.after(2000, counter)
    global position
    global Error
    if position == 1 :
        global Score
        Score += 1
    else:
        Error += 1
    position = 0



root.bind("<Button 1>",inside)
draw_circle_with_random_size_and_random_color()
counter()
root.mainloop()
