import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

def forward:
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)  

def backward:
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)

def right:
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)

def left:
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
