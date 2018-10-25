import robot
r = robot.rmap()
r.lm('task6')

def task():
    x = int(input("Enter letter width: "))
    y = int(input("Enter letter height: "))
    if x > 24 or y > 24 or x == 2:
        print("Error")
    else:
        if x-2*(x//2)<1:
            r.paint()
            r.down()
            r.paint()
            for w in range(x//2-1):
                r.right()
                r.paint()
            for h in range(y-2):
                r.down()
                r.paint()
            r.right()
            r.paint()
            for h in range(y-2):
                r.up()
                r.paint()
            for w in range(x//2-1):
                r.right()
                r.paint()
            r.up()
            r.paint()
            for x in range(x-1):
                r.left()
                r.paint()
        else:
            for w in range(x//2):
                r.paint()
                r.right()
            for h in range(y-1):
                r.down()
                r.paint()
            r.up(y-1)
            r.paint()
            for w in range(x//2):
                r.right()
                r.paint()
                
                
r.start(task)
