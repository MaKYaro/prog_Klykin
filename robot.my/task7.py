import robot
r = robot.rmap()
r.lm('task7')

def task():

r.start(task)
i=0
while r.freeDown():
    r.right()
while not r.freeDown() and r.freeRight():
    i=i+1
    r.right()
if i>1:
    if r.freeDown():
        r.down()
        r.right(i)
        r.paint(i)
    else:
        r.left(i)
        r.down()
        r.right(i)
        r.paint(i)
else :
    while r.freeLeft():
        r.left()
if r.freeDown():
    r.down()
else:
    while not r.freeDown():
        r.right()
    r.down