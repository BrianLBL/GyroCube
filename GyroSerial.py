#Reads serial data from gyroscope sensor
import serial
import time

#Initialize (Reset module and )
MPU = int("68",16)
ser = serial.Serial('COM3', 19200, timeout = 1)   #Please set correct port value if not COM3
print(ser.name) #Testing which port was open
ser.write(int("6B"),16) #Communicate with register 6B
ser.write(int("00"),16) #Resets by writing 0 into register 6B
ser.close() #Ends the transmission

#Loop (Continuously Reads Data)

