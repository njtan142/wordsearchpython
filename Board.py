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
        self.currentStartPos = (0, 0)
        self.currentEndPos = (0, 0)
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

        # Current Line Drawing
        if self.start:
            self.currentStartPos = (self.startPos[0] * 31 + 31 / 2 + self.x, self.startPos[1] * 31 + 31 / 2 + self.y)
            self.currentEndPos = (self.endPos[0] * 31 + 31 / 2 + self.x, self.endPos[1] * 31 + 31 / 2 + self.y)
            pygame.draw.line(screen, (255, 0, 0),
                             (self.startPos[0] * 31 + 31 / 2 + self.x, self.startPos[1] * 31 + 31 / 2 + self.y),
                             (self.endPos[0] * 31 + 31 / 2 + self.x, self.endPos[1] * 31 + 31 / 2 + self.y), 3)
