from vpython import *
from time import *
mRadius=.75
wallThickness=.1
roomWidth=10
roomDepth=5
roomHeight=10
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)
deltaX=.1
deltaY=.1
deltaZ=.1

xPos=0
yPos=1
zPos=-1

while True:
    rate(50)
    xPos=xPos+deltaX
    yPos=yPos+deltaY
    zPos=zPos+deltaZ
    #x right marble edge
    XRME=xPos+mRadius
    XLME=xPos-mRadius
#y top marble edge/y bottom marble edge
    Ytme=yPos+mRadius
    Ybme=yPos-mRadius
#z back marble edge/z front marble edge
    Zbme=zPos-mRadius
    Zfme=zPos+mRadius
 #right wall edgeS
    RWE=roomWidth/2-wallThickness/2
    LWE=-roomWidth/2+wallThickness/2

    
    if (XRME>=RWE or XLME<LWE):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)


    #Homework is to make the ball move in three dimensions