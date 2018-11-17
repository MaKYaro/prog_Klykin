import turtle
t1 = turtle.Turtle()
length = 10

for step in range(6):
    for x in range(4):
        t1.forward(length)
        t1.left(90)
    t1.right(180)
    t1.penup()
    t1.forward(5)
    t1.left(90)
    t1.penup()
    t1.forward(5)
    t1.left(90)
    length += 10
    t1.pendown()


