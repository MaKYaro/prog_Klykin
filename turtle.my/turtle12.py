import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
number = int(input("Введите n:"))
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


def koh_star1(length):
    """Рисует снежинку Коха с глубиной рекурсии 1"""
    koh1(length)
    t1.right(120)
    koh1(length)
    t1.right(120)
    koh1(length)


def koh_star2(length):
    """Рисует снежинку Коха с глубиной рекурсии 2"""
    koh2(length)
    t1.right(120)
    koh2(length)
    t1.right(120)
    koh2(length)


def koh_star3(length):
    """Рисует снежинку Коха с глубиной рекурсии 3"""
    koh3(length)
    t1.right(120)
    koh3(length)
    t1.right(120)
    koh3(length)


if number == 1:
    koh_star1(length_get)
elif number == 2:
    length_get = length_get/4
    koh_star2(length_get)
elif number == 3:
    length_get = length_get/10
    koh_star3(length_get)
else:
    print("Невозможно")






