import pygame
import sys
import time
from Letter import Letter
from Scene1 import SceneOne, MainMenuScene, LevelSelection

print("""

            ░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
            ░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
            ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
            ░░████╔═████║░██║░░██║██╔══██╗██║░░██║  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
            ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
            ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝  """)

print("\n\n")
user = input(
    "                                          PRESS ENTER TO START                                                                ")

loading = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████████████████████████████████████"
for char in loading:
    sys.stdout.write(char)
    sys.stdout.flush()

    time.sleep(0.02)

print("\n\n")
print("""                                               [1] EASY                                    """)
print("""                                               [2] HARD                                      """)

category = input("Enter your game mode:")
match int(category):
    case 1:
        print('You selected easy mode')
    case 2:
        print('You selected hard mode')
    case other:
        print('Wrong input, please restart the game')
        sys.exit()
easyLevel1 = ['plain', 'river', 'herb', 'arctic', 'ivy', 'valley']
easyLevel2 = ['yam', 'lobster','sparrow','parrot','bear','tick']
easyLevel3 = ['neongreen','neonblue','peach','purple','yellowgreen']

hardLevel1 = ['sand','raspberry','lilac','cyan','sapphire','amaranth','ochre','amber','slategray','apricot']
hardLevel2 = ['vienna','honolulu','liecester','riverside','geneva','leipzig','seattle','prague','kabul','budapest']
hardLevel3 = ['bamboo','season','coast','waterfall','savanna','rainforest','ocean','marsh','reed']
hardLevel4 = ['toaster','duvet','curtains','cupboard','bath','mattress','espresso','blanket','wardrobe']
hardLevel5 = ['weasel','vicuna','opossum','crane','swan','chicken','dolphin','guanaco','lemming']

words = []
if category == 1:
    level = input("Select level (1 to 3)")
    match int(level):
        case 1:
            words = easyLevel1
        case 2:
            words = easyLevel2
        case 3:
            words = easyLevel3
        case other:
            sys.exit()
else:
    level = input("Select lvel (1 to 5)")
    match int(level):
        case 1:
            words = hardLevel1
        case 2:
            words = hardLevel2
        case 3:
            words = hardLevel3
        case 4:
            words = hardLevel4
        case 5:
            words = hardLevel5


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
