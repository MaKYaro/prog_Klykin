import robot
r = robot.rmap()
r.lm('task3')

def task():
    for x in range(3):
        r.right()
        r.right()
        r.down()
        r.up()
    r.right()
    r.right()







r.start(task)
