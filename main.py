import pygame
from objects.player import Player
from objects.staticGravityPoint import StaticGravityPoint
from objects.staticPlatform import StaticPlatform
from objects.teleport import Teleport
from objects.button import Button

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
back_button = Button("Back to menu", 90, 30, 180, 60, 30, (30, 54, 70))
# Main menu
is_main_menu = True
main_menu = pygame.Surface((W, H))
start_button = Button("Start", 300, H // 2 - 30, 140, 60, 30, (30, 54, 70))
end_button = Button("Quit", W - 300, H // 2 - 30, 140, 60, 30, (30, 54, 70))

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


def start_button_callback():
    global is_main_menu
    is_main_menu = False


def end_button_callback():
    global is_running
    is_running = False


def back_button_callback():
    global is_main_menu
    is_main_menu = True


while is_running:
    main_menu.fill(WHITE)
    main_screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        start_button.click(event, start_button_callback)
        end_button.click(event, end_button_callback)
        back_button.click(event, back_button_callback)

    if is_main_menu:
        main_menu.blit(start_button.image, start_button.rect)
        main_menu.blit(end_button.image, end_button.rect)
        screen.blit(main_menu, (0, 0))
    else:
        moving_game_objects.update(FPS, MAX_H, gravity_points, platforms, teleports)

        platforms.draw(main_screen)
        gravity_points.draw(main_screen)
        moving_game_objects.draw(main_screen)

        for teleport in teleports:
            main_screen.blit(teleport.enter.image, teleport.enter.rect)
            main_screen.blit(teleport.exit.image, teleport.exit.rect)

        y_offset = min(MAX_H - H, max(0, player.rect.centery - H // 2))

        main_screen.blit(back_button.image, (back_button.rect.x, back_button.rect.y + y_offset))

        screen.blit(main_screen, (0, -y_offset))

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_focused():
        pygame.draw.circle(screen, LIGHT_BLUE, pos, 5)

    pygame.display.flip()

    clock.tick(FPS)
