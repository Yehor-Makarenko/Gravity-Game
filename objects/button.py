import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height, font_size, bg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.font = pygame.font.SysFont("Arial", font_size)
        self.text = self.font.render(text, True, (100, 156, 255))
        self.image.fill(bg)
        self.image.blit(self.text, (width // 2 - self.text.get_width() // 2, height // 2 - self.text.get_height() // 2))
        self.bg = bg
        self.is_pressed = False

    def click(self, event, func):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(x, y):
            self.is_pressed = True
        if event.type == pygame.MOUSEBUTTONUP and self.is_pressed:
            self.is_pressed = False
            if self.rect.collidepoint(x, y):
                func()
