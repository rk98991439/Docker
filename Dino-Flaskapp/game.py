import random
import os
import pygame

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
GRAVITY = 0.6

class Dino:
    def __init__(self):
        self.score = 0
        self.jumping = False
        self.dead = False
        self.ducking = False
        self.rect = pygame.Rect(50, SCREEN_HEIGHT - 50, 44, 47)
        self.jump_speed = 11.5
        self.movement = [0, 0]

    def jump(self):
        if not self.jumping and not self.dead:
            self.jumping = True
            self.movement[1] = -self.jump_speed

    def duck(self):
        if not self.jumping and not self.dead:
            self.ducking = True

    def unduck(self):
        self.ducking = False

    def update(self):
        if self.jumping:
            self.movement[1] += GRAVITY
            self.rect.y += self.movement[1]
            if self.rect.y >= SCREEN_HEIGHT - 50:
                self.jumping = False
                self.rect.y = SCREEN_HEIGHT - 50

        self.score += 1

class Cactus:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - 40, 40, 40)
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

class Game:
    def __init__(self):
        self.dino = Dino()
        self.cacti = []
        self.game_over = False

    def spawn_cactus(self):
        if random.randint(0, 100) < 10:
            self.cacti.append(Cactus())

    def update(self):
        if not self.game_over:
            self.dino.update()
            for cactus in self.cacti:
                cactus.update()
                if self.dino.rect.colliderect(cactus.rect):
                    self.game_over = True
            self.cacti = [cactus for cactus in self.cacti if cactus.rect.x > -cactus.rect.width]
            self.spawn_cactus()

    def get_state(self):
        return {
            'dino': {
                'x': self.dino.rect.x,
                'y': self.dino.rect.y,
                'jumping': self.dino.jumping,
                'ducking': self.dino.ducking,
                'score': self.dino.score
            },
            'cacti': [{'x': cactus.rect.x, 'y': cactus.rect.y} for cactus in self.cacti],
            'game_over': self.game_over
        }

    def jump(self):
        self.dino.jump()

    def duck(self):
        self.dino.duck()

    def unduck(self):
        self.dino.unduck()

