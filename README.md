## About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides a qToggleServer driver for Raspberry Pi GPIOs based on the 
[RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) Python library.

The `RPiGPIO` port class allows controlling all available GPIOs, configuring them as inputs or outputs, enabling or
disabling internal pulls.
 
The `RPiGPIOFloat` port class makes RPi GPIOs always act as outputs, leaving them floating when writing "low".


## Install

Install using pip:

    pip install qtoggleserver-rpigpio


## Usage

##### `qtoggleserver.conf:`
``` ini
...
ports = [
    ...
    {
        driver = "qtoggleserver.rpigpio.RPiGPIO"
        no = 18             # GPIO number
        def_value = true    # default value at startup
        def_output = true   # default output/input GPIO mode at startup
    }
    ...
]
...
```
