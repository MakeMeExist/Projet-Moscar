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
minute = 0

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
# pygame.display.set_caption("MOSCARLAND")
# screen = pygame.display.set_mode((640, 480))
# Combat.all_missile.draw(screen)
clock = pygame.time.Clock()
# List to hold the walls
# player = Player()  # Create the player

# ----------------------------------------------------------------------------------------------------------------------------------------
# missile = []
# for i in range(10):
#     missile.append(Missile(pygame.Rect(32 + randint(i * 5, i * 15), 64 + randint(i * 5, i * 15), 6, 6)))
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
mis = Missile(pygame.Rect(32, 62, 32, 32), 2, 2)
# for i in range(1):
#     for i in range(min + 1):
#         av = randint(0, len(spawn) - 1)
#         b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
#         missile.append(Missile(b, spawn[av].x, spawn[av].y, time))
#
# for i in range(len(missile)):
#     n = (player.rect.x - missile[i].rect.x) / 100
#     v = (player.rect.y - missile[i].rect.y) / 100
#     a = [n, v]
#     direc.append(a)
# ----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------

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
        minute += 1
        seconde = 0
    # création_chercheur(time, min, chercheur, spawn)
    création_missile2(time, minute, missile, spawn, direc)
    print(len(chercheur))

    # ----------------------------------------------------------------------------------------------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    # Move the player if an arrow key is pressed
    process_keyboard()
    # ----------------------------------------------------------------------------------------------------------------------------------------
    for i in range(len(chercheur)):
        chercheur[i].direction3(player.rect.x, player.rect.y)
        if player.rect.colliderect(chercheur[i]):
            print("dead")
            raise SystemExit
        chercheur[i].vie += 1
        if chercheur[i].vie > 400:
            suppr_chercheur.append(i)

    for i in range(len(missile)):

        # # direction_move_x = missile[i].direction(player.rect.x, player.rect.y)[0]
        # # direction_move_y = missile[i].direction(player.rect.x, player.rect.y)[0]
        # #
        # #       mode interessant
        # # for i in range(len(missile)):
        # #     direction_move_x = missile[i].direction(player.rect.x, player.rect.y)[0] / 50
        # #     direction_move_y = missile[i].direction(player.rect.x, player.rect.y)[0] / 50
        #
        # # je de base
        # # for i in range(len(missile)):
        # direction_move_x = direc[i][0]
        # direction_move_y = direc[i][1]
        # # if missile[i].rect.y == 0:
        # #     direction_move_y = missile[i].y
        # # if missile[i].rect.x == 0:
        # #     direction_move_y = missile[i].x
        # if missile[i].rect.x == 0 or missile[i].rect.x <= 1:
        #     direction_move_y, missile[i].rect.x = missile[i].y, missile[i].x
        #
        # missile[i].move(direction_move_x, direction_move_y)
        missile[i].update_enemy_position()
        # missile[i].move(1,2)
        if player.rect.colliderect(missile[i]):
            print("dead")
            raise SystemExit
        missile[i].vie += 1
        if missile[i].vie > 400:
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

    mis.direction2(player.rect.x, player.rect.y)
    # mis.move(1, 1)
    # print("chercheur", len(chercheur))
    # print("direc", len(direc))
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # if player.rect.colliderect(end_rect):
    #     raise SystemExit

    # Draw the scene
    screen.fill((0, 0, 0))
    draw_cube(walls, spawn, missile, chercheur)
    # pygame.draw.rect(screen, (22, 225, 55), mis)
    pygame.display.flip()
