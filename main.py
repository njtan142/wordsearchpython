import pygame
import sys
from Letter import Letter
from Scene1 import SceneOne, MainMenuScene, LevelSelection

size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Word Search')


white = (255, 255, 255)
black = (0, 0, 0)

letter = Letter(10, 10, 'hey')

sprites = pygame.sprite.Group()
sprites.add(letter)

s1 = SceneOne(screen)
main = MainMenuScene(screen)
level = LevelSelection(screen)


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


scene = 1
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
        if scene is 3:
            scene = 1
        elif scene is 2:
            scene = 1
        else:
            sys.exit()
    elif pressed[pygame.K_RETURN]:
        if scene is 1:
            scene = 2
        elif scene is 2:
            scene = 3
    elif pressed[pygame.K_1]:
        if scene is 2:
            scene = 3
            s1.levelSelected('Easy Level')
    elif pressed[pygame.K_2]:
        if scene is 2:
            scene = 3
            s1.levelSelected('Medium Level')
    elif pressed[pygame.K_3]:
        if scene is 2:
            scene = 3
            s1.levelSelected('Hard Level')



while 1:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            handlePress()

    print(scene)
    match(scene):
        case 1:
            main.draw()
        case 2:
            level.draw()
        case 3:
            s1.draw()
    pygame.display.update()

