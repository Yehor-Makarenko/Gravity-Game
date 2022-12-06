import pygame
import math
import numpy as np

G = 666.667
gravity_coefficient = 100


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, mass, max_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (255, 0, 50), (width // 2, height // 2), width // 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.mass = mass
        self.speed = np.array([float(0), float(max_speed)])
        self.max_speed = max_speed

    def update(self, *args):
        is_gravity_point = False
        for teleport in args[4]:
            if self.rect.colliderect(teleport.enter.rect):
                self.rect.center = teleport.exit.rect.center

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        self.speed[1] += gravity_coefficient / args[0]**2

        for gp in args[2]:
            force_vec = np.array(gp.rect.center) - np.array(self.rect.center)
            force_vec_len = np.linalg.norm(force_vec)

            if force_vec_len > 400:
                continue

            is_gravity_point = True
            acceleration = G * gp.mass**2 / force_vec_len**2
            acceleration_vec = acceleration * force_vec / (force_vec_len * args[0]**2)

            self.speed += acceleration_vec

        if self.speed[0] > self.max_speed:
            self.speed[0] = self.max_speed
        elif self.speed[0] < -self.max_speed:
            self.speed[0] = -self.max_speed

        if self.speed[1] > self.max_speed:
            self.speed[1] = self.max_speed
        elif self.speed[1] < -self.max_speed:
            self.speed[1] = -self.max_speed

        if self.rect.y > args[1] or self.rect.collidelist(list(obj.rect for obj in args[3])) != -1:
            self.kill()
