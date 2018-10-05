import turtle
t1=turtle.Turtle()
t1.shape('turtle')
L=20
N=2
def prop_polyg(L: float, N: int):
    """Рисует правильный N-угольник со стороной L"""
    t1.left(180-180*(N-2)/N/2)
    t1.forward(L)
    for engle in range(N-1):
        t1.left(360/N)
        t1.forward(L)
for fig in range(10):
    L+=4
    N+=1
    t1.pendown()
    prop_polyg(L, N)
    t1.right(180*(N-2)/N/2)
    t1.penup()
    t1.forward(L/4)

