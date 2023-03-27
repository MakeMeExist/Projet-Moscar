# #! /usr/bin/env python
#
# import os
# import random
# import pygame
#
# from moscar_constant import map_create2
# from moscar_class import *
# from random import randint
# from time import sleep
# from moscar_constant import *
# from math import acos
# from math import sin

from fonction import *

# lazer = Laser("barre")
# lazer.forme_(player)
# laser.append(lazer)
# ----------création_de_la_map------------------------------------------------------------------------------------------------------------------------------

generation_spawn(spawn)
map_create2(mape, walls)

running = True

while running:
    clock.tick(60)
    time += 1
    if time % 60 == 0:
        seconde += 1
    if seconde // 60 == 1:
        min += 1
        seconde = 0
    # my_timer(time)
    # print(min, "min", seconde, "seconde", time, "time")
    création_laser(time, min, laser, player,tetris)
    # création_missile3(time, min, missile, spawn)

    print(len(missile))
    # ----------------------------------------------------------------------------------------------------------------------------------------
    laser_suppression(laser, suppr_laser)
    for i in suppr_laser:  # despawn
        for j in range(len(laser)):
            if i == j:
                laser = laser[:i] + laser[i + 1:]
    suppr_laser = []
    # ----------------------------------------------------------------------------------------------------------------------------------------
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    player.update_hero_position()

    # ----------------------------------------------------------------------------------------------------------------------------------------
    missile_collision(missile, player)
    missile_suppression(missile, suppr_missile)
    for i in range(len(laser)):
        if laser[i].collision_laser(player) and laser[i].color == RED:
            print("dead")
            raise SystemExit

    screen.fill((0, 0, 0))
    draw_cube(walls, spawn, missile, chercheur)
    affichage(player, missile, walls, chercheur, laser)
    pygame.display.flip()
