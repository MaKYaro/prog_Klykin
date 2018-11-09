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
<<<<<<< HEAD
r.start(task)











	#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
=======
r.start(task)
>>>>>>> 8afefbe62300179eeb3bd0b3ff88f7686558258d
