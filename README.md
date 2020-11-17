# UniversalGPIO 

Python Library for interfacing GPIO Pins on Linux based Routers, Network Devices, and embedded Devices like Raspberry pi and OpenWRT based Routers.
## Tested on:
#### Raspberry PI 3 model B+
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


## Development

- Directly from source (fork or clone my repo)
```bash 
git clone https://github.com/harshsinghvi/UniversalGPIO
cd UniversalGPIO 
pip3 install -r dev_requirements.txt

python3 setup.py sdist bdist_wheel ## to build the Package
pip install dist/UniversalGPIO-x.x.x-py3-none-any.whl ## install the package

bumpversion --current-version 1.0.0 minor setup.py UniversalGPIO/__init__.py ## Versioning 

```

## Refrences :
- [https://openwrt.org/docs/techref/hardware/port.gpio](https://openwrt.org/docs/techref/hardware/port.gpio)

## Contributors 
- [Harsh Singhvi](https://harshsinghvi.com)
