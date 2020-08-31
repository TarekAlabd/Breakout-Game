from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    def collision(self, rect):
        rl = False
        tb = False
        # same condition as old
        if self.get_top() >= rect.get_bottom() >= self.get_top():
            tb = True
        if rect.get_top() >= self.get_bottom() >= rect.get_bottom():
            tb = True
        if rect.get_left() <= self.get_right() <= rect.get_right():
            rl = True
        if rect.get_right() >= self.get_left() >= rect.get_left():
            rl = True
        return rl, tb

    def get_top(self):
        return self.top
    def get_bottom(self):
        return self.bottom
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

    def setDimensions(self,left,bottom,right,top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top


class Brick(RECTA):
    def __init__(self, x, y, left, bottom, right, top):
        RECTA.__init__(self,left, bottom, right, top)
        global brickWidth
        global brickHeight
        self._x = x
        self._y = y

    def draw(self):
        glLoadIdentity()
        colorAtCoordinates(self._x,self._y)
        left = self.getX() - brickWidth / 2
        bottom = self.getY() - brickHeight / 2
        right = self.getX() + brickWidth / 2
        top = self.getY() + brickHeight / 2
        #Drawing
        glRectd(left,bottom,right,top)
        #Update Dimensions
        RECTA.setDimensions(self,left,bottom,right,top)

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y 

    def offDeltaX(self, deltaX):
        self._x += deltaX

    def offDeltaY(self, deltaY):
        self._y += deltaY

class Ball(RECTA):
    def __init__(self, left, bottom, right, top):
        RECTA.__init__(self,left, bottom, right, top)
        global ballWidth
        global ballHeight
        self._x = ballWidth/2
        self._y = ballHeight/2

    
    def draw(self):
        glLoadIdentity()
        colorAtCoordinates(0,self._y)
        top = self.getY() + ballHeight / 2
        bottom = self.getY() - ballHeight / 2
        left = self.getX() - ballWidth / 2
        right = self.getX() + ballWidth / 2
        # Drawing
        glRectd(left, bottom,right,top)
        # update Dimensions
        RECTA.setDimensions(self,left,bottom,right,top)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def offDeltaX(self, deltaX):
        self._x+=deltaX

    def offDeltaY(self, deltaY):
        self._y+=deltaY

class Color:
    
    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    def getR(self):
        return self._r
    
    def getB(self):
        return self._b

    def getG(self):
        return self._g


ballWidth = 10
ballHeight = 10

# Brick dimensions
brickWidth = 38
brickHeight = 18

# Colors 

firstColor = Color(0.29,0,0.99)
secondColor = Color(1,0.5,0.1)
thirdColor =  Color(0.31,0.89,0.23)
fourthColor = Color(0.98,0.96,0.25)
fifthColor = Color(1,1,1)

def DrawRectangle(rect):
    glLoadIdentity()
    glBegin( GL_QUADS )
    glVertex( rect.left, rect.bottom, 0 )
    glVertex( rect.right, rect.bottom, 0 )
    glVertex( rect.right, rect.top, 0 )
    glVertex( rect.left, rect.top, 0 )
    glEnd()



def colorAtCoordinates(x, y):
    global firstColor
    global secondColor
    global thirdColor
    global fourthColor
    global fifthColor
    
    if y > 840 or y > 710 :
        glColor(firstColor.getR(), firstColor.getG(), firstColor.getB())
    elif y < 710 and y > 610:
        glColor(secondColor.getR(), secondColor.getG(), secondColor.getB()) 
    elif y < 610 and y > 510:
        glColor(thirdColor.getR(), thirdColor.getG(), thirdColor.getB())        
    elif y < 510 and y > 410:
        glColor(fourthColor.getR(), fourthColor.getG(), fourthColor.getB())     
    else:
        glColor(fifthColor.getR(), fifthColor.getG(), fifthColor.getB())
  

def drawColoredWalls():
    glColor(firstColor.getR(), firstColor.getG(), firstColor.getB())
    topSideWall = RECTA(5, 810, 635, 840)
    DrawRectangle(topSideWall)
    
    firstLeftSideWall = RECTA( 5, 815, 30, 710 )
    firstRightSideWall = RECTA( 610, 815, 635, 710)
    DrawRectangle(firstLeftSideWall)
    DrawRectangle(firstRightSideWall)
    
    glColor(secondColor.getR(), secondColor.getG(), secondColor.getB()) 
    secondLeftSideWall = RECTA( 5, 710, 30, 610 )
    secondRightSideWall = RECTA( 610, 710, 635, 610 )
    DrawRectangle(secondLeftSideWall)
    DrawRectangle(secondRightSideWall)
    
    glColor(thirdColor.getR(), thirdColor.getG(), thirdColor.getB())        
    thirdLeftSideWall = RECTA( 5, 610, 30, 510 )
    thirdRightSideWall = RECTA( 610, 610, 635, 510)
    DrawRectangle(thirdLeftSideWall)
    DrawRectangle(thirdRightSideWall)
    
    glColor(fourthColor.getR(), fourthColor.getG(), fourthColor.getB())     
    fourthLeftSideWall = RECTA( 5, 510, 30, 410 )
    fourthRightSideWall = RECTA( 610, 510, 635, 410 )
    DrawRectangle(fourthLeftSideWall)
    DrawRectangle(fourthRightSideWall)

    glColor(fifthColor.getR(), fifthColor.getG(), fifthColor.getB())
    fifthLeftSideWall = RECTA( 5, 410, 30, 75 )
    fifthRightSideWall = RECTA( 610, 410, 635, 75 )
    DrawRectangle(fifthLeftSideWall)
    DrawRectangle(fifthRightSideWall)

    glColor(firstColor.getR(), firstColor.getG(), firstColor.getB())
    sixthLeftSideWall = RECTA( 5, 75, 30, 60)
    sixthRightSideWall = RECTA( 610, 75, 635, 60)
    DrawRectangle(sixthLeftSideWall)
    DrawRectangle(sixthRightSideWall)

    glColor(fifthColor.getR(), fifthColor.getG(), fifthColor.getB())
    fifthLeftSideWall = RECTA( 5, 60, 30, 0 )
    fifthRightSideWall = RECTA( 610, 60, 635, 0 )
    DrawRectangle(fifthLeftSideWall)
    DrawRectangle(fifthRightSideWall)

def drawText(string, x, y):
    glLineWidth( 3 )
    glColor( 1, 1, 1 )
    glLoadIdentity()
    glTranslate( x, y, 0 )
    glScale( 0.18, 0.18, 1 )
    string = string.encode()  # conversion from Unicode string to byte string
    for i in string:  # render character by character starting from the origin
        glutStrokeCharacter( GLUT_STROKE_ROMAN, i )

