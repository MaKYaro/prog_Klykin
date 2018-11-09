from tkinter import *
import random
import math
root = Tk()
root.geometry("300x300")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

balls = []
numbers = random.randint(3, 10)
for number in range(numbers):
    r = random.randint(30, 50)
    x = random.randint(50, 250)
    y = random.randint(0, 300)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    colors = ['red', 'black', 'yellow', 'white', 'pink']
    oval = canvas.create_oval(x, y, x+r, y+r, fill=random.choice(colors))
    ball = [x, y, dx, dy, oval]
    balls.append(ball)

def tick_handler():
    for ball in balls:
        x, y, dx, dy, oval = ball
        # Отражение от края холста
        if x < 0:
            dx = -dx; x = 0
        elif x > 300-r:
            dx = -dx
            x = 300-r
        if y < 0:
            dy = -dy
            y = 0
        elif y > 300-r:
            dy = -dy
            y = 300-r
        x = x + dx; y = y + dy
        canvas.move(oval, dx, dy)
        ball[0] = x
        ball[1] = y
        ball[2] = dx
        ball[3] = dy


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler()
    sleep_dt = math.ceil(50*(1/speed))
    root.after(sleep_dt, time_handler)

def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)

speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

# Скорость = 1
speed_scale.set(1);
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()