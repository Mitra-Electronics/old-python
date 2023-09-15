import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

X = int(input("Wait for"))

led1 = 12#GPIO 18
led2 = 11#GPIO 17
led3 = 36#GPIO 16
led4 = 33#GPIO 13
led5 = 32#GPIO 12
led6 = 23#GPIO 11
led7 = 19#GPIO 10
led8 = 21#GPIO 9
led9 = 24#GPIO 8
led10 = 26#GPIO 7
led11 = 31#GPIO 6
led12 = 29#GPIO 5
led13 = 7#GPIO 4
led14 = 5#GPIO 3
led15 = 3#GPIO 2
led16 = 35#GPIO 19
led17 = 

GPIO.setup(led1, GPIO.OUT)

while True:
    GPIO.output(led1, True)
    time.sleep(X)
    GPIO.output(led1, False)
    time.sleep(X)
    
