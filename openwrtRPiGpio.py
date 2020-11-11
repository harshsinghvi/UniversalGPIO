import os
import re
import os.path  

INPUT="in"
OUTPUT="out"
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
            exit()
        if mode == INPUT or mode==OUTPUT:
            self._mode=mode
        else:
            raise invalidMode("Invalid mode Name:"+mode+"\n Use openwrtRPiGpio.INPUT or openwrtRPiGpio.OUTPUT")
            exit()
        if(initial_state == 0 or initial_state ==1 ):
            self._state=initial_state
        else:
            raise invalidState("State can either be 1 / 0 or True / False ")
            exit()
        if reverse_state == True or reverse_state ==False:
            self._reverse_state=reverse_state
        else: 
            raise invalidDataType("reverse_state Parameter can either be 1 / 0 or True / False ")
        try:
            self.__gpio__init__()
        except: 
            raise invalidPinNumber("Check the pin Number for your specific Model/Device")
            exit()


    def __gpio__init__(self):
        try:
            export_file = open("/sys/class/gpio/export",'w')
            export_file.write(str(self._pin))
            export_file.flush()

            gpio_direction_file=open("/sys/class/gpio/gpio{}/direction".format(self._pin),'w')
            gpio_direction_file.write(self._mode)
            gpio_direction_file.flush()
        except OSError:            
            print("Warning: Pin {} Was already in use and is now forced to be used in this program.".format(self._pin))
            self.cleanup()
            self.__gpio__init__()
        except:
            raise fileIOError
            exit()


        self.__pinOperation()

    def __system__init__(self):
        if os.path.isdir("/sys/class/gpio/"):
            gpchipfile=[]
            d=os.listdir("/sys/class/gpio/")
            for i in d:
                f=re.search("^gpiochip.*",i)
                if f != None:
                    gpchipfile.append(int(f.string[8:]))

            self._base=int(open("/sys/class/gpio/gpiochip"+str(min(gpchipfile))+"/base",'r').read())
        else:
            raise KernelError("/sys/class/gpio/ not found: Please check the firmare")

    def __del__(self): 
        self.cleanup()
    
    def __pinOperation(self):
        if self._state==OUTPUT:
            try:
                gpio_state_file=open("/sys/class/gpio/gpio{}/value".format(self._pin),'w')                
                if self._reverse_state:
                    gpio_state_file.write(str(not self._state))
                else:
                    gpio_state_file.write(str(self._state))
                gpio_state_file.flush()
            except: 
                raise fileIOError
                exit()
            return 0
        if self._state==INPUT:
            try:
                gpio_state_file=open("/sys/class/gpio/gpio{}/value".format(self._pin),'r')
                read_value=int(gpio_direction_file.readline())
                gpio_direction_file.close()
            except:
                raise fileIOError
                exit()
            return read_value     

    def cleanup(self):
        try:
            unexport_file = open("/sys/class/gpio/unexport",'w')
            unexport_file.write(str(self._pin))
            unexport_file.flush()
        except:
            raise fileIOError
            exit()

    def write(self,state):
        if self._mode==INPUT:
            raise illegalUseOfClassMethod("The Pin is set INPUT")
            exit()
        if(state==0 or state==1):
            self._state=state
            self.__pinOperation()
            return 0
        else:
            raise invalidState("State can either be 1 / 0 or True / False ")
            exit()

    def high():
        self._state=1
        return self.__pinOperation()
        
    def low():
        self._state=0
        return self.__pinOperation()

    def state(self):
        if self._mode==INPUT:
            raise illegalUseOfClassMethod("The Pin is set INPUT")
            exit()
        return self._state

    def read(self):
        if self._mode==OUTPUT:
            raise illegalUseOfClassMethod("The Pin is set OUTPUT")
            exit()
        return self.__pinOperation()