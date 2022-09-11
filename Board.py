import pygame
from Tile import Tile
from Letter import Letter
import random
import string


class Board(pygame.sprite.Sprite):
    def __init__(self, rows, columns, x, y, searches):
        tiles = []
        self.sprites = pygame.sprite.Group()
        for row in range(rows):
            for column in range(columns):
                char = searches[row][column].upper()
                # if char == "":
                #     char = random.choice(string.ascii_letters).lower()
                tile = Tile(row * 31 + x, column * 31 + y)
                letter = Letter(row * 31 + x + 7, column * 31 + y + 3, char)
                tiles.append(tile)
                self.sprites.add(tile, letter)
