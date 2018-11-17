import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
length_get = 100
number_get = 100


def circle_l(length: float, number: int):
    """Рисует окрудность с поворотом влево"""
    for step in range(number):
        t1.forward(length)
        t1.left(number)


def circle_r(length: float, number: int):
    """Рисует окрудность с поворотом вправо"""
    for step in range(number):
        t1.forward(length)
        t1.right(360/number)


t1.left(90)


for numbers in range(10):
    circle_l(length_get, number_get)
    circle_r(length_get, number_get)
    length_get += 0.4
    number_get += 2


