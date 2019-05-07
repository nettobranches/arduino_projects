from pyfirmata import Aduino
from pyfirmata import INPUT, OUTPUT, PWM
from time import sleep

port = 'COM3'

board = Arduino(port)

arduino = {
	'digital': tuple(x for x in range(14)),
	'analog': tuple(x for x in range(6)),
	'pwm':(3,5,6,9,10,11),
	'use_ports': True,
	'disabled': (0,1)
}

nano = {
	'digital': tuple(x for x in range(14)),
	'analog': tuple(x for x in range(8)),
	'pwm':(3,5,6,9,10,11),
	'use_ports': True,
	'disabled': (0,1)
}

# board.setup_layout(arduino)
# assigning models to digital pins
board.digital[13].mode = OUTPUT
board.analog[0].mode = INPUT

#pin mode assignment
ledPin = board.get_pin('d:13:o')
