import turtle
t1=turtle.Turtle()
t1.shape('turtle')
L=2
N=100
def circle_r(L:float, N:float):
    """Рисует окрудность с поворотом вправо"""
    for step in range(N):
        t1.forward(L)
        t1.right(180/N)
t1.left(90)
for number in range(3):
    circle_r(1, 200)
    circle_r(0.4, 100)



