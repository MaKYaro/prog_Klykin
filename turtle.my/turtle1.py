import turtle
t1=turtle.Turtle()

def proper_polygon(N: int, L:float):
    """Write proper polygon with N sides and size's length L"""

    t1.forward(L)
    t1.left(360/N)
for x in range(4):
    proper_polygon(4, 50)


