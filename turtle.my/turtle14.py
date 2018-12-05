import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
number_get = int(input("Введите n:"))
length_get = 100
t1.penup()
t1.goto(-200, 0)
t1.pendown()


def levi1(length: float):
    t1.left(45)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)


def levi2(length: float):
    t1.left(45)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)


def levi3(length: float):
    t1.left(45)
    levi2(length)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)


if number_get == 1:
    levi1(length_get)
elif number_get == 2:
    length_get = length_get/4
    levi2(length_get)
elif number_get == 3:
    length_get = length_get/10
    levi3(length_get)
else:
    print("Impossible")






