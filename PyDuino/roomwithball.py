from vpython import *
import time
import serial

arduinoData=serial.Serial('com5', 9600)
roomX=10
roomY=10
roomZ=15
wallT=.5
wallColor=vector(1,1,1)
wallOpacity=.8
frontOpacity=.1
marbleR=.5
ballColor=vector(0,0,1)

myFloor=box(size=vector(roomX,wallT,roomZ),pos=vector(0,-roomY/2,0),color=wallColor,opacity=wallOpacity)
myCeiling=box(size=vector(roomX,wallT,roomZ),pos=vector(0,roomY/2,0),color=wallColor,opacity=wallOpacity)
leftWall=box(size=vector(wallT,roomY,roomZ),pos=vector(-roomX/2,0,0),color=wallColor,opacity=wallOpacity)
rightWall=box(size=vector(wallT,roomY,roomZ),pos=vector(roomX/2,0,0),color=wallColor,opacity=wallOpacity)
backWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,-roomZ/2),color=wallColor,opacity=wallOpacity)
frontWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,roomZ/2),color=wallColor,opacity=frontOpacity)
marble=sphere(color=ballColor,radius=marbleR)

paddleX=2
paddleY=2
paddleZ=.2
paddleOpacity=.8
paddleColor=vector(0,.8,.9)
paddle=box(size=vector(paddleX,paddleY,paddleZ), pos=vector(0,0,roomZ/2), color=paddleColor,opacity=paddleOpacity)
#deltas are the velocity
marbleX=0
deltaX=.06

marbleY=0
deltaY=.06

marbleZ=0
deltaZ=.06

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

    padX=(roomX/1023.0)*x-roomX/2
    padY=(-roomY/1023.0)*y+roomY/2

    marbleX=marbleX+deltaX
    marbleY=marbleY+deltaY
    marbleZ=marbleZ+deltaZ

#if it hits the left or right wall, it changes its x direction
    if marbleX+marbleR>(roomX/2-wallT/2) or marbleX-marbleR<(-roomX/2+wallT/2):
        deltaX=deltaX*(-1)
        marbleX=marbleX+deltaX
#if it hits the top or bottom wall, it changes its y direction
    if marbleY+marbleR>(roomY/2-wallT/2) or marbleY-marbleR<(-roomY/2+wallT/2):
        deltaY=deltaY*(-1)
        marbleY=marbleY+deltaY

#if it hits the back wall, change direction
    if marbleZ-marbleR<(-roomZ/2+wallT/2):
        deltaZ=deltaZ*(-1)
        marbleZ=marbleZ+deltaZ
# but the front only if it intersects the paddle
    if marbleZ+marbleR>=roomZ/2-wallT/2:
        #if all 4 of these are true then we bounce
        if marbleX>padX-paddleX/2 and marbleX<padX+paddleX/2 and marbleY>padY-paddleY/2 and marbleY<padY+paddleY/2:
#how to bounce
            deltaZ=deltaZ*(-1)
            marbleZ=marbleZ+deltaZ
    marble.pos=vector(marbleX,marbleY,marbleZ)
    paddle.pos=vector(padX, padY, roomZ/2)

