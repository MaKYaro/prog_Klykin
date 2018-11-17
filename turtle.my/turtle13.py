import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
number_get = int(input("Введите n:"))
length_get = 100
t1.penup()
t1.goto(-200, 0)
t1.pendown()


def min1(length: float):
    """Draw Minkovsky`s curve with depth of recursion 1"""
    t1.forward(length)
    t1.left(90)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)
    t1.forward(length)
    t1.left(90)
    t1.forward(length)
    t1.left(90)
    t1.forward(length)
    t1.right(90)
    t1.forward(length)


def min2(length: float):
    """Draw Minkovsky`s curve with depth of recursion 2"""
    min1(length)
    t1.left(90)
    min1(length)
    t1.right(90)
    min1(length)
    t1.right(90)
    min1(length)
    min1(length)
    t1.left(90)
    min1(length)
    t1.left(90)
    min1(length)
    t1.right(90)
    min1(length)


def min3(length: float):
    """Draw Minkovsky`s curve with depth of recursion 3"""
    min2(length)
    t1.left(90)
    min2(length)
    t1.right(90)
    min2(length)
    t1.right(90)
    min2(length)
    min2(length)
    t1.left(90)
    min2(length)
    t1.left(90)
    min2(length)
    t1.right(90)
    min2(length)


if number_get == 1:
    min1(length_get)
elif number_get == 2:
    length_get = length_get/4
    min2(length_get)
elif n == 3:
    length_get = length_get/10
    min3(length_get)
else:
    print("Impossible")






