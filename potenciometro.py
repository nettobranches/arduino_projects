import pyfirmata
from time import sleep

def blinkLED(pin, message):
	print(message)
	board.digital[pin].write(1)
	sleep(1)
	board.digital[pin].write(0)

	sleep(1)

port = 'COM3'
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

pirPin = board.get_pin('d:7:i')
redPin = 12
greenPin = 13

while True:
	value = pirPin.read()
	print('pin7', pirPin)
	while value is None:
		pass

	if vaule is True:
		blinkLED(redPin, 'motion detected')
	else:
		blinkLED(greenPin, 'no motion detected')

board.exit()