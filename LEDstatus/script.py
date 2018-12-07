#!/usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
  
while True:
	data = (ser.readline()).decode('utf8')

	if(data == '0' ): print('the LED is Off')
	time.sleep(1)
	if(data == '0' ): print('the LED is ON')
  
  # written by AI : 09/10/2018 15:16:18
