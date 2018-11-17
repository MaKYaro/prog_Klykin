import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
number_get = int(input("Введите n:"))
length_get = 100
t1.penup()
t1.goto(-200, 0)
t1.pendown()


def koh1(length: float):
    """Рисует кривую Коха с глубиной 1"""
    t1.forward(length)
    t1.left(60)
    t1.forward(length)
    t1.right(120)
    t1.forward(length)
    t1.left(60)
    t1.forward(length)


def koh2(length: float):
    """Рисует кривую Коха с глубиной 2"""
    koh1(length)
    t1.left(60)
    koh1(length)
    t1.right(120)
    koh1(length)
    t1.left(60)
    koh1(length)


def koh3(length: float):
    """Рисует кривую Коха с глубиной 3"""
    koh2(length)
    t1.left(60)
    koh2(length)
    t1.right(120)
    koh2(length)
    t1.left(60)
    koh2(length)


if number_get == 1:
    koh1(length_get)
elif number_get == 2:
    length_get = length_get/4
    koh2(length_get)
elif number_get == 3:
    length_get = length_get/10
    koh3(length_get)
else:
    print("Невозможно")






