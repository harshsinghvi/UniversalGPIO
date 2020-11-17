import os
import re
import os.path  
import sys 

INPUT="in"
OUTPUT="out"
IN="in"
OUT="out"

ON=1
OFF=0
HIGH=1
LOW=0

class invalidPinNumber(Exception):
    pass

class invalidMode(Exception):
    pass

class invalidDataType(Exception):
    pass

class invalidState(Exception):
    pass

class KernelError(Exception):
    pass

class fileIOError(Exception):
    pass

class illegalUseOfClassMethod(Exception):
    pass

class pin():
    ## _pin _mode _state _reverse_state _initial_state 

    def __init__(self,pin,mode,initial_state=0,reverse_state=False):  # check pin status and availability 
        self.__system__init__()

        if type(pin)==type(0):
            self._pin=pin+self._base
        else:
            raise invalidPinNumber(str(pin)+" is invalid pin Number ")
            sys.exit()
        if mode == INPUT or mode==OUTPUT:
            self._mode=mode
        else:
            raise invalidMode("Invalid mode Name:"+mode+"\n Use UniversalGPIO.GPIO.INPUT or UniversalGPIO.GPIO.OUTPUT")
            sys.exit()
        if(initial_state == 0 or initial_state ==1 ):
            self._state=initial_state
        else:
            raise invalidState("State can either be 1 / 0 or True / False ")
            sys.exit()
        if reverse_state == True or reverse_state ==False:
            self._reverse_state=reverse_state
        else: 
            raise invalidDataType("reverse_state Parameter can either be 1 / 0 or True / False ")
        try:
            self.__gpio__init__()
        except: 
            raise invalidPinNumber("Check the pin Number for your specific Model/Device")
            sys.exit()

    def __gpio__init__(self):
        try:
            export_file = open("/sys/class/gpio/export",'w')
            export_file.write(str(self._pin))
            export_file.flush()
            export_file.close()

            gpio_direction_file=open("/sys/class/gpio/gpio{}/direction".format(self._pin),'w')
            gpio_direction_file.write(self._mode)
            gpio_direction_file.flush()
            gpio_direction_file.close()

        except OSError:            
            print("Warning: Pin {} Was already in use and is now forced to be used in this program.".format(self._pin))
            self.cleanup()
            self.__gpio__init__()
        except:
            raise fileIOError
            sys.exit()
        if self._mode == OUTPUT:
            self.write(self._state)
        else:
            self.read()

    def __system__init__(self):
        if os.path.isdir("/sys/class/gpio/"):
            gpchipfile=[]
            d=os.listdir("/sys/class/gpio/")
            for i in d:
                f=re.search("^gpiochip.*",i)
                if f != None:
                    gpchipfile.append(int(f.string[8:]))
            base_file=open("/sys/class/gpio/gpiochip"+str(min(gpchipfile))+"/base",'r')
            self._base=int(base_file.read())
            base_file.close()
        else:
            raise KernelError("/sys/class/gpio/ not found: Please check the firmare")

    def __del__(self): 
        os.system("echo "+str(self._pin)+ " > /sys/class/gpio/unexport")

    def cleanup(self):
        try:
            unexport_file = open("/sys/class/gpio/unexport",'w')
            unexport_file.write(str(self._pin))
            unexport_file.flush()
            unexport_file.close()
        except :
            os.system("echo "+str(self._pin)+ " > /sys/class/gpio/unexport")
            raise fileIOError("using os.system() to unexport the pin")

    def write(self,state):
        if self._mode==INPUT:
            raise illegalUseOfClassMethod("The Pin is set INPUT")
            return 1
        if(state==0 or state==1):
            self._state=state
            try:
                gpio_state_file=open("/sys/class/gpio/gpio{}/value".format(str(self._pin)),'w')                
                if self._reverse_state:
                    if self._state:
                        gpio_state_file.write("0")
                    else :
                        gpio_state_file.write("1")
                else:
                    if self._state:
                        gpio_state_file.write("1")
                    else :
                        gpio_state_file.write("0")
                gpio_state_file.flush()
                gpio_state_file.close()
            except: 
                raise fileIOError
                sys.exit()
        else:
            raise invalidState("State can either be 1 / 0 or True / False ")
            sys.exit()

    def high(self):
        return self.write(HIGH)
        
    def low(self):
        return self.write(LOW)

    def state(self):
        if self._mode==INPUT:
            raise illegalUseOfClassMethod("The Pin is set INPUT")
            sys.exit()
        return self._state

    def read(self):
        if self._mode==OUTPUT:
            raise illegalUseOfClassMethod("The Pin is set OUTPUT")
            return 1
        try:
            gpio_state_file=open("/sys/class/gpio/gpio{}/value".format(self._pin),'r')
            read_value=int(gpio_state_file.readline())
            gpio_state_file.close()
        except:
            raise fileIOError
        return read_value


def setup(gpio_pin, mode,initial_state=0,reverse_state=False):
    return pin(gpio_pin,mode,initial_state,reverse_state)
    