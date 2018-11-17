import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
length_get = 20
number_get = 2


def prop_polygon(length: float, number: int):
    """Рисует правильный N-угольник со стороной L"""
    t1.left(180-180*(number-2)/number/2)
    t1.forward(length)

    for angle in range(number-1):
        t1.left(360/number)
        t1.forward(length)


for fig in range(10):
    length_get += 4
    number_get += 1
    t1.pendown()
    prop_polygon(length_get, number_get)
    t1.right(180*(number_get-2)/number_get/2)
    t1.penup()
    t1.forward(length_get/4)

