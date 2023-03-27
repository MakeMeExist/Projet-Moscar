import os
import random
import pygame
from random import randint
from math import sqrt
from math import ceil
from math import acos
from math import cos
from math import sin
from math import radians

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("MOSCARLAND")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"

# --------------------couleur--------------------------------------------------------------------------------------------------------------------
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
TURQUOISE = pygame.Color(64, 224, 208)

# ---------------map-------------------------------------------------------------------------------------------------------------------------

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

# -------------------------liste---------------------------------------------------------------------------------------------------------------

missile = []
chercheur = []
suppr_missile = []
suppr_chercheur = []
direc = []
walls = []
spawn = []
laser = []
suppr_laser = []
tetris = ["barre","L","S","carre","RS","RL","T"]

# ----------------------------------------------------------------------------------------------------------------------------------------

def norm(x, y) -> float:
    return sqrt(x ** 2 + y ** 2)


# -----------------------time-----------------------------------------------------------------------------------------------------------------

time = 0
seconde = 0
min = 0
