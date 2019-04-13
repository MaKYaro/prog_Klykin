import numpy as np
import matplotlib.pyplot as plt
import time

c = 30000

def python_a(n):
    start = time.time()
    X = n
    Y = n
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - start

def numpy_a(n):
    start = time.time()
    X = n
    Y = n
    Z = X + Y
    return time.time() - start

x = np.arange(1, c, 10)
plt.plot(x, python_a(x)-numpy_a(x) )
plt.show()