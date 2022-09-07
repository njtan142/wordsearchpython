import pygame
from Tile import Tile
from Letter import Letter


class Board(pygame.sprite.Sprite):
    def __init__(self, rows, columns, x, y):
        tiles = []
        self.sprites = pygame.sprite.Group()
        for row in range(rows):
            for column in range(columns):
                tile = Tile(row * 31 + x, column * 31 + y)
                letter = Letter(row * 31 + x + 7, column * 31 + y + 3, "Q")
                tiles.append(tile)
                self.sprites.add(tile, letter)
