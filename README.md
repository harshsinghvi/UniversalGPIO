# 🔮 UniversalGPIO

Python Library for interfacing GPIO Pins on Linux based Routers, Network Devices, and embedded Devices like Raspberry pi and OpenWRT based Routers.

## 📔 [Documentation](Docs/README.md)

### This Package includes

- [GPIO Module](docs/GPIO.md)
- [API Module](docs/API.md) (To be Updated Soon)
- [Dignostics and Troubleshooting  Module](docs/Dignostics.md) (To be Updated Soon)

## 💽 Installation (Stable Version)

The latest stable version is available on PyPI. Either add `UniversalGPIO` to your requirements.txt file or install with pip:

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

## 🛠️ Tested on

### Raspberry PI 3 model B+

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

## 📜 Refrences

- [https://openwrt.org/docs/techref/hardware/port.gpio](https://openwrt.org/docs/techref/hardware/port.gpio)

## 📝 Contributors

### 👨‍💻[Harsh Singhvi](https://harshsinghvi.com)
