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


t1 = turtle.Turtle()
t1.shape('turtle')
koh(500, 0)




