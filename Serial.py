import serialser = serial.Serial('/dev/tty.raspberrypi-SerialPort', timeout=1, baudrate=9600)
serial.flushInput();
serial.flushOutput()
   
while True:
    out = serial.readline().decode()
    if out!='' :
        print (out)
    if out == 'exit':
        break
