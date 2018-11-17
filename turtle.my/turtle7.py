import turtle
t1 = turtle.Turtle()
t1.shape('turtle')


def circle_l(length: float, number: int):
    """Рисует окрудность с поворотом влево"""
    for step in range(number):
        t1.forward(length)
        t1.left(360/number)


def circle_r(length: float, number: int):
    """Рисует окрудность с поворотом вправо"""
    for step in range(number):
        t1.forward(length)
        t1.right(360/number)


circle_l(2, 100)
circle_r(2, 100)
t1.left(60)
circle_l(2, 100)
circle_r(2, 100)
t1.left(60)
circle_l(2, 100)
circle_r(2, 100)


