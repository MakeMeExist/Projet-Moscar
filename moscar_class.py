#! /usr/bin/env python

import os
import random
import pygame
from math import sqrt
from math import ceil

walls = []


def norm(x, y) -> float:
    return sqrt(x ** 2 + y ** 2)


# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(256, 106, 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 6, 6)


class Missile:
    def __init__(self, rec, x_def, y_def, naissance=999999999999):
        self.rect = rec
        self.x = x_def
        self.y = y_def
        self.depart = naissance
        self.vie = 0


    def move(self, dx, dy):

        if dx != 0:
            self.move_single_axis(dx, 0)
        else:
            self.move_single_axis(self.x, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
        else:
            self.move_single_axis(self.y, 0)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

    def direction(self, x, y):
        a = self.rect.x
        b = self.rect.y
        return [x - a, y - b]

    def direction2(self, x, y):
        a = self.rect.x
        b = self.rect.y
        vx,vy = 1,1
        if x < a:
            vx = -vx
        if y <b:
            vy = -vy
        self.move(vx,vy)

    # def suppression:
    #     if


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


class Spawn:
    def __init__(self, rec, x_def, y_def):
        self.rect = rec
        self.x = x_def
        self.y = y_def
