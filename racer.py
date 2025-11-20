import pygame
import sys
from pygame.locals import *


pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

DISPLAYSURF = pygame.display.set_mode((300,300))

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

FPS = pygame.time.Clock()
FPS.tick(60)

object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
 
print(object1.colliderect(object2))

object1 = pygame.Rect((20, 50), (50, 100))
 
print(object1.collidepoint(50, 75))