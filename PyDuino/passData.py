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

    #b'Count: 1\r\n'

    #remove the b
    dataPacket=str(dataPacket,'utf-8')
    #remove the giant spacing from Arduino's println 
    dataPacket=dataPacket.strip('\r\n')

    #unpack the data
    splitPacket=dataPacket.split(",")
    #now we have our data in the form of an array!!!
    #print(splitPacket)

    #take the first element of the array, convert to a float, and store it in x
    x=str(splitPacket[0])
    #same but y
    y=str(splitPacket[1])
    #same but z
    #z=str(splitPacket[2])
    print(x, y)

  