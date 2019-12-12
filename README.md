### About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides a qToggleServer driver for Raspberry Pi GPIOs.


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
        driver = "qtoggleserver.rpigpio.RPiGPIO"
        no = 18
        def_value = true
        def_output = true
    }
    ...
]
...
