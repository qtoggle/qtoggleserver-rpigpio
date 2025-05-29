from RPi import GPIO

from .rpigpio import RPiGPIO
from .rpigpiofloat import RPiGPIOFloat


__all__ = ["RPiGPIO", "RPiGPIOFloat"]


VERSION = "unknown-version"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
