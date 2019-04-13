import math
import pylab
from matplotlib import mlab

t_list = mlab.frange(-20, 20, 0.01)

pylab.ion()

for n in range(50):
    y_list = [math.cos(2 * t) for t in t_list]
    x_list = [math.sin(t + n) for t in t_list]
    pylab.clf()
    pylab.plot(x_list, y_list)
    pylab.draw()
    pylab.pause(0.1)


pylab.close()