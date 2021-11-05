
import threading
import time
import math
import sys
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import datetime
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Variables
mcp = None          # mcp object
chan2 = None        # LDR channel 2 on MCP
chan1 = None        # mcp channel 1 on MCP
button =  23       # BCM PIN Number for button, i.e actual is pin 12 on RaspberryPi

interval = 1        # Time interval      
startTime = 0       # Start Time


# Setup RPi Pins and peripherals
def setup():
    global mcp
    global chan2
    global chan1
    global button
    global startTime

    GPIO.setmode(GPIO.BCM)

    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    
    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 1 and pin 2
    chan1 = AnalogIn(mcp, MCP.P1)
    chan2 = AnalogIn(mcp, MCP.P2)

    # Interrupt
    GPIO.add_event_detect(button, GPIO.FALLING, callback=btn_Interrupt, bouncetime=300)

    
    print("{:<13}{:<20}{:<22}{:}".format("Runtime", "Temp Reading", "Temp","Light Reading"))

    # Start Time 
    startTime = time.time()

    

# Thread Function
def Thread():
    global mcp
    global chan2
    global chan1
    global interval
    global startTime

    x = threading.Timer(interval,Thread)   # thread
    x.daemon = True                             
    x.start()                              # Start Thread

    # Runtime
    runtime = int(time.time()) - int(startTime)
    #  start the current thread 
    print("{:}{:<12}{:<20}{:0.3f} {:<15}{:}".format(runtime,"s",chan1.value, (chan1.voltage - 0.5)*100,"C", chan2.value))
           

# Interrupt
def btn_Interrupt(channel):
    global interval

    start = time.time()
    time.sleep(0.2)

    while GPIO.input(button) == GPIO.LOW:
        time.sleep(0.01)

    isTime = time.time() - start

    # If the button is pressed for more than 8 seconds, time interval is 10s
    if isTime>=8:
        interval = 10

    # If the button is pressed for more than 4 seconds, time interval is 5s
    elif isTime>=4:
        interval = 5

    # Default time interval is 1s
    else:
        interval = 1



if __name__ == "__main__":
    try:
       setup()
       Thread()

       while True:
             pass
      
    # clean GPIO
    except KeyboardInterrupt:
       print("Exiting Program")
       GPIO.cleanup()
   
