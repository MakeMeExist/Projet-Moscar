from classe import *

player = Hero()


def map_create2(map: list, walls: list):
    x = y = 0
    for row in map:
        for col in row:
            if col == "W":
                walls.append(Wall3(x, y))
            x += 16
        y += 16
        x = 0


def draw_cube(walls, spawn, missile, chercheur):
    # pygame.draw.rect(screen, (255, 200, 0), player.rect)
    # for wall in walls:
    #     walls[wall].blit_wall3()
    # pygame.draw.rect(screen, (255, 255, 255), wall.rect)

    # pygame.draw.rect(screen, (255, 0, 0), end_rect)

    for i in range(len(spawn)):
        pygame.draw.rect(screen, (64, 224, 208), spawn[i])
    # for i in range(len(missile)):
    #     pygame.draw.rect(screen, (22, 225, 55), missile[i])
    # for i in range(len(chercheur)):
    #     pygame.draw.rect(screen, (255, 23, 55), chercheur[i])


def création_missile3(time, min, missile, spawn):
    new_missile = []
    if time % 60 == 0:
        for i in range(min + 1):
            av = randint(0, len(spawn) - 1)
            b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
            new_missile.append(Enemy(b))
        for i in range(len(new_missile)):
            new_missile[i].direction4(player.x, player.y)
        missile += new_missile
        new_missile = []


def création_chercheur2(time, min, chercheur, spawn):
    new_missile = []
    if time % 60 == 0:
        for i in range(min + 1):
            av = randint(0, len(spawn) - 1)
            b = pygame.Rect(spawn[av].rect.x, spawn[av].rect.y, 6, 6)
            new_missile.append(Enemy(b))
        for i in range(len(new_missile)):
            new_missile[i].direction4(player.x, player.y)
        chercheur += new_missile
        new_missile = []


def generation_spawn(spawn):
    for i in range(17):
        spawn.append(Spawn(pygame.Rect(32 * (i + 1) + 0, 0, 6, 6), -3, 3))
    for i in range(15):
        spawn.append(Spawn(pygame.Rect(32, 32 * i + 32, 6, 6), - 1, 1))
    for i in range(17):
        spawn.append(Spawn(pygame.Rect(32 * (i + 1) + 0, 64 + 13 * 32, 6, 6), - 1, 1))
    for i in range(15):
        spawn.append(Spawn(pygame.Rect(32 + 16 * 32, 32 * i + 32, 6, 6), - 1, 1))


def my_timer(time):
    global seconde, min
    if time % 60 == 0:
        seconde += 1
    if seconde // 60 == 1:
        min += 1
        seconde = 0


def missile_collision(missile, player):
    for i in range(len(missile)):
        missile[i].update_enemy_position()
        if missile[i].collision(player):
            print("dead")
            raise SystemExit


def missile_suppression(missile, suppr_missile):
    for i in range(len(missile)):
        missile[i].vie += 1
        if missile[i].vie > 70:
            suppr_missile.append(i)
    for i in suppr_missile:  # despawn
        for j in range(len(missile)):
            if i == j:
                missile = missile[:i] + missile[i + 1:]
    suppr_missile = []


def laser_suppression(laser, suppr_laser):
    for i in range(len(laser)):
        laser[i].timer += 1
        if laser[i].timer >= 100:
            laser[i].mort()
    for i in range(len(laser)):
        if laser[i].timer >= 140:
            suppr_laser.append(i)


def affichage(player, missile, walls, chercheur, laser):
    for i in range(len(laser)):
        laser[i].apparition()
    player.blit_hero()
    for i in range(len(missile)):
        missile[i].blit_enemy()
    for i in range(len(walls)):
        walls[i].blit_wall3()
    for i in range(len(chercheur)):
        chercheur[i].blit_enemy()


def création_laser(time, min, laser, player, tetris):
    new_missile = []
    if time % 300 == 0:
        a = randint(0, len(tetris)-1)
        a = tetris[a]

        lazer = Laser(a)
        lazer.forme_(player)
        laser.append(lazer)
