#IMPORTING REQUIRED MODULE
import turtle
import os
import time

#screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Borders
brdr_pen = turtle.Turtle()
brdr_pen.speed(0)
brdr_pen.color("Blue")
brdr_pen.penup()
brdr_pen.setposition(-300,300)
brdr_pen.pendown()
brdr_pen.pensize(3)
for side in range(4):
    brdr_pen.fd(600)
    brdr_pen.rt(90)
brdr_pen.hideturtle()

#player
plr =turtle.Turtle()
plr.color("green")
plr.shape("triangle")
plr.penup()
plr.speed(0)
plr.setposition(0,-250)
plr.setheading(90)

#movement
plrspeed = 15

def move_left():
    x=plr.xcor()
    x-=plrspeed
    plr.setx(x)
def move_right():
    x = plr.xcor()
    x += plrspeed
    plr.setx(x)
#keys
turtle.listen()
turtle.onkey(move_left(),"Left")


exit("Enter")
#delay = ("press Enter to exit")
