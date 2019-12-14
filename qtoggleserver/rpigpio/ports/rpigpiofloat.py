
from RPi import GPIO

from qtoggleserver.utils import json as json_utils
from qtoggleserver.core import ports


class RPiGPIOFloat(ports.Port):
    TYPE = ports.TYPE_BOOLEAN
    WRITABLE = True

    def __init__(self, no, def_value=None):
        self._no = no
        self._def_value = def_value

        super().__init__(port_id='gpio{}'.format(no))

    async def handle_enable(self):
        self._configure(self._def_value)

    async def read_value(self):
        return GPIO.gpio_function(self._no) == GPIO.OUT

    async def write_value(self, value):
        self.debug('writing output value %s', json_utils.dumps(value))

        if value:
            GPIO.setup(self._no, GPIO.OUT, initial=False)

        else:
            GPIO.setup(self._no, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

    def _configure(self, def_value):
        self.debug('configuring (initial=%s)', str(def_value).lower())

        if def_value:
            GPIO.setup(self._no, GPIO.OUT, initial=False)

        else:
            GPIO.setup(self._no, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
