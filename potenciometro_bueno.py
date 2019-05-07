from pyfirmata import Arduino, util
from time import sleep
import os

port = 'COM3'
board = Arduino(port)
sleep(5)
it = util.Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')

try:
	while True:
		p = a0.read()
		print(p)
except KeyboardInterrupt:
	board.exit()
	os._exit()
