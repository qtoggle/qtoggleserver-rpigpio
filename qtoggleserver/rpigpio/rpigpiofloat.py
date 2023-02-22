from typing import Optional

from RPi import GPIO

from qtoggleserver.core import ports as core_ports
from qtoggleserver.utils import json as json_utils


class RPiGPIOFloat(core_ports.Port):
    TYPE = core_ports.TYPE_BOOLEAN
    WRITABLE = True

    def __init__(self, no: int, def_value: Optional[bool] = None) -> None:
        self._no: int = no
        self._def_value: Optional[bool] = def_value

        super().__init__(port_id=f'gpio{no}')

    async def handle_enable(self) -> None:
        self._configure(self._def_value)

    async def read_value(self) -> bool:
        return GPIO.gpio_function(self._no) == GPIO.OUT

    @core_ports.skip_write_unavailable
    async def write_value(self, value: bool) -> None:
        self.debug('writing output value %s', json_utils.dumps(value))

        if value:
            GPIO.setup(self._no, GPIO.OUT, initial=False)
        else:
            GPIO.setup(self._no, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

    def _configure(self, def_value: Optional[bool]) -> None:
        self.debug('configuring (initial=%s)', str(def_value).lower())

        if def_value:
            GPIO.setup(self._no, GPIO.OUT, initial=False)
        else:
            GPIO.setup(self._no, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
