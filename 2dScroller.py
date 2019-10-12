

#todo == slow down the coin an make it colectable


import pygame
from pygame_functions import *
import random

pygame.init()

#coin object
class coin:
    def __init__(self, x, y, image, collected):
        self.x = x
        self.y = y
        self.image = image
        self.collected = False
        
#player object
class player:
    def __init__(self, x, y, size, image):
        self.x = x
        self.y = y
        self.size = size
        self.image = image
        self.jumping = False
        self.jump_offset = 0
       
#jump method when key is hit       
def jumpPress(p):
    if keyPressed("space"):
        print("space was hit")
        p.jumping = True
        print("jump true")  
        movingCoin()   
    
#action of jumping      
def doJumping(p):
    jumpHeight

    if p.jumping:
        p.jump_offset += 4
        print("do_jump +1")
        if p.jump_offset >= jumpHeight:
            p.jumping = False
            print("do_jump = false")
    if p.jump_offset > 0 and p.jumping == False:
        p.jump_offset -= 4
        print("do_jump -1")
        
#to move the coin method
def movingCoin():
    moveSprite(coin1, random.randint(0, 800), random.randint(400, 550), True) 
    showSprite(coin1)           

#screen width
width, height = 800, 600
screenSize(width, height)

#sprite images the folder
playerImage = "images/run (3).png"
coinImage = "images/meme.png"

#object instances
p = player(50, 540, 30, playerImage)
c = coin(400, 350, coinImage, False)

#add player sprites
player1 = makeSprite(p.image)
addSpriteImage(player1, "images/run (2).png")
addSpriteImage(player1, "images/run (3).png")
addSpriteImage(player1, "images/run(4).png")
addSpriteImage(player1, "images/run(5).png")
addSpriteImage(player1, "images/run(6).png")
addSpriteImage(player1, "images/run(7).png")
addSpriteImage(player1, "images/run(8).png")
showSprite(player1)

#add coin sprite
coin1 = makeSprite(c.image)
#print(coin1)

#setBackground
setBackgroundImage("images/cartoonBackground1.jpg")

#height of jump in pixels
jumpHeight = 50

#make a clock
nextFrame = clock()
#frame start
frame = 0

#game loop
while True:
    
     #clock
    if clock() > nextFrame:
        frame = (frame+1)%8
        nextFrame += 80
    
    #movement and chaninging sprite image    
    if keyPressed("right"):
        changeSpriteImage(player1, 0*8+frame)
        scrollBackground(-5, 0)
            
        
    #calling the jump methods    
    jumpPress(p)
    doJumping(p)
    
    #pygame.display.update()
    moveSprite(player1, p.x, p.y - p.jump_offset, True) 

    #frames per second
    tick(60)


endWait()