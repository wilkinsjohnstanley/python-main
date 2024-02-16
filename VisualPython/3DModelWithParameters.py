from vpython import *
from time import *
#no constants, use variables
marbleRadius=.75
wallThickness=.1
roomWidth=10
roomDepth=10
roomHeight=10

#vector(x,y,z)
floor=box(pos=vector(0,-roomHeight/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
ceiling=box(pos=vector(0,roomHeight/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
backWall=box(pos=vector(0,0,-roomDepth/2),color=color.white,size=vector(roomWidth,roomHeight,wallThickness))
leftWall=box(pos=vector(-roomWidth/2,0,0),color=color.white,size=vector(wallThickness,roomHeight, roomDepth))
rightWall=box(pos=vector(roomWidth/2-, 0, 0),color=color.white,size=vector(wallThickness,roomHeight, roomDepth))
marble=sphere(radius=marbleRadius, color=color.blue)
deltaX=.1
xPos=0
while True:
    rate(10)
    xPos=xPos+deltaX
    if (xPos>4 or xPos<-4):
        deltaX=deltaX*(-1)
    
    marble.pos=vector(0,xPos,0)