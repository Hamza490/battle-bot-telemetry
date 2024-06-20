import serial
import time
ser = serial.Serial('COM3', baudrate = 9600, timeout=1)
time.sleep(3)

while 1:
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
