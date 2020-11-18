# 🔮 UniversalGPIO

Python Library for interfacing GPIO Pins on Linux based Routers, Network Devices, and embedded Devices like Raspberry pi and OpenWRT based Routers.

## Contents

- [Installation](##Installation)
- [Getting Started](##Getting-Started)
- [GPIO Module](GPIO.md)
- [API Module](API.md) 🏗️ (To be Updated Soon)
- [Dignostics and Troubleshooting  Module](dignostics.md) 🚧 (To be Updated Soon)
- [Examples](https://github.com/harshsinghvi/UniversalGPIO/tree/master/examples)

## 💽 Installation

The latest stable version is available on PyPI. Either add `UniversalGPIO` to your requirements.txt file or install with pip:

`pip install UniversalGPIO`

## 🔰 Getting Started

You can interface with GPIO Pins on the supported devices. You can use the `setup()` method in the GPIO Module.

```python
>>> import UniversalGPIO.GPIO as GPIO
>>> pin_out = setup(12,GPIO.OUTPUT)
>>> pin_in = setup(13,GPIO.INPUT)
```

Writing state to the OUTPUT Pin:

```python
>>> pin_out.state(1)
1

# OR

>>> pin_out.high()
1
```

Reading States from the INPUT Pin:

```Python
>>> pin_in.read()
1
```

Cleaning Pins After Use:

```python
>>> pin_out.cleanup()
>>> pin_in.cleanup()
```
