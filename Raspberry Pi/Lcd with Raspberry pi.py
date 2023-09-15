import RPi.GPIO as GPIO
from time import sleep
import lcddriver

GPIO.setmode(GPIO.BCM)

sp = 18
led = 17

password = "12345"

GPIO.setup(sp, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

display = lcddriver.lcd()

#setup
try:
    while True:
        sensor = GPIO.input(sp)
        if sensor == 1:
            p = input("Enter the password: ")
            display.lcd_clear()
            display.lcd_display_string("Enter the password", 1)
            if p == password:
                print("Password Accepted!")
                display.lcd_clear()
                display.lcd_display_string("Password accepted", 1)
                GPIO.output(led, 1)
            elif p !== password:
                print("Invalid password")
                display.lcd_clear()
                display.lcd_display_string("Invalid password", 1)
        elif sensor == 0:
            print("Nothing detected")
            display.lcd_clear()
            display.lcd_display_string("Nothing detected", 1)
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
