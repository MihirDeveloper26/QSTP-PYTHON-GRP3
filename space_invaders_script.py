#IMPORTING REQUIRED MODULE
import pygame
from pygame import *
import sys
from os.path import abspath, dirname
from random import choice


#Initializing pygame modules
pygame.init()

screen = pygame.display.set_mode((1024,720)) #Initialzing a screen for display

pygame.display.set_caption('Space Invaders')

clock = pygame.time.Clock() #setting frame rate

#COLORS IN RGB YOU CAN MAKE COMBINATIONS LATER
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)


base_path = abspath(dirname(__file__))
font_path = base_path + '/fonts/'
image_path = base_path + '/images/'
sound_path = base_path + '/sounds/'

#Initialize all Graphic requirements Here only
spaceship = pygame.image.load("spaceship.png")
spaceship = pygame.transform.scale(spaceship, (120, 120))
sw = screen.get_width() #stores screen width
sh = screen.get_height() #stores screen height
x_increment = 30 #increment on key press

#Initialize required Variables here
draw_state = 0
score = 0



try:
    #Reads file from local directory and extracts high score
    #       variable called highest_score
    highest_score_file = open("highscore.txt", "r")
    highest_score = int(highest_score_file.read())
    highest_score_file.close()
except:
    highScore = 0

def gameUi():
	'''
	Add lines of code here
	this will be the game screen
	'''
	pass


def gameLogic():
	'''
	Add lines of code here
	this function handles the game play
	'''
	pass

def left():
    '''
    Moves the spaceship to left
    '''
    global spaceship_x
    #pass
    if spaceship_x - x_increment > 0:
        spaceship_x -= x_increment


def right():
    '''
    Movews the spaceship to right
    '''
    global spaceship_x
    #pass
    if spaceship_x - x_increment < sw:
        spaceship_x += x_increment

def shoot():
    '''
    Spaceship fires
    '''
    pass

def welcomeScreen():
	'''
	Add lines of code here
	this will be the welcome screen
	'''
	pass

#welcomeScreen()
run = True #Initializing Variable

#In beginning place the spaceship at bottom centre of the screen

spaceship_y = screen.get_height() - spaceship.get_height()
spaceship_x = screen.get_width()/2 - spaceship.get_width()/2

while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    pressed = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    screen.blit(spaceship, (spaceship_x, spaceship_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#user quits game
            run = False
   		
        elif pressed[pygame.K_LEFT]:
            #left key pressed
            left()
        elif pressed[pygame.K_RIGHT]:
            #right key pressed
            right()
        elif pressed[pygame.K_SPACE]:
            #spacebar key pressed
            shoot()
    if draw_state == 0:
        pass
    	#welcomeScreen() #If newgame starts
    if draw_state > 0:#If game has already begun
        pass
        #gameUi()#Draw game matrix
    pygame.display.update() #Update portions of the screen for software displays 
            
pygame.quit() #Uninitialize all pygame modules

