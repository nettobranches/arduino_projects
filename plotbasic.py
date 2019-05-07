from matplotlib import pyplot
import random

x =  range(0,25)
y = [random.randint(0,100) for r in range(0,25)]

fig1 = pyplot.figure()
pyplot.plot(x,y,'-')
pyplot.title('First plot - random integers')
pyplot.xlabel('x axis')
pyplot.ylabel('y axis')

pyplot.show()