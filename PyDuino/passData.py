import time
import serial
#I created an object that can get data from Arduino
arduinoData=serial.Serial('com5',9600)
#give it a second to get up and running
time.sleep(1)
#create an infinite loop just like Arduino!
while True:
    while(arduinoData.inWaiting()==0):
        pass
    dataPacket=arduinoData.readline()
    print(dataPacket)
