import pygame
from random import randint
from math import sqrt

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
HERO_SIZE = 50
HERO_BMP = pygame.Surface((HERO_SIZE, HERO_SIZE))
HERO_BMP.fill(BLUE)
HERO_SPEED = 10
hero_x = SCREEN_WIDTH // 2
hero_y = SCREEN_HEIGHT // 2
CLOCK = pygame.time.Clock()

ENEMY_SIZE = 10
ENEMY_SPEED = HERO_SPEED * 0.7999

enemy_x = None
enemy_y = None
enemy_vx = None
enemy_vy = None
ENEMY_BMP = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
ENEMY_BMP.fill(RED)


def norm(x, y):
    return sqrt(x ** 2 + y ** 2)


def spawn():
    ex = randint(0, SCREEN_WIDTH)
    ey = randint(0, SCREEN_HEIGHT)
    dx = hero_x - ex
    dy = hero_y - ey
    n = norm(dx, dy)
    if n != 0:
        dx /= n
        dy /= n
    dx *= ENEMY_SPEED
    dy *= ENEMY_SPEED
    return ex, ey, dx, dy


def blit_hero(x, y) -> None:
    screen.blit(HERO_BMP, (x - HERO_SIZE // 2, y - HERO_SIZE // 2))


def blit_enemy(x, y) -> None:
    screen.blit(ENEMY_BMP, (x - ENEMY_SIZE // 2, y - ENEMY_SIZE // 2))


def update_hero_position():
    new_x, new_y = hero_x, hero_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        new_y = hero_y - HERO_SPEED
    elif keys[pygame.K_DOWN]:
        new_y = hero_y + HERO_SPEED

    return new_x, new_y


def update_enemy_position():
    return enemy_x + enemy_vx, enemy_y + enemy_vy


enemy_x, enemy_y, enemy_vx, enemy_vy = spawn()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
go_on = True
counter = 0
while go_on:
    hero_x, hero_y = update_hero_position()
    enemy_x, enemy_y = update_enemy_position()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go_on = False
        if e.type == pygame.KEYDOWN:
            enemy_x, enemy_y, enemy_vx, enemy_vy = spawn()

    hero_x, hero_y = update_hero_position()
    enemy_x, enemy_y = update_enemy_position()

    screen.fill(BLACK)
    blit_hero(hero_x, hero_y)
    blit_enemy(enemy_x, enemy_y)
    pygame.display.update()
    CLOCK.tick(30)

pygame.quit()
