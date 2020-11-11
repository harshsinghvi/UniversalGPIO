import openwrtRPiGPIO as GPIO
from time import sleep

pin=GPIO.pin(2,GPIO.OUTPUT)

while(1):
    pin.write(1)
    sleep(2000)
    pin.write(0)


