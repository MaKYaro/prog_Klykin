import turtle
t1=turtle.Turtle()
t1.shape('turtle')
L=2
N=100
def circle_l(L:float, N:int):
    """Рисует окрудность с поворотом влево"""
    for step in range(N):
        t1.forward(L)
        t1.left(N)
def circle_r(L:float, N:int):
    """Рисует окрудность с поворотом вправо"""
    for step in range(N):
        t1.forward(L)
        t1.right(360/N)
t1.left(90)
for number in range(10):
    circle_l(L, N)
    circle_r(L, N)
    L+=0.4
    N+=2


