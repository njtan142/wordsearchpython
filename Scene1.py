import pygame
from WordSearchGenerator import WordsGenerator
from Letter import Letter


class SceneOne():
    def __init__(self, screen):
        self.screen = screen
        self.words = ['hello', 'world', 'python', 'word', 'search', 'magazine', 'language', 'programming']
        self.displayedWords = [None] * len(self.words)
        self.wordsearch = WordsGenerator(
            self.words, 11, 11)
        self.board = self.wordsearch.generate()
        self.level = ''
        self.sprites = pygame.sprite.Group()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.sprites.draw(self.screen)
        self.board.drawPlayer(self.screen)
        self.sprites.draw(self.screen)

    def generate(self):
        a = 1
        # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(0, 0, 100, 400))

    def playerMovement(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and self.board.player[1] > 0:
            self.board.player[1] -= 1
        elif pressed[pygame.K_s] and self.board.player[1] < 10:
            self.board.player[1] += 1
        elif pressed[pygame.K_a] and self.board.player[0] > 0:
            self.board.player[0] -= 1
        elif pressed[pygame.K_d] and self.board.player[0] < 10:
            self.board.player[0] += 1

        if pressed[pygame.K_RETURN]:
            if self.board.start:
                self.board.startPos = self.board.player.copy()
                self.board.start = False
            else:
                self.board.endPos = self.board.player.copy()
                self.board.start = True
                a = self.board.startPos[0] - self.board.endPos[0]
                b = self.board.startPos[1] - self.board.endPos[1]
                wordLength = max(abs(a), abs(b)) + 1
                print(a, b)
                if a < 0:
                    if b > 0:
                        x = self.board.startPos[0]
                        y = self.board.startPos[1]
                        print(x, y)
                        print(self.getWord(wordLength, x, y, 1, -1))
        # print(self.board.startPos, self.board.endPos)

    def getWord(self, length, x, y, dx, dy):
        word = ""
        x = x
        y = y
        for i in range(length):
            word += self.board.searches[x][y]
            x += dx
            y += dy
        return word


    def levelSelected(self, level):
        self.sprites = pygame.sprite.Group()
        self.level = Letter(390, 50, level, (255, 255, 255), 50)
        self.level.rect = self.level.image.get_rect(center=(1000 / 2, 700 / 2))
        self.level.rect.y = 50
        self.sprites.add(self.level)

        for index in range(len(self.words)):
            print(self.words[index])
            letter = Letter(0, index * 20, self.words[index], (250, 250, 250), 20)
            letter.rect.x = 0
            letter.rect.y = index * 20
            self.sprites.add(letter)

        print(self.sprites)


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
