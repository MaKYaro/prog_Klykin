import turtle
t1=turtle.Turtle()
t1.shape('turtle')
n=int(input("Введите n:"))
L=100
t1.penup()
t1.goto(-200, 0)
t1.pendown()
def levi1(L: float):
    t1.left(45)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)
def levi2(L: float):
    t1.left(45)
    levi1(L)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)
def levi3(L: float):
    t1.left(45)
    levi2(L)
    t1.forward(L)
    t1.right(90)
    t1.forward(L)

if n==1:
    levi1(L)
elif n==2:
    L=L/4
    levi2(L)
elif n==3:
    L=L/10
    levi3(L)
else:
    print("Impossible")






