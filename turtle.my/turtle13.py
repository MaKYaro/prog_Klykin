import turtle


def min(step_length, recursion_depth):
    """Draw Minkovsky`s curve with depth of recursion 1"""
    if recursion_depth > 2:
        t1.forward(step_length)
        return
    min(step_length/4, recursion_depth + 1)
    t1.left(90)
    min(step_length/4, recursion_depth + 1)
    t1.right(90)
    min(step_length/4, recursion_depth + 1)
    t1.right(90)
    min(step_length/4, recursion_depth + 1)
    min(step_length/4, recursion_depth + 1)
    t1.left(90)
    min(step_length/4, recursion_depth + 1)
    t1.left(90)
    min(step_length/4, recursion_depth + 1)
    t1.right(90)
    min(step_length/4, recursion_depth + 1)


t1 = turtle.Turtle()
t1.shape('turtle')
t1.penup()
t1.goto(-200, 0)
t1.pendown()
min(500, 1)






