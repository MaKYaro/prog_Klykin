import robot
r = robot.rmap()
r.lm('task4')

def task():
    while r.freeUp():
        r.up()
    while r.freeRight():
        r.right()
    r.down()
    r.left()
    for x in range(5):
        r.paint()
        r.down()
        r.down()
        r.paint()
        r.down()
        r.down()
        r.paint()
        r.left()
        r.up()
        r.up()
        r.up()











r.start(task)
