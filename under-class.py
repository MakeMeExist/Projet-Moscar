#! /usr/bin/env python

import os
import random
import pygame
from undertales import *
from random import randint

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((640, 480))
# Combat.all_missile.draw(screen)
clock = pygame.time.Clock()
# List to hold the walls
player = Player()  # Create the player
missile1 = Missile(pygame.Rect(32, 64, 6, 6))
# Holds the level layout in a list of strings.


# Parse the level string above. W = wall, E = exit
map = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W               E  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW",

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

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    missile1.move(randint(-3, 5), randint(-2, 2))
    if player.rect.colliderect(end_rect):
        raise SystemExit
    if player.rect.colliderect(missile1):
        print("dead")
        raise SystemExit
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (22, 225, 55), missile1)
    pygame.display.flip()
