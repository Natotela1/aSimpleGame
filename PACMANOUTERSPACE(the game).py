# Pac Man In Outer Space the game
# A game where pac man has to quickly collide with the cherry before it passes by off the screen to win
# while avoiding the monsters which are also passing
# if pac man collides with any monster you lose

# Import pygame to use its specific functions
import pygame
import random
from pygame import mixer
pygame.init()

# create a screen with a width and a height
# and make the background setting of game with backgroud music also

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PAC MAN IN OUTER SPACE")
background = pygame.image.load("background.jpg")
mixer.music.load("PAC-MAN Namco Sounds - Start Music.mp3")
mixer.music.play(-1)
# declare and assign the characters of game with images
player = pygame.image.load("player.jpg")
prize = pygame.image.load("pri.png")
enemy = pygame.image.load("monster.jpg")
enemy1 = pygame.image.load("enemey1.png")
enemy2 = pygame.image.load("enemy2.png")

# Get the width and height of the images in order to do boundary detection
# make the images stays within screen boundaries or know when the image is off the screen

image_height = player.get_height()
image_width = player.get_width()
prizeheight = prize.get_height()
prizewidth = prize.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy1height = enemy1.get_height()
enemy1width = enemy1.get_width()
enemy2height = enemy2.get_height()
enemy2width = enemy2.get_width()
pygame.display.flip()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# declare the positions that characters of game will initially display at
playerXPosition = 100
playerYPosition = 50


prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prizeheight)

enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2height)

# declare an check if the keys that will be used to control pac man is pressed using boolean values.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# a while loop that will run the game logic over and over again.
# during real time game play.

while 1:
    # declaring the display of the game in real time game play
    screen.fill(0)
    screen.blit(background, (0,0))
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    pygame.display.update()

    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press the right control key down an not up to be able to move pacman
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
              keyLeft = False
            if event.key == pygame.K_RIGHT:
              keyRight = False


    # declare control key  values to be able move player accordingly within the window screen  of game
    
    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 0.5
    if keyRight == True:
        if playerXPosition > 0:
            playerXPosition += 0.5
    # Check for collision of the enemy monsters with the player pacman
    # using bounding boxes around the images of the player and enemy characters.
    # if these boxes intersect there is a collision.
    
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Test collision of the boxes:
    # if theres collision between player and enemymonsters you lose
    # if theres coliision between player and cherry you win

    
    if (playerBox.colliderect(enemyBox)) or (playerBox.colliderect(enemy1Box)) or (playerBox.colliderect(enemy2Box)):
        print("You lose!")
        pygame.quit()
        exit(0)
    if prizeXPosition < 0:
        print("You lose!")
        pygame.quit()
        exit(0)

    if (playerBox.colliderect(prizeBox)):

        print("You win!")

        pygame.quit()
        exit(0)

    # declare how Make enemy approach the player.
    prizeXPosition -= 0.25
    enemyXPosition -= 0.15
    enemy1XPosition -= 0.4
    enemy2XPosition -= 0.15
    # ================The game loop logic ends here. =============
