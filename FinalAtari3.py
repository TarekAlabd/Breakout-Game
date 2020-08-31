from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from utilities import *
import pygame


FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4
count =0

# Window dimensions
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 840

# Score
falling = 0
playerResult = 00

# x coordinates
mouse_x = 0

# Ball Speed 
deltaX = 5
deltaY = 5

# list of bricks
bricks = []

# Timers
brickCoordinatesUpdaterTimeInterval = 10000
brickAddingTimeInterval = 4*brickCoordinatesUpdaterTimeInterval
bricksShouldDescend = False
shouldAddMoreBricks = False

ball = Ball( 0, 0, 0, 0)  # initial position of the ball
wall = RECTA( 20, 20, WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20 )
player = RECTA( 0, 60, 30, 75 )  # initial position of the bat

# Testing the collision between the ball and the wall
def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    if ball.getX()+ballWidth/2 >= wall.right:
        return FROM_RIGHT
    if ball.getX()-ballWidth/2 <= wall.left:
        return FROM_LEFT
    if ball.getY()+ballHeight/2 >= wall.top:
        return FROM_TOP
    if ball.getY()-ballHeight/2 <= wall.bottom:
        return FROM_BOTTOM

# Testing the collision Logic between the ball and the bat
def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.getY()-ballHeight/2 <= player.top and ball.getX()-ballWidth/2 >= player.left and ball.getX()+ballWidth/2 <= player.right:
        return True
    return False


# Testing the collision between the ball and the bricks
def test_ball_brick(ball, bricks): # Test the collision between ball and brick
    for i in range(len(bricks)):
        rl = ball.collision(bricks[i])[0]
        tb = ball.collision(bricks[i])[1]
        # print(bricks[i].bottom())
        # print(ball.top())
        if rl == True and tb == True:
            print(rl, tb)
            x = True
            # print(bricks[i].getY() - brickHeight)
            # print(ballYTop)
            return x, i
    return False, -1
            #print(list(bricks.values())[i].getX(), list(bricks.values())[i].getY())


def gameTimer(x):
    glutPostRedisplay()
    glutTimerFunc(10, gameTimer,0) 

def updateBricksCoordinatesTimer(t):
    global bricksShouldDescend
    bricksShouldDescend = not bricksShouldDescend
    glutTimerFunc(brickCoordinatesUpdaterTimeInterval, updateBricksCoordinatesTimer,0)

def addMoreBricksTimer(x):
    global shouldAddMoreBricks
    shouldAddMoreBricks = not shouldAddMoreBricks
    glutTimerFunc(2 * brickAddingTimeInterval,addMoreBricksTimer,0)

# Drawing Bricks
def drawBricks(newX, newY):
    x = newX
    y = newY
    for i in range(4):  # iterate through row
        y -= 25
        for j in range(13):  # iterate through colom
            x += 45
            brick = Brick(x, y, x - brickWidth / 2, y - brickHeight / 2,
                          x + brickWidth / 2, y + brickHeight / 2)
            bricks.append(brick)
            brick.draw()
        x = 5
# SOUNDS
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

collision_sound = pygame.mixer.Sound("collision_tone.wav")
fall_sound = pygame.mixer.Sound("fall_tone.wav")



def Display():
    global falling
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global bricks
    global bricksShouldDescend
    global shouldAddMoreBricks
    global count

    glClear( GL_COLOR_BUFFER_BIT )

    string = str( falling )
    drawText( string, 315, 0 )
    string = str( playerResult )
    drawText( string, 150, 0 )

    ball.offDeltaX(deltaX)
    ball.offDeltaY(deltaY)
    
    ball.draw()
    glColor( 1, 1, 1 )

    # Collision logic 
    if Test_Ball_Wall( ball, wall ) == FROM_RIGHT:
        pygame.mixer.Sound.play(collision_sound)
        deltaX = -5

    if Test_Ball_Wall( ball, wall ) == FROM_LEFT:
        pygame.mixer.Sound.play(collision_sound)
        deltaX = 5

    if Test_Ball_Wall( ball, wall ) == FROM_TOP:
        deltaY = -5

    if Test_Ball_Wall( ball, wall ) == FROM_BOTTOM:
        deltaY = 5
        pygame.mixer.Sound.play(fall_sound)
        falling = falling + 1



    player.left = mouse_x - 25  # remember that "mouse_x" is a global variable
    player.right = mouse_x + 25

    DrawRectangle(player)

    # Drawing bricks
    if shouldAddMoreBricks:
        drawBricks(5, 945)
        shouldAddMoreBricks = False

    if(len(bricks)==0):
        drawBricks(5, 825)

        drawBricks(5, 620)
    else:
        for i in range(len(bricks)):
            if bricksShouldDescend:
                bricks[i].offDeltaY(-25)
            bricks[i].draw()
        bricksShouldDescend = False

    # Apply the collision between the ball and the bricks
    if test_ball_brick(ball, bricks)[0] == True:
        # print('Hello')
        count = count + 1
        del bricks[test_ball_brick(ball, bricks)[1]]
        deltaY = -5
        pygame.mixer.Sound.play(collision_sound)
        playerResult += 3

    # Collision logic 
    if Test_Ball_Player( ball, player ):
        deltaY = 5

     # winning and losing conditions
    if falling == 10:
        sys.exit("you lost,try again")
    if count == len(bricks):
            string = str("you win")
            drawText(string, 315, 400)


    drawColoredWalls()

    glutSwapBuffers()

def MouseMotion(x, y):
    global mouse_x
    mouse_x = x

def init():
    glClearColor( 0.0, 0.0, 0.0, 0.0 )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glOrtho( 0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1 )  # l,r,b,t,n,f
    glMatrixMode( GL_MODELVIEW )


def main():
    glutInit()
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
    glutInitWindowSize( WINDOW_WIDTH,
                        WINDOW_HEIGHT )  # mouse coordinates inbetween [WINDOW_WIDTH=800,WINDOW_HEIGHT=500]
    glutInitWindowPosition( 0, 0 )
    glutCreateWindow( b"Atari" )
    glutDisplayFunc( Display )
    glutTimerFunc(10, gameTimer,0) 
    glutTimerFunc(brickCoordinatesUpdaterTimeInterval, updateBricksCoordinatesTimer,0)
    glutTimerFunc(brickAddingTimeInterval,addMoreBricksTimer,0)
    glutPassiveMotionFunc( MouseMotion )
    init()
    glutMainLoop()


main()

