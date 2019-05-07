#!/usr/bin/python

# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

import sys
from matplotlib import pyplot
import pyfirmata
from time import sleep
import tkinter


def onStartButtonPress():
    while True:
        if flag.get():
            sleep(1)
            a0val = a0.read()
            pData.append(float(a0.read()))
            ledval = a0val * 5* 55
            print(ledval)
            a3.write(ledval)
            pyplot.ylim([0, 1])
            del pData[0]
            l1.set_xdata([i for i in range(25)])
            l1.set_ydata(pData)  # update the data
            pyplot.draw()  # update the plot
            top.update()
        else:
            flag.set(True)
            break


def onPauseButtonPress():
    flag.set(False)


def onExitButtonPress():
    print ("Exiting....")
    onPauseButtonPress()
    board.exit()
    pyplot.close(fig)
    top.quit()
    top.destroy()
    print ("Done.")
    sys.exit()

# Associate port and board with pyFirmata
port = 'COM3'
board = pyfirmata.Arduino(port)

# Using iterator thread to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Assign a role and variable to analog pin 0 
a0 = board.get_pin('a:0:i')
a3 = board.get_pin('d:3:p')

# Tkinter canvas
top = tkinter.Tk()
top.title("Tkinter + matplotlib")

# Create flag to work with indefinite while loop
flag = tkinter.BooleanVar(top)
flag.set(True)

pyplot.ion()

pData = [0.0] * 25
fig = pyplot.figure()
pyplot.title('Potentiometer')
ax1 = pyplot.axes()
l1, = pyplot.plot(pData)
pyplot.ylim([0, 1])

# Create Start button and associate with onStartButtonPress method
startButton = tkinter.Button(top,
                             text="Start",
                             command=onStartButtonPress)
startButton.grid(column=1, row=2)

# Create Stop button and associate with onStopButtonPress method
pauseButton = tkinter.Button(top,
                             text="Pause",
                             command=onPauseButtonPress)
pauseButton.grid(column=2, row=2)

# Create Exit button and destroy the window
exitButton = tkinter.Button(top,
                            text="Exit",
                            command=onExitButtonPress)
exitButton.grid(column=3, row=2)

top.mainloop()