from RPi import GPIO

from .rpigpio import RPiGPIO
from .rpigpiofloat import RPiGPIOFloat


__all__ = ["RPiGPIO", "RPiGPIOFloat"]


VERSION = "0.0.0"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
