import pygame
from WordSearchGenerator import WordsGenerator
from Letter import Letter


class SceneOne():
    def __init__(self, screen):
        self.screen = screen
        self.wordsearch = WordsGenerator(
            ['hello', 'world', 'python', 'word', 'search', 'magazine', 'language', 'programming'], 11, 11)
        self.board = self.wordsearch.generate()
        self.level = ''
        self.sprites = pygame.sprite.Group()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.sprites.draw(self.screen)
        self.sprites.draw(self.screen)

    def levelSelected(self, level):
        self.sprites = pygame.sprite.Group()
        self.level = Letter(390, 50, level, (255, 255, 255), 50)
        self.level.rect = self.level.image.get_rect(center=(1000/2, 700/2))
        self.level.rect.y = 50
        self.sprites.add(self.level)


class MainMenuScene:
    def __init__(self, screen):
        self.title = Letter(390, 30, "Word", (255, 255, 255), 100)
        self.title2 = Letter(380, 120, "Finder", (255, 255, 255), 100)
        self.enter = Letter(390, 400, "Press Enter", (255, 255, 255), 50)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.title, self.title2, self.enter)
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.sprites.draw(self.screen)


class LevelSelection:
    def __init__(self, screen):
        self.title = Letter(200, 30, "Level Selection", (255, 255, 255), 100)
        self.easy = Letter(390, 340, "Easy(1)", (255, 255, 255), 50)
        self.medium = Letter(390, 400, "Medium(2)", (255, 255, 255), 50)
        self.hard = Letter(390, 460, "Hard(3)", (255, 255, 255), 50)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.title, self.easy, self.medium, self.hard)
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.sprites.draw(self.screen)
