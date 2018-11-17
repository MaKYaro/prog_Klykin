import turtle
t1 = turtle.Turtle()


def proper_polygon(n: int, l: float):
    """Write proper polygon with n sides and size's length l"""

    t1.forward(l)
    t1.left(360/n)


for x in range(4):
    proper_polygon(4, 50)


