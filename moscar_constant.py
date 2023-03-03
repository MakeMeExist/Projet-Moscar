import pygame
from moscar_class import *

player = Player()
pygame.display.set_caption("MOSCARLAND")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mape = ["",
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


def map_create(map: list):
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


def draw_cube(walls, spawn, missile):
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)

    # pygame.draw.rect(screen, (22, 225, 55), mis)
    for i in range(len(spawn)):
        pygame.draw.rect(screen, (64, 224, 208), spawn[i])
    for i in range(len(missile)):
        pygame.draw.rect(screen, (22, 225, 55), missile[i])


def process_keyboard():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-3, 0)
    if key[pygame.K_RIGHT]:
        player.move(3, 0)
    if key[pygame.K_UP]:
        player.move(0, -3)
    if key[pygame.K_DOWN]:
        player.move(0, 3)
