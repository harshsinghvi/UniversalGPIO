# 🔮 UniversalGPIO.GPIO

Universal Module to comminucating to GPIO Pins of Any kind Supported Device (Linux Kernel and GPIO Pins on Harware). This Module enables us to Interface with the GPIO Pins of devices and gives the code reusability between Different Devices.

## ➕ Creating A GPIO Pin Object

To communicate with the GPIO Pins on your Device, you first need to instantiate a Pin. The easiest way to do that is by calling the function setup(). It can also be configured manually by instantiating a Pin class.

### 📌 setup()

> Return a Pin configured to Communicate with the GPIO Pin with the correspondning parameters.

**Parameters :**

- **gpio_pin** (int) - The Pin number which you want to use.

- **mode** (str) - The Pin Mode to communicate direction either input or output. The following Variables can be used:
    1. `UniversalGPIO.GPIO.OUTPUT`    - For output
    1. `UniversalGPIO.GPIO.OUT`       - For output
    1. `UniversalGPIO.GPIO.INPUT`     - For input
    1. `UniversalGPIO.GPIO.IN`        - For input

- **initial_state** (int) - *Default:*`0` *Only if the mode is output else it will be ignored* The state with which you want to initilize the Pin either 1 / 0. The following Variables can be used:
    1. `UniversalGPIO.GPIO.HIGH`   - For on/1
    1. `UniversalGPIO.GPIO.ON`     - For on/1
    1. `UniversalGPIO.GPIO.LOW`    - For off/0
    1. `UniversalGPIO.GPIO.OFF`    - For off/0

- **reverse_state** (bool) - *Default:*`False` Set True if you want to reverse the output state. *Only if the mode is output else it will be ignored*.

**Example:**

```python
>>> import UniversalGPIO.GPIO as GPIO
>>> pin_p0_number=12
>>> pin_p0=GPIO.setup(pin_p0_number, GPIO.OUTPUT)
```

### Variables in the Module

#### For States

- `UniversalGPIO.GPIO.HIGH`
- `UniversalGPIO.GPIO.Low`
- `UniversalGPIO.GPIO.ON`
- `UniversalGPIO.GPIO.OFF`

#### For Mode

- `UniversalGPIO.GPIO.INPUT`
- `UniversalGPIO.GPIO.OUTPUT`
- `UniversalGPIO.GPIO.IN`
- `UniversalGPIO.GPIO.OUT`

## 📍 Pin Reference

### *class* Pin

> A Pin Object for communicating with GPIO Pin.

**Example:**

```python
>>> import UniversalGPIO.GPIO as GPIO
>>> pin_p0_number=12
>>> pin_p0=GPIO.Pin(pin_p0_number, GPIO.OUTPUT, initial_state=0,reverse_state=False)
>>> pin_p0.cleanup()
```

**Parameters :**

- **gpio_pin** (int) - The Pin number which you want to use.

- **mode** (str) - The Pin Mode to communicate direction either input or output. The following Variables can be used:
    1. `UniversalGPIO.GPIO.OUTPUT`    - For output
    1. `UniversalGPIO.GPIO.OUT`       - For output
    1. `UniversalGPIO.GPIO.INPUT`     - For input
    1. `UniversalGPIO.GPIO.IN`        - For input

- **initial_state** (int) - *Default:*`0` *Only if the mode is output else it will be ignored* The state with which you want to initilize the Pin either 1 / 0. The following Variables can be used:
    1. `UniversalGPIO.GPIO.HIGH`   - For on/1
    1. `UniversalGPIO.GPIO.ON`     - For on/1
    1. `UniversalGPIO.GPIO.LOW`    - For off/0
    1. `UniversalGPIO.GPIO.OFF`    - For off/0

- **reverse_state** (bool) - *Default:*`False` Set True if you want to reverse the output state. *Only if the mode is output else it will be ignored*.

#### write()

> For Writing state to the pin. Only use this method if the mode set to output.

- **Returns** (int) : `0` if no errors were found and `1` if there was errors in writing state.

- **Raises** :
  - `illegalUseOfClassMethod` - If called when mode is set to OUTPUT.
  - `fileIOError` - If there are errors in writing state to the kernel.
  - `invalidState` - If the state passed in the Parameter is invalid.

- **Parameters** :
  - **state** (int) - The state which you want to write to the GPIO Pin.

#### high()

> For Writing ON/HIGH state to the pin. Only use this method if the mode set to output.

- **Returns** (int) : `0` if no errors were found and `1` if there was errors in writing state.

- **Raises** :
  - `illegalUseOfClassMethod` - If called when mode is set to OUTPUT.
  - `fileIOError` - If there are errors in writing state to the kernel.

- **Parameters** :

#### low()

> For Writing OF/LOW state to the pin. Only use this method if the mode set to output.

- **Returns** (int) : `0` if no errors were found and `1` if there was errors in writing state.

- **Raises** :
  - `illegalUseOfClassMethod` - If called when mode is set to OUTPUT.
  - `fileIOError` - If there are errors in writing state to the kernel.

- **Parameters** :

#### state()

> For Reading exixting state of the pin. Only use this method if the mode set to output.

- **Returns** (int) : current `state` of the GPIO Pin.

- **Raises** :
  - `illegalUseOfClassMethod` - If called when mode is set to OUTPUT.

- **Parameters** :

#### read()

> For Reading state of the pin. Only use this method if the mode set to input.

- **Returns** (int) : current `state` of the GPIO Pin.

- **Raises** :
  - `illegalUseOfClassMethod` - If called when mode is set to INPUT.
  - `fileIOError` - If there are errors in Reading state to the kernel.

- **Parameters** :

#### cleanup()

> It is recomented to clean the GPIO Pins to tell the kernel that the pins are not in use any more.

- **Returns** : `None`

- **Raises** :
  - `fileIOError` - If there are errors in Reading state to the kernel.

- **Parameters** :
