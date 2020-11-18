# 🔮 UniversalGPIO

Python Library for interfacing GPIO Pins on Linux based Routers, Network Devices, and embedded Devices like Raspberry pi and OpenWRT based Routers.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://pypi.org/project/universalgpio/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://GitHub.com/harshsinghvi/UniversalGPIO)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/harshsinghvi/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/harshsinghvi/UniversalGPIO/graphs/commit-activity)

[![PyPI version](https://badge.fury.io/py/UniversalGPIO.svg)](https://badge.fury.io/py/UniversalGPIO)
[![GitHub release](https://img.shields.io/github/release/harshsinghvi/UniversalGPIO.svg)](https://GitHub.com/harshsinghvi/UniversalGPIO/releases/)

[![GitHub forks](https://img.shields.io/github/forks/harshsinghvi/UniversalGPIO.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/harshsinghvi/UniversalGPIO/network/)
[![GitHub stars](https://img.shields.io/github/stars/harshsinghvi/UniversalGPIO.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/harshsinghvi/UniversalGPIO/stargazers/)
[![GitHub watchers](https://img.shields.io/github/watchers/harshsinghvi/UniversalGPIO.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/harshsinghvi/UniversalGPIO/watchers/)
[![GitHub followers](https://img.shields.io/github/followers/harshsinghvi.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/harshsinghvi?tab=followers)

## 📔 [Documentation](https://github.com/harshsinghvi/UniversalGPIO/blob/master/docs/README.md)

### This Package includes

- [GPIO Module](https://github.com/harshsinghvi/UniversalGPIO/blob/master/docs/GPIO.md)
- [API Module](https://github.com/harshsinghvi/UniversalGPIO/blob/master/docs/API.md) 🏗️ (To be Updated Soon)
- [Dignostics and Troubleshooting  Module](https://github.com/harshsinghvi/UniversalGPIO/blob/master/docs/dignostics.md) 🚧 (To be Updated Soon)

## 💽 Installation (Stable Version)

The latest stable version is available on [PyPI](https://pypi.org/project/universalgpio/). Either add `UniversalGPIO` to your requirements.txt file or install with pip:

`pip install UniversalGPIO`

Or install from Releases:

`pip install https://github.com/harshsinghvi/UniversalGPIO/releases/download/v1.0.2/UniversalGPIO-1.0.2-py3-none-any.whl`

## 💻 Development

- Directly from source (fork or clone my repo)

```bash
git clone https://github.com/harshsinghvi/UniversalGPIO
cd UniversalGPIO
pip install --upgrade pip
pip install -r dev_requirements.txt

python setup.py sdist bdist_wheel ## to build the Package
pip install dist/UniversalGPIO-x.x.x-py3-none-any.whl ## install the package

bumpversion --current-version 1.0.0 minor setup.py UniversalGPIO/__init__.py ## Versioning
```

## 📜 Refrences

- [https://openwrt.org/docs/techref/hardware/port.gpio](https://openwrt.org/docs/techref/hardware/port.gpio)
- [https://openwrt.org/docs/guide-developer/add.new.device](https://openwrt.org/docs/guide-developer/add.new.device)

## 📝 Contributors

### 👨‍💻[Harsh Singhvi](https://harshsinghvi.com)

[![Twitter][1.1]][1]
[![Facebook][2.1]][2]
[![Github][3.1]][3]
[![LinkedIn][4.1]][4]

[1.1]: http://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[2.1]: http://i.imgur.com/fep1WsG.png (facebook icon without padding)
[3.1]: http://i.imgur.com/9I6NRUm.png (github icon without padding)
[4.1]: https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png (LinkedIn icon without padding)

[1]: http://www.twitter.com/harshsinghvi29
[2]: http://www.facebook.com/insomniaccoderharsh
[3]: http://www.github.com/harshsinghvi
[4]: https://www.linkedin.com/in/harsh-singhvi/

## 🛠️ Tested on

### Raspberry PI 3 Model B+

- OpenWrt Version 19.07.4

`/etc/os-reaease`

```bash
NAME="OpenWrt"
VERSION="19.07.4"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 19.07.4"
VERSION_ID="19.07.4"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r11208-ce6496d796"
OPENWRT_BOARD="brcm2708/bcm2710"
OPENWRT_ARCH="aarch64_cortex-a53"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 19.07.4 r11208-ce6496d796"
```
