import pygame
import sys
from Letter import Letter
from Scene1 import SceneOne, MainMenuScene, LevelSelection

print("Welcome to Word Finder")
username = input("Press enter to play game:")
print("Game modes:")
print("Easy - 1")
print("Medium - 2")
print("Hard - 3")
category = input("Enter your game mode:")
match int(category):
    case 1:
        print('You selected easy mode')
    case 2:
        print('You selected medium mode')
    case 3:
        print('You selected hard mode')
    case other:
        print('Wrong input, please restart the game')
        sys.exit()

level = input("Select level (1 to 5)")

print("Your game is loaded in a new window")

size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Word Search')


white = (255, 255, 255)
black = (0, 0, 0)

letter = Letter(10, 10, 'hey')

sprites = pygame.sprite.Group()
sprites.add(letter)

s1 = SceneOne(screen)

match int(category):
    case 1:
        s1.levelSelected("Easy | " + "Level " + level)
    case 2:
        s1.levelSelected("Medium | " + "Level " + level)
    case 3:
        s1.levelSelected("Hard | " + "Level " + level)



class Player:
    def __init__(self):
        self.x = 100
        self.y = 120


player = Player()

def redraw():
    screen.fill(black)
    sprites.draw(screen)
    # pygame.draw.rect(screen, (50, 50, 50), (player.x, player.y, 31, 31), 3)  # width = 3
    pygame.display.update()


def handlePress():
    global scene
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.y -= 31
    elif pressed[pygame.K_s]:
        player.y += 31
    elif pressed[pygame.K_a]:
        player.x -= 31
    elif pressed[pygame.K_d]:
        player.x += 31
    elif pressed[pygame.K_ESCAPE]:
            sys.exit()





while 1:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            handlePress()

    s1.playerMovement()
    s1.draw()
    s1.generate()
    # pygame.draw.rect(screen, (50, 50, 50), (player.x, player.y, 31, 31), 3)
    pygame.display.update()

