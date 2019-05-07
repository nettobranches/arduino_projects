import sys
from matplotlib import pyplot
import pyfirmata
from time import sleep
import numpy as np

port = 'COM3'
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')

pyplot.ion()

pData = [0]*25
fig = pyplot.figue()
pyplot.title("Real-time Potenciometer reading")
ax1 = pyplot.axes()
l1 = pyplot.plot(pData)
pyplot.ylim([0,1])

while True:
	try:
		sleep(1)
		pData.append(float(a0.read()))
		pyplot.ylim([0,1])
		del pData[0]
		l1.set_xdata([i for i in xrange(25)])
		l1.set_ydata(pData)
		pyplot.draw()
	except KeyboardInterrupt:
		board.exit()
		break
