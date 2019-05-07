import pyfirmata
pin = 13
port = 'COM3'
board = pyfirmata.Arduino(port)
board.digital[pin].write(1)
board.digital[pin].write(0)
board.digital[pin].read()