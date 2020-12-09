from UniversalGPIO.GPIO import Pin, OUT,IN,ON,OFF
from os import system
from time import sleep

modes = ['out','output','in','input']
states= ['on', 'off', 1, 0, 'high', 'low']

def gpiocontrol(pin, mode, state=0):
    if mode not in modes:
        raise InvalidMode("allowed_modes =['out','output','in','input']")
    if state not in states:
        raise InvalidMode("allowed_STATES =['on', 'off', 1, 0, 'high', 'low']")
    else:
        if state in ['on', 1, 'high']:
            state = 1
        else: 
            state = 0
    system("./scripts/gpiocontrol.sh {} {} {}".format(pin, mode, state))
    
def unexport(pin):
    system("echo "+str(pin)+ " > /sys/class/gpio/unexport")

def blink_one_buy_one(delay_time, start=None, end=None):
    if start == None and end == None:
        system("./scripts/pin_discovery_blink.sh {}".format(delay_time))
    else:
        system("./scripts/pin_discovery_blink.sh {} {} {}".format(delay_time, start, end))

def blink_all(start, end):
    system("./scripts/pin_discovery_blink-all.sh {} {}".format(start, end))
