import pygame


class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y, text, color=(0,0,0), size=20):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        font = pygame.font.SysFont('timesnewroman',  size)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y