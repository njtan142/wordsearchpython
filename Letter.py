import pygame


class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y, text):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        font = pygame.font.SysFont('timesnewroman',  20)
        self.image = font.render(text, True, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y