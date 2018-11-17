import turtle
t1 = turtle.Turtle()
s = 0.1
for number in range(15):
    for step in range(100):
        t1.forward(s)
        t1.right(1.8)
    s += 0.1
