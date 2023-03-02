import pygame
from classe import *
from moviepy.editor import *
SCREEN_WIDTH, SCREEN_HEIGHT = 1200,600

n_ligne = 11
n_colone = 17

pos_case_x2 = 20
pos_case_y2 = 20

longeur_case = 50
hauteur_case = 50

# Creation des couleurs pour les cases :
RED = pygame.Color("#FF0000")
COLOR = pygame.Color(100, 100, 150)
BLACK = pygame.Color(0)
WHITE = pygame.Color(255,255,255)# ou "#FFFFFF"
GREY = pygame.Color("#7F7F7F")
BLUE = pygame.Color("#AEACE2")
# Laod des images
pion = pygame.image.load("assets/gfx/Pion2.png")
character = pygame.image.load("assets/gfx/Pion2.png")
icon = pygame.image.load("assets/gfx/demon4.png")
you_win = pygame.image.load("assets/gfx/victory.jpg")
fleche_droite = pygame.image.load("assets/gfx/flechedroite.png")
fleche_gauche = pygame.image.load("assets/gfx/flechegauche.png")
you_died = pygame.image.load("assets/gfx/you_died.png")
again = pygame.image.load("assets/gfx/again.png")
black = pygame.image.load("assets/gfx/black.jpg")
status = pygame.image.load("assets/gfx/status2.png")
#starting screen
debut_background = pygame.image.load("assets/gfx/debutbackground2.jpg")
start_button = pygame.image.load("assets/gfx/startsao2.png")

#Redimensionnement des images
again = pygame.transform.smoothscale(again, (SCREEN_WIDTH,100))
you_died = pygame.transform.smoothscale(you_died,(SCREEN_WIDTH,200))
you_win = pygame.transform.smoothscale(you_win,(SCREEN_WIDTH,SCREEN_HEIGHT))
black = pygame.transform.smoothscale(black,(SCREEN_WIDTH,SCREEN_HEIGHT))
pion = pygame.transform.smoothscale(pion,(100,100))#redimmensionne le pion
character = pygame.transform.smoothscale(character,(50,50))
icon = pygame.transform.smoothscale(icon,(50,50))
position_flechedroite = (750, 100)
taille_flechedroite = (100,100)
position_flechegauche = (500, 100)
taille_flechegauche = (100,100)
fleche_droite = pygame.transform.smoothscale(fleche_droite, taille_flechedroite)
fleche_gauche = pygame.transform.smoothscale(fleche_gauche, taille_flechegauche)

status = pygame.transform.smoothscale(status,(200,400))
debut_background = pygame.transform.smoothscale(debut_background,(SCREEN_WIDTH,SCREEN_HEIGHT))
taille_start_button = 200
start_button = pygame.transform.smoothscale(start_button,(taille_start_button,taille_start_button))

#Importe les sons
soundcreeper = pygame.mixer.Sound('assets/snd/creeper-minecraft-m-sound-effect.mp3')
soundbamboo = pygame.mixer.Sound("assets/snd/bamboo-hit-sound-effect.mp3")
notdiscord = pygame.mixer.Sound("assets/snd/discord-notification-sound-effect.mp3")
wow_you_win = pygame.mixer.Sound("assets/snd/victory-sound-effect.mp3")


#importe les vidéos
clip = VideoFileClip("assets/vid/link_start.mp4").resize((SCREEN_WIDTH, SCREEN_HEIGHT))


L1 = []
L2 = []
compteur = 0
compteur_notdiscord = 0




screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)
screen.fill(WHITE)
sprite = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
status_sprite = pygame.Surface((200,400))

