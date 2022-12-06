import pygame


class StaticPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((50, 50, 180))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, *args):
        pass
