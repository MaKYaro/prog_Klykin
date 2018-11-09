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
        for down in range(2):
            r.down()
        r.paint()
        for down in range(2):
            r.down()
        r.paint()
        r.left()
        for up in range(3):
            r.up()
<<<<<<< HEAD












=======
            
>>>>>>> 8afefbe62300179eeb3bd0b3ff88f7686558258d
r.start(task)
