#! /usr/bin/env python

from constant import *


class Hero:
    def __init__(self):
        self.rect = pygame.Rect(256, 106, 16, 16)
        self.size = 16
        self.HERO_BMP = pygame.Surface((self.size, self.size))
        self.HERO_BMP.fill(BLUE)
        self.HERO_SPEED = 3
        self.x = 256
        self.y = 256
        self.pos_x = True
        self.pos_m_x = True
        self.pos_y = True
        self.pos_m_y = True

    def update_hero_position(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move(0, -self.HERO_SPEED)
        elif keys[pygame.K_DOWN]:
            self.move(0, self.HERO_SPEED)
        if keys[pygame.K_LEFT]:
            self.move(-self.HERO_SPEED, 0)
        elif keys[pygame.K_RIGHT]:
            self.move(self.HERO_SPEED, 0)

    def blit_hero(self) -> None:
        screen.blit(self.HERO_BMP, (self.x - self.size // 2, self.y - self.size // 2))

    def collision(self, objet):
        if self.x - objet.size <= objet.x < self.x + self.size \
                and self.y - objet.size <= objet.y < self.y + self.size:
            return True
        return False

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.x += dx
        self.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.collision(wall):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.x = wall.x - self.size  # - self.HERO_SPEED
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.x = wall.x + self.size - self.HERO_SPEED
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.y = wall.y - self.size
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.y = wall.y + self.size - self.HERO_SPEED


class Wall3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.wall_BMP = pygame.Surface((self.size, self.size))
        self.wall_BMP.fill((255, 255, 255))

    def blit_wall3(self) -> None:
        screen.blit(self.wall_BMP, (self.x - self.size // 2, self.y - self.size // 2))


class Enemy:
    def __init__(self, rec, HER_SPEED=5):
        self.rec = rec
        self.size = 6
        self.ENEMY_BMP = pygame.Surface((self.size, self.size))
        self.ENEMY_BMP.fill(RED)
        self.vie = 0
        self.ENEMY_SPEED = HER_SPEED * 0.8
        self.x = None
        self.y = None
        self.enemy_vx = None
        self.enemy_vy = None

    def direction4(self, her_x, her_y):
        ex = self.rec.x
        ey = self.rec.y
        dx = her_x - ex
        dy = her_y - ey
        n = norm(dx, dy)
        if n != 0:
            dx /= n
            dy /= n
        dx *= self.ENEMY_SPEED
        dy *= self.ENEMY_SPEED
        self.x, self.y, self.enemy_vx, self.enemy_vy = ex, ey, dx, dy

    def update_enemy_position(self):
        self.x, self.y = self.x + self.enemy_vx, self.y + self.enemy_vy

    def blit_enemy(self) -> None:
        screen.blit(self.ENEMY_BMP, (self.x - self.size // 2, self.y - self.size // 2))

    def collision(self, objet):
        if self.x - objet.size <= objet.x < self.x + self.size \
                and self.y - objet.size <= objet.y < self.y + self.size:
            return True
        return False


class Spawn:
    def __init__(self, rec, x_def, y_def):
        self.rect = rec
        self.x = x_def
        self.y = y_def


class Laser:
    def __init__(self, forme):
        self.forme = forme
        self.size = 50
        self.x = None
        self.y = None
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.tour = 1
        self.cube = [self.c1, self.c2, self.c3, self.c4]
        self.timer = 0
        self.color = TURQUOISE
        self.laser_BMP2 = pygame.Surface((self.size, self.size))
        self.laser_BMP2.fill(self.color)

    def forme_(self, player):
        x = player.x
        y = player.y
        s = self.size
        c1, c2, c3, c4 = None, None, None, None
        if self.forme == "barre":
            c1, c2, c3, c4 = (x - s * 1.5, y), (x - 0.5 * s, y), (x + s * 0.5, y), (x + s * 1.5, y)
            self.x, self.y = x, y

        elif self.forme == "carre":
            c1, c2, c3, c4 = (x - s * 0.5, y + s * 0.5), (x + 0.5 * s, y + s * 0.5), (x + s * 0.5, y - s * 0.5), (
                x - s * 0.5, y - s * 0.5)
        elif self.forme == "L":
            c1, c2, c3, c4 = (x, y + s * 0.5), (x, y - s * 0.5), (x + s, y - s * 0.5), \
                             (x + s * 2, y - s * 0.5)
        elif self.forme == "RS":
            c1, c2, c3, c4 = (x, y + s * 0.5), (x, y - s * 0.5), (x + s, y + s * 0.5), \
                             (x - s, y - s * 0.5)
        elif self.forme == "T":
            c1, c2, c3, c4 = (x + s, y - s * 0.5), (x - s, y - s * 0.5, y + s * 0.5), (x, y + s * 0.5), (x, y - s * 0.5)
        elif self.forme == "RL":
            c1, c2, c3, c4 = (x - s, y - s * 0.5), (x - s * 2, y - s * 0.5), (x, y + s * 0.5), (x, y - s * 0.5),
        elif self.forme == "S":
            c1, c2, c3, c4 = (x, y + s * 0.5), (x, y - s * 0.5), (x + s, y - s * 0.5), \
                             (x - s, y + s * 0.5)

        self.c1, self.c2, self.c3, self.c4 = c1, c2, c3, c4
        self.cube = [c1, c2, c3, c4]

    def rotation(self):
        if self.tour == 1:
            for i in range(len(self.cube)):
                self.cube[i] = (self.cube[i][1], self.cube[i][0])
            self.tour += 1
        elif self.tour == 2:
            for i in range(len(self.cube)):
                self.cube[i] = (self.cube[i][0], -self.cube[i][1])
            self.tour += 1
        elif self.tour == 3:
            for i in range(len(self.cube)):
                self.cube[i] = (self.cube[i][1], self.cube[i][0])
            self.tour += 1
        elif self.tour == 4:
            for i in range(len(self.cube)):
                self.cube[i] = (-self.cube[i][0], self.cube[i][1])
            self.tour = 1

    def apparition(self):
        screen.blit(self.laser_BMP2, (self.c1[0] - self.size // 2, self.c1[1] - self.size // 2))
        screen.blit(self.laser_BMP2, (self.c2[0] - self.size // 2, self.c2[1] - self.size // 2))
        screen.blit(self.laser_BMP2, (self.c3[0] - self.size // 2, self.c3[1] - self.size // 2))
        screen.blit(self.laser_BMP2, (self.c4[0] - self.size // 2, self.c4[1] - self.size // 2))
        for i in range(len(self.cube)):
            screen.blit(self.laser_BMP2, (self.cube[i][0] - self.size // 2, self.cube[i][1               ] - self.size // 2))

    def mort(self):
        self.laser_BMP2.fill(RED)
        self.color = RED

    def collision_laser(self, objet):
        for i in range(len(self.cube)):
            if self.cube[i][0] - objet.size <= objet.x < self.cube[i][0] + self.size \
                    and self.cube[i][1] - objet.size <= objet.y < self.cube[i][1] + self.size:
                return True
        return False

    def pour_rotation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rotation()
