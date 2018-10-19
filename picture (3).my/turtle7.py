import turtle
t1=turtle.Turtle()
t1.shape('turtle')

def circle_l(L:float, N:int):
    """Рисует окрудность с поворотом влево"""
    for step in range(N):
        t1.forward(L)
        t1.left(360/N)
def circle_r(L:float, N:int):
    """Рисует окрудность с поворотом вправо"""
    for step in range(N):
        t1.forward(L)
        t1.right(360/N)
circle_l(2, 100)
circle_r(2, 100)
t1.left(60)
circle_l(2, 100)
circle_r(2, 100)
t1.left(60)
circle_l(2, 100)
circle_r(2, 100)


