import turtle
t1=turtle.Turtle()
t1.shape('turtle')
n=int(input("Введите n:"))
L=100
t1.penup()
t1.goto(-200, 0)
t1.pendown()
def koh1 (L: float):
    """Рисует кривую Коха с глубиной 1"""
    t1.forward(L)
    t1.left(60)
    t1.forward(L)
    t1.right(120)
    t1.forward(L)
    t1.left(60)
    t1.forward(L)
def koh2 (L: float):
    """Рисует кривую Коха с глубиной 2"""
    koh1(L)
    t1.left(60)
    koh1(L)
    t1.right(120)
    koh1 (L)
    t1.left(60)
    koh1 (L)
def koh3 (L: float):
    """Рисует кривую Коха с глубиной 3"""
    koh2(L)
    t1.left(60)
    koh2(L)
    t1.right(120)
    koh2 (L)
    t1.left(60)
    koh2 (L)
if n==1:
    koh1(L)
elif n==2:
    L=L/4
    koh2(L)
elif n==3:
    L=L/10
    koh3(L)
else:
    print("Невозможно")






