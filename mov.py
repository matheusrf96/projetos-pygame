import pygame
import time

from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

pos_x = 10
pos_y = 100

pos_m = 500
pos_n = 100

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Meu primeiro programa!')

# pygame.draw.circle(tela, RED, (x, y), 10, width=0)

while True:
    for evento in pygame.event.get():
        pass
    teclas = pygame.key.get_pressed()

    if teclas[K_RIGHT]:
        if pos_x < 540:
            pos_x += 1
    elif teclas[K_LEFT]:
        if pos_x != 0:
            pos_x -= 1
    elif teclas[K_DOWN]:
        if pos_y != 380:
            pos_y += 1 
    elif teclas[K_UP]:
        if pos_y != 0:
            pos_y -= 1 

    if teclas[K_d]:
        if pos_m < 540:
            pos_m += 1
    elif teclas[K_a]:
        if pos_m != 0:
            pos_m -= 1
    elif teclas[K_s]:
        if pos_n != 380:
            pos_n += 1 
    elif teclas[K_w]:
        if pos_n != 0:
            pos_n -= 1 

    tela.fill(BLACK)
    pygame.draw.rect(tela, RED, (pos_x, pos_y, 100, 100))
    pygame.draw.ellipse(tela, BLUE, (pos_m, pos_n, 100, 100))
    pygame.display.flip()