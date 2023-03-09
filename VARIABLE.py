#! /usr/bin/env python

import os
import random
import pygame
import timeOT
from moscar_constant import map_create
from moscar_class import *
from random import randint
from time import sleep
from moscar_constant import *
from math import acos
from math import sin
time = 0
seconde = 0
min = 0

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
clock = pygame.time.Clock()

# ----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------
spawn = []
for i in range(17):
    spawn.append(Spawn(pygame.Rect(32 * (i + 1) + 0, 0, 6, 6), -3, 3))
for i in range(15):
    spawn.append(Spawn(pygame.Rect(32, 32 * i + 32, 6, 6), - 1, 1))
for i in range(17):
    spawn.append(Spawn(pygame.Rect(32 * (i + 1) + 0, 64 + 13 * 32, 6, 6), - 1, 1))
for i in range(15):
    spawn.append(Spawn(pygame.Rect(32 + 16 * 32, 32 * i + 32, 6, 6), - 1, 1))
# ----------------------------------------------------------------------------------------------------------------------------------------
missile = []
chercheur = []
direc = []
suppr_missile = []
suppr_chercheur = []

# Holds the level layout in a list of strings.

map_create(mape)
# Parse the level string above. W = wall, E = exit

running = True

while running:
    clock.tick(60)
    time += 1
    if time % 60 == 0:
        seconde += 1
    if seconde // 20 == 1:
        min += 1
        seconde = 0

    création_missile3(time, min, missile, spawn, direc)
    print(len(chercheur))

    # ----------------------------------------------------------------------------------------------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    process_keyboard()
    # ----------------------------------------------------------------------------------------------------------------------------------------

    for i in range(len(missile)):

        missile[i].update_enemy_position()
        if player.rect.colliderect(missile[i]):
            print("dead")
            raise SystemExit
        missile[i].vie += 1
        if missile[i].vie > 600:
            suppr_missile.append(i)

    for i in suppr_missile:  # despawn
        for j in range(len(missile)):
            if i == j:
                direc = direc[:i] + direc[i + 1:]
                missile = missile[:i] + missile[i + 1:]
    suppr_missile = []

    for i in suppr_chercheur:  # despawn
        for j in range(len(chercheur)):
            if i == j:
                chercheur = chercheur[:i] + chercheur[i + 1:]
    suppr_chercheur = []

    screen.fill((0, 0, 0))
    draw_cube(walls, spawn, missile, chercheur)

    pygame.display.flip()
