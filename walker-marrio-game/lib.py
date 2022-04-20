import turtle as t
import winsound
from turtle import Turtle
from random import randint

screen = t.Screen()
screen.bgpic('background.png')

# sau: width,height = 1067,600
WIDTH = 1067
HEIGHT = 600

SPEED = 10
SCORE = 0
max_score = 50

marrioFrame = 1
marrioDir = "r"
marrioX = 0

coinX = randint(-300, 300)
bombX = randint(-300, 300)
heartX = randint(-300, 300)

t_mario = Turtle()
t_coin = Turtle()
t_bomb = Turtle()
t_heart = Turtle()

# WINDOW SIZE
def windowSetup(width,height):
    t.setup(width, height)
    t.showturtle

def showMarrio(x,y):
    global t_mario, marrioFrame, marrioDir
    
    t_mario.penup()
    name = f'images/marion-{marrioDir}-{marrioFrame}.gif'
    s = t.Screen()
    s.addshape(name)
    
    t_mario.setposition(x,y)
    t_mario.shape(name)

def moveRight():
    global marrioX
    global marrioFrame
    global marrioDir
    global SCORE
    global coinX
    global bombX
    global heartX
    marrioDir = "r" 
    position =  WIDTH / 2 - 50
    if marrioX < position:
        marrioX += 50
    if coinX in range(marrioX-20, marrioX+20):
        SCORE += 10
        coinX = randint(-300, 300)
        showCoin(coinX)
    if bombX in range(marrioX-20, marrioX+20):
        SCORE -= 10
        bombX = randint(-300, 300)
        showBomb(bombX)
    if heartX in range(marrioX-20, marrioX+20):
        SCORE += 10
        heartX = randint(-300, 300)
        showHeart(heartX)
    marrioX += 50
    marrioFrame += 1
    if marrioFrame >= 5:
        marrioFrame = 1
    showMarrio(marrioX, 0)
    showScore()

def moveLeft():
    global marrioX
    global marrioFrame
    global marrioDir
    global SCORE
    global coinX
    global bombX
    global heartX
    marrioDir = "l"
    position = -WIDTH / 2 + 50
    if marrioX > position: 
        marrioX -= 50
    if coinX in range(marrioX-20, marrioX+20):
        SCORE += 10
        coinX = randint(-300, 300)
        showCoin(coinX)
    if bombX in range(marrioX-20, marrioX+20):
        SCORE -= 10
        bombX = randint(-300, 300)
        showBomb(bombX)
    if heartX in range(marrioX-20, marrioX+20):
        SCORE += 10
        heartX = randint(-300, 300)
        showHeart(heartX)
    marrioX += 0
    marrioFrame += 1
    if marrioFrame <= 5:
        marrioFrame = 1
    showMarrio(marrioX, 0)
    showScore()

def showScore():
    global SCORE, max_score
    t.hideturtle()
    t.clear()
    t.penup()
    t.setposition(0,-100)
    style = ('Courier', 30, 'bold')
    if SCORE >= 0:
        t.clear()
        t.write(f'{SCORE}', font = style)
        if max_score >= SCORE:
            t.clear()
            t.write(f'{SCORE}',font = style)
        else:
            t.clear()
            t.setposition(-200,-200)
            t.write("YEEEEEE!!!",font = style)
            t.hideturtle()       
    else:
        t.clear()
        t.setposition(-200, -200)
        t.write("OOPS TRY AGAIN!!!", font = style)
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        t.hideturtle()

# Display the coinX
def showCoin(x):
    global t_coin
    name = f'images/coin.gif'
    s = t.Screen()
    s.addshape(name)

    t_coin.penup()
    t_coin.setposition(x,0)

    t_coin.pendown()
    t_coin.shape(name)

# Display the bombX
def showBomb(x):
    global t_bomb

    name = f'images/bomb.gif'
    s = t.Screen()
    s.addshape(name)

    t_bomb.penup()
    t_bomb.setposition(x, 0)

    t_bomb.pendown()
    t_bomb.shape(name)

# Display the heartX
def showHeart(x):
    global t_heart

    name = f'images/heart.gif'
    s = t.Screen()
    s.addshape(name)

    t_heart.penup()
    t_heart.setposition(x, 0)

    t_heart.pendown()
    t_heart.shape(name)







