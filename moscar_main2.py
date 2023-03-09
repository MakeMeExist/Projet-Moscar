import pygame
from random import randint
from math import sqrt

BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

CLOCK = pygame.time.Clock()


# enemy_x = None
# enemy_y = None
# enemy_vx = None
# enemy_vy = None


class Hero:
    def __init__(self):
        self.size = 50
        self.HERO_BMP = pygame.Surface((self.size, self.size))
        self.HERO_BMP = self.HERO_BMP.fill(BLUE)
        self.HERO_SPEED = 10
        self.hero_x = SCREEN_WIDTH // 2
        self.hero_y = SCREEN_HEIGHT // 2

    def update_hero_position(self):
        new_x, new_y = self.hero_x, self.hero_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            new_y = self.hero_y - self.HERO_SPEED
        elif keys[pygame.K_DOWN]:
            new_y = self.hero_y + self.HERO_SPEED
        if keys[pygame.K_LEFT]:
            new_x = self.hero_x - self.HERO_SPEED
        elif keys[pygame.K_RIGHT]:
            new_x = self.hero_x + self.HERO_SPEED
        self.hero_x, self.hero_y = new_x, new_y

    def blit_hero(self) -> None:
        screen.blit(self.HERO_BMP, (self.hero_x - self.size // 2, self.hero_y - self.size // 2))


class Enemy:
    def __init__(self, HER_SPEED):
        self.size = 50
        self.ENEMY_BMP = pygame.Surface((self.size, self.size))
        self.ENEMY_BMP = self.ENEMY_BMP.fill(RED)
        self.ENEMY_SPEED = HER_SPEED * 0.8
        self.enemy_x = None
        self.enemy_y = None
        self.enemy_vx = None
        self.enemy_vy = None

    def direction4(self, her_x, her_y):
        ex = randint(0, SCREEN_WIDTH)
        ey = randint(0, SCREEN_HEIGHT)
        dx = her_x - ex
        dy = her_y - ey
        n = norm(dx, dy)
        if n != 0:
            dx /= n
            dy /= n
        dx *= self.ENEMY_SPEED
        dy *= self.ENEMY_SPEED
        # self.move(ex + dx, ey + dy)
        self.enemy_x, self.enemy_y, self.enemy_vx, self.enemy_vy = ex, ey, dx, dy
        # self.enemy_vx, self.enemy_vy = dx, dy

    def update_enemy_position(self):
        self.enemy_x, self.enemy_y = self.enemy_x + self.enemy_vx, self.enemy_y + self.enemy_vy

    def blit_enemy(self) -> None:
        screen.blit(self.ENEMY_BMP, (self.enemy_x - self.size // 2, self.enemy_y - self.size // 2))

    def collision(self, objet):
        if self.enemy_x - objet.size <= objet.hero_x < self.enemy_x + self.size \
                and self.enemy_y - objet.size <= objet.hero_y < self.enemy_x + self.size:
            return True
        return False


def norm(x, y):
    return sqrt(x ** 2 + y ** 2)


moi = Hero()
truc = Enemy(moi.HERO_SPEED)

truc.direction4(moi.hero_x, moi.hero_y)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
go_on = True
counter = 0
while go_on:
    moi.update_hero_position()
    truc.update_enemy_position()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go_on = False
        if e.type == pygame.KEYDOWN:
            truc.direction4(moi.hero_x, moi.hero_y)
    if truc.collision(moi) == True:
        print("You're dead !")
    # hero_x, hero_y = update_hero_position()
    # enemy_x, enemy_y = update_enemy_position()

    screen.fill(BLACK)
    print(type(truc.ENEMY_BMP),type(moi.HERO_BMP))
    # moi.blit_hero()
    # truc.blit_enemy()
    pygame.display.update()
    CLOCK.tick(30)

pygame.quit()
