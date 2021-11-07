# test omgeving matplot lib
# we gaan proberen een random walk plot te maken van een vergeleiking
# we stellen da x = range(0-1)
# we stellen dat r =range(0-4)
# we stellen da e = random

import random
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

n = 1000

x = numpy.zeros(n)
y = numpy.zeros(n)
z = numpy.zeros(n)

cur = [0, 0, 0]

for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
        z[i] = z[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
        z[i] = z[i - 1] + 1
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
        z[i] = z[i - 1]
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
        z[i] = z[i - 1] - 1

fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes
# ax.scatter(x[-1], y[-1], z[-1], c='b', marker='o')
plt.style.use('seaborn')
plt.plot(x, y, z)
plt.show()






