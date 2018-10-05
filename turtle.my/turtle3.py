import turtle
t1=turtle.Turtle()
L=10

for step in range(6):
    for x in range(4):
        t1.forward(L)
        t1.left(90)
    t1.right(180)
    t1.penup()
    t1.forward(5)
    t1.left(90)
    t1.penup()
    t1.forward(5)
    t1.left(90)
    L += 10
    t1.pendown()


