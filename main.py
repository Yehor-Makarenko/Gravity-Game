import pygame
from objects.player import Player
from objects.staticGravityPoint import StaticGravityPoint
from objects.staticPlatform import StaticPlatform
from objects.teleport import Teleport

pygame.init()

W = 800
H = 1000
MAX_H = 1500

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Gravity Game")

clock = pygame.time.Clock()
FPS = 60
y_offset = 0
WHITE = (255, 255, 255)
LIGHT_BLUE = (0, 255, 255)
SOME_COLOR = (255, 0, 255)
is_running = True
main_screen = pygame.Surface((W, MAX_H))
player = Player(W // 2, 0, 20, 20, 100, 7 * 60 / FPS)
moving_game_objects = pygame.sprite.Group()
gravity_points = pygame.sprite.Group()
teleports = []
platforms = pygame.sprite.Group()

moving_game_objects.add(player)

gravity_points.add(StaticGravityPoint(W - 230, 100, 160))
gravity_points.add(StaticGravityPoint(590, 500, 160))
gravity_points.add(StaticGravityPoint(500, H - 100, 160))

platforms.add(StaticPlatform(-3, MAX_H // 2, 10, MAX_H))
platforms.add(StaticPlatform(W + 3, MAX_H // 2, 10, MAX_H))

platforms.add(StaticPlatform(200, 250, 500, 30))
platforms.add(StaticPlatform(W - 200, H - 200, 350, 30))
platforms.add(StaticPlatform(W // 2, MAX_H - 200, W, 30))

teleports.append(Teleport(W - 430, MAX_H - 500, 240, MAX_H - 100))

pygame.mouse.set_visible(False)

while is_running:
    main_screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    moving_game_objects.update(FPS, MAX_H, gravity_points, platforms, teleports)

    platforms.draw(main_screen)
    gravity_points.draw(main_screen)
    moving_game_objects.draw(main_screen)

    for teleport in teleports:
        main_screen.blit(teleport.enter.image, teleport.enter.rect)
        main_screen.blit(teleport.exit.image, teleport.exit.rect)

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_focused():
        pygame.draw.circle(main_screen, LIGHT_BLUE, pos, 5)

    y_offset = min(MAX_H - H, max(0, player.rect.centery - H // 2))

    screen.blit(main_screen, (0, -y_offset))

    pygame.display.flip()

    clock.tick(FPS)
