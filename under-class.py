#! /usr/bin/env python

import os
import random
import pygame
import timeOT
from undertales import *
from random import randint
from time import sleep

time = 0
seconde = 0
min = 0
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("MOSCARLAND")
screen = pygame.display.set_mode((640, 480))
# Combat.all_missile.draw(screen)
clock = pygame.time.Clock()
# List to hold the walls
player = Player()  # Create the player

# ----------------------------------------------------------------------------------------------------------------------------------------
# missile = []
# for i in range(10):
#     missile.append(Missile(pygame.Rect(32 + randint(i * 5, i * 15), 64 + randint(i * 5, i * 15), 6, 6)))
# ----------------------------------------------------------------------------------------------------------------------------------------
spawn = []
for i in range(17):
    spawn.append(Spawn(pygame.Rect(32 * i + 32, 32, 6, 6), -3, 3))
for i in range(15):
    spawn.append(Spawn(pygame.Rect(32, 32 * i + 32, 6, 6), - 1, 1))
for i in range(17):
    spawn.append(Spawn(pygame.Rect(32 * i + 32, 32 + 13 * 32, 6, 6), - 1, 1))
for i in range(15):
    spawn.append(Spawn(pygame.Rect(32 + 16 * 32, 32 * i + 32, 6, 6), - 1, 1))
# ----------------------------------------------------------------------------------------------------------------------------------------
missile = []
new_missile = []
direc = []
# for i in range(1):
#     a = randint(0, len(spawn) - 1)
#     b = pygame.Rect(spawn[a].rect.x, spawn[a].rect.y, 6, 6)
#     missile.append(Missile(b))
#
# for i in range(len(missile)):
#     n = player.rect.x / 100 -missile[i].rect.x / 100
#     v = player.rect.y / 100 - missile[i].rect.y / 100
#     a = [n, v]
#     direc.append(a)
# ----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------

# Holds the level layout in a list of strings.


# Parse the level string above. W = wall, E = exit
map = ["",
       "",
       "",
       "",
       "       WWWWWWWWWWWWWWWWWWWWWWW",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       W                     W",
       "       WWWWWWWWWWWWWWWWWWWWWWW",
       ]
x = y = 0
for row in map:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)
    time += 1
    if time % 60 == 0:
        seconde += 1
        time = 0
    if seconde // 60 == 1:
        min += 1
        seconde = 0
    if time % 600 == 0:
        for i in range(min + 1):
            av = randint(0, len(spawn) - 1)
            b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
            new_missile.append(Missile(b, spawn[av].x, spawn[av].y,time))
        for i in range(len(new_missile)):
            n = player.rect.x // 100 - new_missile[i].rect.x // 100
            v = player.rect.y // 100 - new_missile[i].rect.y // 100

            a = [n, v]
            direc.append(a)

        missile += new_missile
        new_missile = []
    # print(min)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-3, 0)
    if key[pygame.K_RIGHT]:
        player.move(3, 0)
    if key[pygame.K_UP]:
        player.move(0, -3)
    if key[pygame.K_DOWN]:
        player.move(0, 3)
    # ----------------------------------------------------------------------------------------------------------------------------------------
    for i in range(len(missile)):

        direction_move_x = int(direc[i][0])
        direction_move_y = int(direc[i][1])
        # if missile[i].rect.y == 0:
        #     direction_move_y = missile[i].y
        # if missile[i].rect.x == 0:
        #     direction_move_y = missile[i].x
        if missile[i].rect.x == 0 or missile[i].rect.x <= 1:
            direction_move_y, missile[i].rect.x = missile[i].y, missile[i].x

        missile[i].move(direction_move_x, direction_move_y)

        # missile[i].move(1,2)
        if player.rect.colliderect(missile[i]):
            print("dead")
            raise SystemExit
        missile[i].depart += 1
        if missile[i].depart > 60:
            missile = missile[:i] + missile[i + 1:]
            direc = direc[:i] + direc[i+1:]
    print(missile,len(missile))
    print(direc,len(direc))
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # if player.rect.colliderect(end_rect):
    #     raise SystemExit
    # mis.move(1,0)
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)

    # pygame.draw.rect(screen, (22, 225, 55), mis)
    for i in range(len(spawn)):
        pygame.draw.rect(screen, (64, 224, 208), spawn[i])
    for i in range(len(missile)):
        pygame.draw.rect(screen, (22, 225, 55), missile[i])
    pygame.display.flip()
