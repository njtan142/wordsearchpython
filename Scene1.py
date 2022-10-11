import pygame
from WordSearchGenerator import WordsGenerator
from Letter import Letter
from copy import deepcopy


class SceneOne():
    def __init__(self, screen, words):
        self.currentEndPos = None
        self.currentStartPos = None
        self.screen = screen
        self.words = words
        self.displayedWords = [None] * len(self.words)
        self.wordsearch = WordsGenerator(
            self.words, 11, 11)
        self.board = self.wordsearch.generate()
        print(self.wordsearch.unplaced)
        self.words = list(set(self.words) - set(self.wordsearch.unplaced))
        print(self.words)
        self.level = ''
        self.sprites = pygame.sprite.Group()
        self.lines = []

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.sprites.draw(self.screen)
        self.board.drawPlayer(self.screen)
        self.sprites.draw(self.screen)
        for line in self.lines:
            pygame.draw.line(self.screen, (0,0,255), (line[0][0], line[0][1]), (line[1][0], line[1][1]), 3)

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

        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.K_RETURN:
                print("enter")

        if pressed[pygame.K_RETURN]:
            if self.board.start:
                self.board.startPos = self.board.player.copy()
                self.board.start = False
            else:
                self.board.endPos = self.board.player.copy()
                a = self.board.startPos[0] - self.board.endPos[0]
                b = self.board.startPos[1] - self.board.endPos[1]
                self.currentStartPos = (self.board.startPos[0] * 31 + 31 / 2 + self.board.x, self.board.startPos[1] * 31 + 31 / 2 + self.board.y)
                self.currentEndPos = (self.board.endPos[0] * 31 + 31 / 2 + self.board.x, self.board.endPos[1] * 31 + 31 / 2 + self.board.y)
                wordLength = max(abs(a), abs(b)) + 1
                print(a, b)
                if abs(a) == abs(b) or abs(b) == abs(a) or a == 0 or b == 0:
                    print("valid")
                    self.board.start = True
                    x = self.board.startPos[0]
                    y = self.board.startPos[1]
                    print(x, y)
                    if a != 0 and b != 0:
                        word = self.getWord(wordLength, x, y, int(abs(a)/a) * -1, int(abs(b)/b) * -1)
                    elif a == 0 and b != 0:
                        word = self.getWord(wordLength, x, y, 0, int(abs(b)/b) * -1)
                    elif b == 0 and a != 0:
                        word = self.getWord(wordLength, x, y, int(abs(a)/a) * -1, 0)
                    else:
                        word = self.getWord(wordLength, x, y, 0, 0)

                    if self.checkWord(word):
                        self.lines.append([deepcopy(self.currentStartPos), deepcopy(self.currentEndPos)])

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

    def checkWord(self, word):
        for answers in self.words:
            if word == answers or word[::-1] == answers:
                print("found!")
                return True
        return False

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
