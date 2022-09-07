import pygame
import sys
from Board import Board
from Letter import Letter

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Word Search')


white = (255, 255, 255)
black = (0, 0, 0)

board = Board(10,10, 100, 120)
letter = Letter(10, 10, 'hey')

sprites = pygame.sprite.Group()
sprites.add(letter)

class Player:
    def __init__(self):
        self.x = 100
        self.y = 120


player = Player()

def redraw():
    screen.fill(black)
    board.sprites.draw(screen)
    sprites.draw(screen)
    pygame.draw.rect(screen, (50, 50, 50), (player.x, player.y, 31, 31), 3)  # width = 3
    pygame.display.update()


def handlePress():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        player.y -= 31
    elif pressed[pygame.K_s]:
        player.y += 31
    elif pressed[pygame.K_a]:
        player.x -= 31
    elif pressed[pygame.K_d]:
        player.x += 31




while 1:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            handlePress()

    print(player.x, player.y)
    redraw()
