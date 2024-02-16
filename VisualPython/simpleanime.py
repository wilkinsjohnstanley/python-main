from vpython import *
from time import *
#vector(x,y,z)
floor=box(pos=vector(0,-5,0),color=color.white,length=10,width=10,height=.1)
ceiling=box(pos=vector(0,5,0),color=color.white,length=10,width=10,height=.1)
leftWall=box(pos=vector(0,0,5),color=color.white,length=10,width=.1,height=10)
rightWall=box(pos=vector(0,0,-5),color=color.white,length=10,width=.1,height=10)
backWall=box(pos=vector(-5,0,0),color=color.white,length=.1,width=10,height=10)
#backWall=box(pos=vector(-5,0,0),color=color.white,size(.1, 10, 10))
marble=sphere(radius=.75, color=color.blue)
deltaX=.1
xPos=0
while True:
    rate(10)
    xPos=xPos+deltaX
    if (xPos>4 or xPos<-4):
        deltaX=deltaX*(-1)
    
    marble.pos=vector(0,xPos,0)