import robot
r = robot.rmap()
r.lm('task7')
def task():
	pass
	while r.freeLeft()or r.freeUp():
		if r.freeUp():
			r.up();
		if r.freeLeft():
			r.left();
	r.down(3);
	r.right(4);
	while not r.freeUp():
		r.paint();
		r.right();
r.start(task)
