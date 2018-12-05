import turtle


def koh(step_length, recursion_depth):
    if recursion_depth > 2:
        t1.forward(step_length)
        return
    koh(step_length/3, recursion_depth+1)
    t1.left(60)
    koh(step_length/3, recursion_depth+1)
    t1.right(120)
    koh(step_length/3, recursion_depth+1)
    t1.left(60)
    koh(step_length/3, recursion_depth+1)


def koh_star(step_length, recursion_depth):
    """Рисует снежинку Коха с глубиной рекурсии 1"""
    if recursion_depth > 2:
        t1.forward(step_length)
        return
    koh(step_length, recursion_depth)
    t1.right(120)
    koh(step_length, recursion_depth)
    t1.right(120)
    koh(step_length, recursion_depth)


t1 = turtle.Turtle()
t1.shape('turtle')
t1.penup()
t1.goto(-200, 0)
t1.pendown()
koh_star(100, 0)






