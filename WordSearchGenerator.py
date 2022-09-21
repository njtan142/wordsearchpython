import random
import math
from Board import Board


class WordsGenerator():
    def __init__(self, words, width=20, height=20):
        self.words = words
        self.width = width
        self.height = height
        self.backwards = 0.5
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.maxAttempts = 20

    def generate(self):
        self.words = sorted(self.words, key=len)
        grid = [["" for i in range(self.width)] for j in range(self.height)]
        unplaced = []

        for index in range(len(self.words)):
            originalWord = self.words[index]
            word = originalWord
            if random.random() < self.backwards:
                word = word[::-1]

            attempts = 0
            while attempts < self.maxAttempts:
                direction = random.randint(0, 3)
                info = self.directionInfo(word, direction)
                if info["maxx"] < 0 or info["maxy"] < 0 or info["maxy"]<info["miny"] or info["maxx"] < info["minx"]:
                    print('too long')
                    unplaced.append(originalWord)
                    break

                ox = round(random.random() * (info["maxx"] - info["minx"]) + info["minx"])
                oy = round(random.random() * (info["maxy"] - info["miny"]) + info["miny"])
                x = ox
                y = oy

                placeable = True
                count = 0
                for l in range(len(word)):
                    charInGrid = grid[x][y]
                    if charInGrid:
                        if charInGrid != word[l]:
                            placeable = False
                            break
                        else:
                            count += 1

                    y += info["dy"]
                    x += info["dx"]

                if not placeable or count >= len(word):
                    attempts += 1
                    continue

                x = ox
                y = oy
                for l in range(len(word)):
                    grid[x][y] = word[l]
                    y += info["dy"]
                    x += info["dx"]
                break

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if len(grid[i][j]) <= 0:
                    grid[i][j] = self.letters[math.floor(random.random() * len(self.letters))]

        self.grid = grid
        return Board(self.width, self.height, 320, 200, grid)

    def directionInfo(self, word, direction):
        minx = 0
        miny = 0
        maxx = self.width - 1
        maxy = self.height - 1
        dx = 0
        dy = 0
        match direction:
            case 0:
                maxy = self.height - 1
                miny = len(word) - 1
                dy = -1
                maxx = self.width - len(word)
                minx = 0
                dx = 1
            case 1:
                maxx = self.width - len(word)
                minx = 0
                dx = 1
            case 2:
                miny = 0
                maxy = self.height - len(word)
                dy = 1
                maxx = self.width - len(word)
                minx = 0
                dx = 1
            case 3:
                miny = 0
                maxy = self.height - len(word)
                dy = 1

        return {
            "maxx": maxx,
            "maxy": maxy,
            "minx": minx,
            "miny": miny,
            "dx": dx,
            "dy": dy
        }
