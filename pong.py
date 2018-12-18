# Add the pygame library to our code
import pygame, sys
from pygame.locals import *

# Initialise the pygame library after it's been imported
pygame.init()

# This is a frames per second counter, we can use it to make sure the game runs at a constant framerate
fpsClock = pygame.time.Clock();

# Opens a new window with a size of 640 pixels wide and 480 pixels high (Resolution of 640x480). You can change the numbers to make the window bigger/smaller
windowSurfaceObj = pygame.display.set_mode((640,480))
# Sets the title of the window we just opened
pygame.display.set_caption('Pong!')

# I have made some color variables so we can use them later on in our game. The pygame.Color(number, number, number) function takes 3 arguments, these are for the amount of RED, GREEN, and BLUE. Each value must be between 0 and 255, where 0 means no color and 255 means full color.
# For example pygame.Color(255, 0, 0) means full RED, and no GREEN or BLUE.
#                           R   G  B

# You can google 'color picker' for a nice little widget that will let you choose a color and give you the R,G,B value needed to add it to your game!
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)

# Creates a variable to check whether Player 1 is pressing the W or S key, we make them False to start with and will make them True if they are pressed in our main game loop below
keyWPressed = False
keySPressed = False

# Creates a variable to check whether Player 2 is pressing the UP or DOWN arrow key
keyUpPressed = False
keyDownPressed = False

# Create some variables for the size of our Players
playerWidth = 10
playerHeight = 100

# Creates some variables for where to draw Player 1 on the screen
player1X = 10
player1Y = 240 - (playerHeight/2)

# Creates some variables for where to draw Player 2 on the screen
player2X = 620
player2Y = 240 - (playerHeight/2)

# Creates some variables for where to draw the ball on the screen
ballX = 50
ballY = 240
ballRadius = 14

# Create a variable for how fast our players can move
speed = 8

# Create variables for how fast our ball moves
ballSpeedX = 4
ballSpeedY = 4

# This is our main game loop, each time the code in this loop runs it counts as 1 frame. Our game is going to run at about 30 frames per second, so this code will run all the way through 30 times in 1 second.
while True:
    # USER INPUT

    # This 'for loop' checks every possible action the user might make, for example: moving the mouse, pressing keys, clicking the mouse buttons.
    # We will only check for keyboard presses for our game
    for event in pygame.event.get():
        # Closes our window when the 'X' on the top right of the window is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Check if the UP, DOWN, W or S keys are pressed and make the variables we made above set to True if they are
        elif event.type == KEYDOWN:
            # W Key
            if event.key == K_w:
                keyWPressed = True
            # S Key
            elif event.key == K_s:
                keySPressed = True
            # UP Key
            if event.key == K_UP:
                keyUpPressed = True
            # DOWN Key
            elif event.key == K_DOWN:
                keyDownPressed = True
        # Check if the UP, DOWN, W or S keys are released and make the variables we made above set to False if they are
        elif event.type == KEYUP:
            # W Key
            if event.key == K_w:
                keyWPressed = False
            # S Key
            elif event.key == K_s:
                keySPressed = False
            # UP Key
            if event.key == K_UP:
                keyUpPressed = False
            # DOWN Key
            elif event.key == K_DOWN:
                keyDownPressed = False

    # GAME LOGIC

    # Move the players if they are holding down their controls (UP, DOWN, W, S)
    if(keyWPressed == True):
        player1Y -= speed
    if(keySPressed == True):
        player1Y += speed
    if(keyUpPressed == True):
        player2Y -= speed
    if(keyDownPressed == True):
        player2Y += speed

    # Stop the players from going off the screen
    if(player1Y < 0):
        player1Y = 0
    if(player1Y+playerHeight > 480):
        player1Y = 480-playerHeight
    if(player2Y < 0):
        player2Y = 0
    if(player2Y+playerHeight > 480):
        player2Y = 480-playerHeight

    # Move our ball on each frame of the game loop
    ballX += ballSpeedX
    ballY += ballSpeedY

    # If the ball hits a Player make it bounce in the other direction
    if(ballX - ballRadius <= player1X + playerWidth and ballY > player1Y and ballY < player1Y + playerHeight):
        ballX = player1X + playerWidth + ballRadius
        ballSpeedX = -ballSpeedX

    if(ballX + ballRadius >= player2X and ballY > player2Y and ballY < player2Y + playerHeight):
        ballX = player2X - ballRadius
        ballSpeedX = -ballSpeedX

    # If our ball hits the top or bottom of the window make it bounce in the opposite direction
    if(ballY - ballRadius <= 0):
        ballY = ballRadius
        ballSpeedY = -ballSpeedY
    elif(ballY + ballRadius >= 480):
        ballY = 480 - ballRadius
        ballSpeedY = -ballSpeedY

    # If the other player scores a goal reset the position of the ball
    if(ballX - ballRadius > 640):
        ballX = 50
        ballY = 240
    if(ballX + ballRadius < 0):
        ballX = 590
        ballY = 240


    # RENDERING TO WINDOW

    # This is going to fill the window with a white background at the start of every frame, you can change this to any color you like
    windowSurfaceObj.fill(whiteColor)

    # Draws rectangles on our windowSurfaceObj (our window), to represent Player 1 and 2, it uses the Player positions we made earlier
    pygame.draw.rect(windowSurfaceObj, redColor, (player1X, player1Y, playerWidth, playerHeight))
    pygame.draw.rect(windowSurfaceObj, blueColor, (player2X, player2Y, playerWidth, playerHeight))

    # Draws a circle on our windowSurfaceObj (our window) to represent the ball, it uses the ball position we made earlier
    pygame.draw.circle(windowSurfaceObj, blackColor, (int(ballX), int(ballY)), ballRadius, 1)

    # After we have drawn our shapes we need to update the window at the end of the main game loop, this function does that
    pygame.display.update()

    #Set our frame rate to 30 frames per second
    fpsClock.tick(30)
