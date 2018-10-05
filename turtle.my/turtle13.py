import turtle
t1=turtle.Turtle()
t1.shape('turtle')
n=int(input("Введите n:"))
L=100
t1.penup()
t1.goto(-200, 0)
t1.pendown()
def min1 (L: float):
    """Draw Minkovsky`s curve with depth of recursion 1"""
    t1.forward(L)
    t1.left(90)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)
    t1.forward(L)
    t1.left(90)
    t1.forward(L)
    t1.left(90)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)
def min2 (L: float):
    """Draw Minkovsky`s curve with depth of recursion 2"""
    min1(L)
    t1.left(90)
    min1(L)
    t1.right(90)
    min1(L)
    t1.right(90)
    min1(L)
    min1(L)
    t1.left(90)
    min1(L)
    t1.left(90)
    min1(L)
    t1.right(90)
    min1(L)
def min3 (L: float):
    """Draw Minkovsky`s curve with depth of recursion 3"""
    min2(L)
    t1.left(90)
    min2(L)
    t1.right(90)
    min2(L)
    t1.right(90)
    min2(L)
    min2(L)
    t1.left(90)
    min2(L)
    t1.left(90)
    min2(L)
    t1.right(90)
    min2(L)

if n==1:
    min1(L)
elif n==2:
    L=L/4
    min2(L)
elif n==3:
    L=L/10
    min3(L)
else:
    print("Impossible")






