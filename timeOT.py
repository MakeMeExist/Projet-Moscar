#! /usr/bin/env python

import os
import random
import pygame
from random import randint
from math import sqrt
from math import ceil
from math import acos
from math import cos
from math import sin
from math import radians

pygame.display.set_caption("MOSCARLAND")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
walls = []
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)


# 1440x900

def norm(x, y) -> float:
    return sqrt(x ** 2 + y ** 2)


class Hero:
    def __init__(self):
        self.rect = pygame.Rect(256, 106, 16, 16)
        self.size = 16
        self.HERO_BMP = pygame.Surface((self.size, self.size))
        self.HERO_BMP.fill(BLUE)
        self.HERO_SPEED = 10
        self.x = 1440 // 2
        self.y = 900 // 2

    def update_hero_position(self):
        new_x, new_y = self.x, self.y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            new_y = self.y - self.HERO_SPEED
        elif keys[pygame.K_DOWN]:
            new_y = self.y + self.HERO_SPEED
        if keys[pygame.K_LEFT]:
            new_x = self.x - self.HERO_SPEED
        elif keys[pygame.K_RIGHT]:
            new_x = self.x + self.HERO_SPEED
        self.x, self.y = new_x, new_y

    def blit_hero(self) -> None:
        screen.blit(self.HERO_BMP, (self.x - self.size // 2, self.y - self.size // 2))


# Class for the orange dude
# class Player(object):
#
#     def __init__(self):
#         self.rect = pygame.Rect(256, 106, 16, 16)
#
#     def move(self, dx, dy):
#
#         # Move each axis separately. Note that this checks for collisions both times.
#         if dx != 0:
#             self.move_single_axis(dx, 0)
#         if dy != 0:
#             self.move_single_axis(0, dy)
#
#     def move_single_axis(self, dx, dy):
#
#         # Move the rect
#         self.rect.x += dx
#         self.rect.y += dy
#
#         # If you collide with a wall, move out based on velocity
#         for wall in walls:
#             if self.rect.colliderect(wall.rect):
#                 if dx > 0:  # Moving right; Hit the left side of the wall
#                     self.rect.right = wall.rect.left
#                 if dx < 0:  # Moving left; Hit the right side of the wall
#                     self.rect.left = wall.rect.right
#                 if dy > 0:  # Moving down; Hit the top side of the wall
#                     self.rect.bottom = wall.rect.top
#                 if dy < 0:  # Moving up; Hit the bottom side of the wall
#                     self.rect.top = wall.rect.bottom


# Nice class to hold a wall rect
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 6, 6)


class Wall3():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 6
        self.wall_BMP = pygame.Surface((self.size, self.size))
        self.wall_BMP.fill(0)

    def blit_wall3(self) -> None:
        screen.blit(self.wall_BMP, (self.x - self.size // 2, self.y - self.size // 2))


class Missile:
    def __init__(self, rec, naissance=0, ENEMY_SPEED=3):
        self.rect = rec
        self.depart = naissance
        self.vie = 0
        self.ENEMY_SPEED = ENEMY_SPEED
        self.enemy_x = None
        self.enemy_y = None
        self.enemy_vx = None
        self.enemy_vy = None

    def move(self, dx, dy):

        if dx != 0:
            self.move_single_axis(dx, 0)
        else:
            self.move_single_axis(self.enemy_vx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        else:
            self.move_single_axis(self.enemy_vy, 0)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

    def direction(self, x, y):
        a = self.rect.x
        b = self.rect.y
        return [x - a, y - b]

    def directio(self, a, b):
        x = a - self.rect.x
        y = b - self.rect.y
        n = norm(x, y)
        angle = acos(x / n)
        vx = cos(angle) * 2
        vy = sin(angle) * 2
        if b < self.rect.y:
            vy = -vy
        print(vx, vy)
        return vx, vy

    def direction2(self, x, y):
        a = self.rect.x
        b = self.rect.y
        vx, vy = 1, 1
        if x < a:
            vx = -vx
        if y < b:
            vy = -vy
        self.move(vx, vy)

    def direction3(self, a, b):
        x = a - self.rect.x
        y = b - self.rect.y
        n = norm(x, y)
        angle = acos(x / n)
        vx = cos(angle) * 2
        vy = sin(angle) * 2
        # if a < self.rect.x:
        #     vx = -vx
        if b < self.rect.y:
            vy = -vy
        print(vx, vy)
        self.move(vx, vy)

    def direction4(self, hero_x, hero_y):
        ex = self.rect.x
        ey = self.rect.y
        dx = hero_x - ex
        dy = hero_y - ey
        n = norm(dx, dy)
        if n != 0:
            dx /= n
            dy /= n
        dx *= self.ENEMY_SPEED
        dy *= self.ENEMY_SPEED
        # self.move(ex + dx, ey + dy)
        # self.enemy_x, self.enemy_y, self.enemy_vx, self.enemy_vy = ex, ey, dx, dy
        self.enemy_vx, self.enemy_vy = dx, dy

    def update_enemy_position(self):
        self.rect.x, self.rect.y = self.rect.x + self.enemy_vx, self.rect.y + self.enemy_vy
        # self.move(self.enemy_vx,self.enemy_vy)


# def tirs(self,n):
#     def __init__(self):
#         super().__init__()
#         self.velocity = 5
#         self.image = pygame.image.load("image.png")
#         self.rect = self.image.get_rect()
#         self.image = pygame.transform.scale(self.image, (50, 50))
#
#
# class Combat:
#     def __init__(self):
#         self.niveau = 1
#         self.all_missile = pygame.sprite.Group()
#
#     def generation_missile(self):
#         self.all_missile.add(Missile())
class Enemy:
    def __init__(self, rec, HER_SPEED=10):
        self.rec = rec
        self.size = 6
        self.ENEMY_BMP = pygame.Surface((self.size, self.size))
        self.ENEMY_BMP.fill(RED)
        self.vie = 0
        self.ENEMY_SPEED = HER_SPEED * 0.8
        self.x = None
        self.y = None
        self.enemy_vx = None
        self.enemy_vy = None

    def direction4(self, her_x, her_y):
        ex = self.rec.x
        ey = self.rec.y
        dx = her_x - ex
        dy = her_y - ey
        n = norm(dx, dy)
        if n != 0:
            dx /= n
            dy /= n
        dx *= self.ENEMY_SPEED
        dy *= self.ENEMY_SPEED
        # self.move(ex + dx, ey + dy)
        self.x, self.y, self.enemy_vx, self.enemy_vy = ex, ey, dx, dy
        # self.enemy_vx, self.enemy_vy = dx, dy

    def update_enemy_position(self):
        self.x, self.y = self.x + self.enemy_vx, self.y + self.enemy_vy

    def blit_enemy(self) -> None:
        screen.blit(self.ENEMY_BMP, (self.x - self.size // 2, self.y - self.size // 2))

    def collision(self, objet):
        if self.x - objet.size <= objet.x < self.x + self.size \
                and self.y - objet.size <= objet.y < self.y + self.size:
            # print(
            #     f"Missile : {self.x, self.y, self.x + self.size, self.y + self.size}")
            # print(f"Heros : {objet.x, objet.y, objet.x + objet.size, objet.y + objet.size}")
            return True
        return False


class Spawn:
    def __init__(self, rec, x_def, y_def):
        self.rect = rec
        self.x = x_def
        self.y = y_def
