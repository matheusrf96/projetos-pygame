import pygame
import time

from pygame.locals import *

def placar(score, cor, x, y):
    font=pygame.font.Font(None,30)
    scoretext=font.render(cor+str(score), 1,(255,255,255))
    tela.blit(scoretext, (x, y))

def jogador_atacante(nome, cor):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Atacante: "+nome, 1, cor)
    tela.blit(scoretext, (220, 0))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)

atk = "Vermelho"
atk_cor = RED

pos_x = 10
pos_y = 100
v_pts = 0

pos_m = 500
pos_n = 100
a_pts = 0

atacante = "V"

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('VA3')

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

    if (pos_x >= (pos_m - 100) and pos_x <= (pos_m + 100)) and (pos_y >= (pos_n - 100) and pos_y <= (pos_n + 100)) and atacante == "V":
        v_pts += 1
        atacante = "A"
        atk = "Azul"
        atk_cor = BLUE

        pos_x = 10
        pos_y = 100

        pos_m = 500
        pos_n = 100
    elif (pos_x >= (pos_m - 100) and pos_x <= (pos_m + 100)) and (pos_y >= (pos_n - 100) and pos_y <= (pos_n + 100)) and atacante == "A":
        a_pts += 1
        atacante = "V"
        atk = "Vermelho"
        atk_cor = RED

        pos_x = 10
        pos_y = 100

        pos_m = 500
        pos_n = 100

    tela.fill(BLACK)

    placar(v_pts, "Vermelho: ", 0, 0)
    placar(a_pts, "Azul: ", 560, 0)
    jogador_atacante(atk, atk_cor)

    pygame.draw.rect(tela, RED, (pos_x, pos_y, 100, 100))
    pygame.draw.rect(tela, BLUE, (pos_m, pos_n, 100, 100))
    pygame.display.flip()