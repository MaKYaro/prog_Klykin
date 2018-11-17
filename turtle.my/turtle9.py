import turtle
t1 = turtle.Turtle()
t1.shape('turtle')


def circle_r(length: float, number: float):
    """Рисует окрудность с поворотом вправо"""
    for step in range(number):
        t1.forward(length)
        t1.right(180/number)


t1.left(90)


for numbers in range(3):
    circle_r(1, 200)
    circle_r(0.4, 100)



