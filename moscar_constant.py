import pygame
from moscar_class import *
from random import randint

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


def draw_cube(walls, spawn, missile,chercheur):
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)

    for i in range(len(spawn)):
        pygame.draw.rect(screen, (64, 224, 208), spawn[i])
    for i in range(len(missile)):
        pygame.draw.rect(screen, (22, 225, 55), missile[i])
    for i in range(len(chercheur)):
        pygame.draw.rect(screen, (255, 23, 55), chercheur[i])


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


def création_missile(time, min, missile, spawn, direc):
    new_missile = []
    if time % 60 == 0:
        for i in range(min + 1):
            av = randint(0, len(spawn) - 1)
            b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
            new_missile.append(Missile(b, spawn[av].x, spawn[av].y, time))
        for i in range(len(new_missile)):
            n = player.rect.x // 100 - new_missile[i].rect.x // 100
            v = player.rect.y // 100 - new_missile[i].rect.y // 100
            a = [n, v]
            direc.append(a)
        missile += new_missile
    new_missile = []


def création_chercheur(time, min, chercheur, spawn):
    if time % 600 == 0:
        for i in range(min + 1):
            av = randint(0, len(spawn) - 1)
            b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
            chercheur.append(Missile(b, spawn[av].x, spawn[av].y, time))


