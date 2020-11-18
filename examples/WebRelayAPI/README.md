# WebRelayAPI using UniversalGPIO.GPIO

## CONFIGURE

> Change the GPIO Pin numbers for your Device in the Dict for the code.

- install Dependencies: `pip install -r requierements.txt`

- GPIO Configure

```python
PINS = {
    "R1": 2,
    "R2": 3,
    "R3": 14,
    "R4": 15
}
```

- Run API Server: `python3 app.py` or `sudo python3 app.py # For non-root users`

### USAGE

- Web interface        : `http://localhost:5000/`
- Getting relay State  : `http://localhost:5000/status` or `http://localhost:5000/status/<RELAY>`
- Changing Relay State : `http://localhost:5000/set/relay=R1&state=1?` or `http://localhost:5000/<relay>/<state>`

### Configure At startup

```bash
cp webrelay /etc/init.d/webrelay
chmod +x /etc/init.d/webrelay
/etc/init.d/webrelay enable
```
