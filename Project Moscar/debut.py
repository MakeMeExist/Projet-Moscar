from rectangles import *
import VARIABLE
import pygame
image = pygame.image.load("image.png")
pygame.init()
pygame.display.set_caption("Mon super titre de Ouf !")

ecran = pygame.display.set_mode((300, 200))
# image = pygame.image.load("image.png").convert_alpha()

continuer = True

while continuer:
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()

pygame.quit()
