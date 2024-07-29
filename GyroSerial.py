#Reads serial data from gyroscope sensor
import serial
import serial.tools.list_ports
import time

#Initialize (Starts the transmission)
ports = serial.tools.list_ports.comports();
ser = serial.Serial()
portList = []
for comPort in ports:
    portList.append(str(comPort))
    print(str(comPort))
    
val = input("select Port: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])
        
print(val)
        
MPU = int("68",16)
ser.baudrate = 19200 #Set the same baudrate as arduino code on module
ser.port = portVar
ser.open()

#Loop (Continuously Reads Data)
while True:
    if ser.is_waiting:
        packet = ser.readline()
        print(packet.decode('utf'))
