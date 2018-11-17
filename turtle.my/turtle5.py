import turtle
t1 = turtle.Turtle()
L = 10
for step in range(15):
    for x in range(2):
        t1.forward(L)
        t1.left(90)
    L += 10


