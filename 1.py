import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()# частота обновления экрана
FPS.tick(60)

displaysurf = pygame.display.set_mode((300,300)) #размер экрана

color1 = pygame.Color(0,0,0) # цвета
color2 = pygame.Color(255,255,255)
color3 = pygame.Color(128,128,128)
color4 = pygame.Color(255,0,0)

object1 = pygame.Rect((20, 50),(50,100))
object2 = pygame.Rect((10,10),(100,100))

print(object1.colliderect(object2)) ## проверяет не столкнется ли объект cо вторым объектом

object1 = pygame.Rect((20,50),(50,100)) # проверяет не столкнется ли объект в этой точке
print(object1.collidepoint(50,75))

while True:# это чтобы выйти из игры
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()