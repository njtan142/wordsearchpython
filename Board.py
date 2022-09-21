import pygame
from Tile import Tile
from Letter import Letter
import random
import string


class Board(pygame.sprite.Sprite):
    def __init__(self, rows, columns, x, y, searches):
        tiles = []
        self.sprites = pygame.sprite.Group()
        self.player = [0, 0]
        self.x = x
        self.y = y
        self.startPos = [0, 0]
        self.endPos = [0, 0]
        self.start = True
        self.searches = searches
        for row in range(rows):
            for column in range(columns):
                char = searches[row][column].upper()
                # if char == "":
                #     char = random.choice(string.ascii_letters).lower()
                tile = Tile(row * 31 + x, column * 31 + y)
                letter = Letter(row * 31 + x + 7, column * 31 + y + 3, char)
                tiles.append(tile)
                self.sprites.add(tile, letter)

    def drawPlayer(self, screen):
        pygame.draw.rect(screen, (150, 150, 150),
                         pygame.Rect(self.player[0] * 31 + self.x, self.player[1] * 31 + self.y, 31, 31), 3)

        if self.start:
            pygame.draw.line(screen, (255, 0, 0),
                             (self.startPos[0] * 31 + 31 / 2 + self.x, self.startPos[1] * 31 + 31 / 2 + self.y),
                             (self.endPos[0] * 31 + 31 / 2 + self.x, self.endPos[1] * 31 + 31 / 2 + self.y), )

            # print(self.startPos, self.endPos)
            # a = self.startPos[0] - self.endPos[0]
            # b = self.startPos[1] - self.endPos[1]
            # length = max(abs(a), abs(b)) + 1
            # word = ""
            # if self.startPos[0] > self.endPos[0]:
            #
