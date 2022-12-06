import pygame


class Teleport:
    def __init__(self, x1, y1, x2, y2):
        self.enter = pygame.sprite.Sprite()
        pygame.sprite.Sprite.__init__(self.enter)
        self.enter.image = pygame.Surface((10, 10))
        self.enter.image.fill((255, 255, 255))
        pygame.draw.circle(self.enter.image, (0, 0, 0), (5, 5), 5)
        self.enter.rect = self.enter.image.get_rect(center=(x1, y1))

        self.exit = pygame.sprite.Sprite()
        pygame.sprite.Sprite.__init__(self.exit)
        self.exit.image = pygame.Surface((10, 10))
        self.exit.image.fill((255, 255, 255))
        pygame.draw.circle(self.exit.image, (50, 50, 50), (5, 5), 5)
        self.exit.rect = self.exit.image.get_rect(center=(x2, y2))

def update(self, *args):
        pass
