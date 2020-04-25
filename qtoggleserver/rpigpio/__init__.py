

from RPi import GPIO

from .rpigpio import RPiGPIO
from .rpigpiofloat import RPiGPIOFloat


VERSION = 'unknown'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
