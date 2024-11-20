# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame
from pygame import Color, Rect
from pygame import draw
from pygame import display
SCREEN_SIZE = (500,300)
# initialize pygame modules
pygame.init()
# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)
# background color
gameDisplay.fill(Color('white'))
# tonuge
draw.polygon (gameDisplay, Color('pink'), [(350, 175), (450, 175),(400,250)])
# lips
draw.rect(gameDisplay, Color('purple'), Rect(25, 125, 450, 50))
# eye one
draw.circle(gameDisplay, Color('black'), (166,50), 45)
# eye two
draw.circle(gameDisplay, Color('black'), (332,50), 45)
# show the graphics on the screen
display.flip()
# Wait for user input before closing the window
input("Press enter to exit")