import pygame


class StaticGravityPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, mass):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (30, 255, 50), (5, 5), 5)
        self.rect = self.image.get_rect(center=(x, y))
        self.mass = mass

    def update(self, *args):
        pass
