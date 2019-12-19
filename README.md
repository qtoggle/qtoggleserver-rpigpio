### About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides a qToggleServer driver for Raspberry Pi GPIOs.

The `RPiGPIO` port class allows controlling all available GPIOs, configuring them as inputs or outputs, enabling or
disabling internal pulls.
 
The `RPiGPIOFloat` port class makes RPi GPIOs always act as outputs, leaving them floating when writing "low".


### Install

Install using pip:

    pip install qtoggleserver-rpigpio


### Usage

##### `qtoggleserver.conf:`
``` javascript
...
ports = [
    ...
    {
        driver = "qtoggleserver.rpigpio.ports.RPiGPIO"
        no = 18
        def_value = true
        def_output = true
    }
    {
        driver = "qtoggleserver.rpigpio.ports.RPiGPIOFloat"
        no = 18
        def_value = true
    }
    ...
]
...
```
