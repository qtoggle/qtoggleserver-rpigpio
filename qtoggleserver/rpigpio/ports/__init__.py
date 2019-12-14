
from RPi import GPIO

from .rpigpio import RPiGPIO
from .rpigpiofloat import RPiGPIOFloat


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
