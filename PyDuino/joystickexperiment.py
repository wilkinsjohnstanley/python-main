from vpython import *
import time
import serial

arduinoData=serial.Serial('com5', 9600)

paddleX=2
paddleY=2
paddleZ=.2

paddle=box(size=vector(paddleX,paddleY,paddleZ), color=blue)


while True:
    while arduinoData.inWaiting()==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket, 'utf-8')
    dataPacket.strip('\r\n')
    splitPacket=dataPacket.split(',')
    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])
    padX=x
    padY=y
    padZ=z
    paddle.pos=vector(padX, padY, padZ)

