#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

#Initializing pygame modules
width = 1024
height = 720
pygame.mixer.init(22100, -16, 2, 64)
pygame.init()
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")



#Initialize required Variables here

spaceship = pygame.image.load("spaceship.png")
spaceship = pygame.transform.scale(spaceship, (120, 120))
alienship = pygame.image.load("alienface.png")
alienship = pygame.transform.scale(alienship, (90,90))
sw = display.get_width() 
sh = display.get_height()
x_increment = 30 
ship_height = spaceship.get_height()
ship_width = spaceship.get_width()
spaceship_y = sh - spaceship.get_height()
spaceship_x = sw/2 - spaceship.get_width()/2
alien_speed = 4
global score,highest_score
draw_state = 0
score = 0

shoot_sound = pygame.mixer.Sound("shoot.ogg")
shoot_sound.set_volume(0.8)

#COLORS IN RGB YOU CAN MAKE COMBINATIONS LATER

background = (74, 35, 90)
white = (244, 246, 247)
yellow = (241, 196, 15)
orange = (186, 74, 0)
green = (35, 155, 86)
white1 = (253, 254, 254)
dark_gray = (23, 32, 42)
green = (0, 255, 0)
blue = ( 0, 0, 255)
gold=( 230, 215, 0)

font = pygame.font.SysFont("verdana", 22)
myfont = pygame.font.SysFont('verdana', 50)
resetFont = pygame.font.SysFont('Comic Sans MS', 30)
myfont_win=pygame.font.SysFont('Times New Roman', 80)

try:
    #       the highest score recorded. This is not erased when game is
    #       closed. Open the file and store the value of highest score in
    #       variable called highest_score
    highest_score_file = open("highscore.txt", "r")
    highest_score = int(highest_score_file.read())
    highest_score_file.close()
except:
    highest_score=0



#Main Space Shuttle to shoot the alien ships

class SpaceShip:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        spaceship_x = self.x
        spaceship_y = self.y
        display.blit(spaceship, (spaceship_x, spaceship_y))


# The bullet that has to be shot 

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 10
        self.speed = -5

    def draw(self):
        pygame.draw.ellipse(display, orange , (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
                return True

# Alien Battleship Movement 

class Alien:
    def __init__(self, x, y, d,speed):
        self.x = x
        self.y = y
        self.d = d
        self.x_dir = 1
        self.speed = speed

    def draw(self):
        alienship_x = self.x
        alienship_y = self.y
        display.blit(alienship,(alienship_x, alienship_y))


    def move(self):
        self.x += self.x_dir*self.speed

    def shift_down(self):
        self.y += self.d



def saved():
    # Result Declaration of the game
    font = pygame.font.SysFont("verdana", 22)
    font_large = pygame.font.SysFont("verdana", 43)
    text2 = font_large.render("Congo,finally you aced at something!", True, white1)
    display.blit(text2, (60, height/2))
    pygame.display.update()



def GameOver():
    # Game over Recognition

    font = pygame.font.SysFont("verdana", 50)
    font_large = pygame.font.SysFont("verdana", 100)
    text2 = font_large.render("Game Over!", True, white1)
    text = font.render("You Lost! You Suck!", True, white1)
    display.blit(text2, (180, height/2-50))
    display.blit(text, (45, height/2 + 100))

#Main Code for the Game Screen

def increase_level():
    pass
    global alien_speed
    alien_speed += 1
    alien_mov()

    

def alien_mov():
    global aliens
    global num_aliens
    global d
    global invasion
    global bullets
    global num_bullet
    aliens = []
    num_aliens = 8
    d = 50
    for i in range(num_aliens):
        i = Alien((i+1)*d + i*20, 80, d, alien_speed)
        aliens.append(i)

def welcome_message():

    global quit, draw_state


    mouse=pygame.mouse.get_pos()  
    click=pygame.mouse.get_pressed()
    
    
    display.fill(dark_gray)
    
    
    textsurface=myfont_win.render('Space Invaders', False, gold)
    display.blit(textsurface, (300, 200))    

    if mouse[0] < 540 and mouse[0] > 390 and mouse[1] < 480 and mouse[1] > 400:
        pygame.draw.rect(display, green,(440,400,140,70))
        if click[0]: 
           draw_state += 1
           game() 
    else: 
        pygame.draw.rect(display,blue,(440,400,140,70))


    textsurface = myfont.render('PLAY', False, white)
    display.blit(textsurface,(440,400)) 

green
def game():
    global invasion
    invasion = False
    ship = SpaceShip(width/2-ship_width /2, height- ship_height , ship_width, ship_height)
    move = False
    global score,highest_score

    global bullets
    bullets = []
    global num_bullet
    num_bullet = 0
    for i in range(num_bullet):
        i = Bullet(width/2 - ship_width/2, height - ship_height - 20)
        bullets.append(i)

    x_move = 0
    
    global aliens
    global num_aliens
    global d
    aliens = []
    num_aliens = 8
    d = 50
    alien_mov()

    while not invasion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RIGHT:
                    x_move = 30
                    move = True
                    ship.x += x_move

                if event.key == pygame.K_LEFT:
                    x_move = -30
                    ship.x += x_move
                    move = True

                if event.key == pygame.K_SPACE:
                    num_bullet += 1
                    i = Bullet(ship.x + ship_width/2 - 5, ship.y)
                    bullets.append(i)
                    

        display.fill(white1)

        textsurface = font.render('Score:', False, green)
        display.blit(textsurface,(0,0))
        textsurface = font.render(str(score), True, green)
        display.blit(textsurface,(72,0))
        
        textsurface = font.render('High Score: ', False, green)
        display.blit(textsurface,(840,0)) 

        textsurface = font.render(str(highest_score), True, green)
        display.blit(textsurface,(980,0))
        
        textsurface = font.render('Level:', False, green)
        display.blit(textsurface,(480,0))
        textsurface = font.render(str(int(score/80)+ 1), True, green)
        display.blit(textsurface,(550,0))

        for i in range(num_bullet):
            bullets[i].draw()
            bullets[i].move()


        for alien in list(aliens):
            alien.draw()
            alien.move()
            for item in list(bullets):
                if item.hit(alien.x, alien.y, alien.d):
                    pygame.mixer.Sound.play(shoot_sound)
                    pygame.mixer.music.stop()
                    bullets.remove(item)
                    num_bullet -= 1
                    aliens.remove(alien)
                    num_aliens -= 1
                    score += 10

        if score > highest_score:
            highest_score = score
            highest_score_file = open("highscore.txt", "w")
            highest_score_file.write(str(highest_score))
            highest_score_file.close()

        if num_aliens == 0:
            increase_level()
            num_bullet = 0
            bullets = []



        for i in range(num_aliens):
            if aliens[i].x + d >= width:
                for j in range(num_aliens):
                    aliens[j].x_dir = -1
                    aliens[j].shift_down()

            if aliens[i].x <= 0:
                for j in range(num_aliens):
                    aliens[j].x_dir = 1
                    aliens[j].shift_down()

        try:
            if aliens[0].y + d > height:
                GameOver()
                pygame.display.update()
                #invasion = True
        except Exception as e:
            pass
        

        

        if ship.x < 0:
            ship.x -= x_move
        if ship.x + ship_width > width:
            ship.x -= x_move

        ship.draw()

        pygame.display.update()
        clock.tick(60)
run = True
while run:
    if draw_state == 0:
        welcome_message()
        
    if draw_state > 0:
        game()
        run = False

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()


# In[ ]:




