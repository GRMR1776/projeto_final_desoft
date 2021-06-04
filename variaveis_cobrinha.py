import pygame
from random import *

Largura = 1000
altura = 500
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde  = (0, 255, 0)
azul = (0, 0, 255)
PRETO = (0, 0, 0)




#funcao cria corpo
lista_cobra = []
comprimento = 10


#relogio
relogio = pygame.time.Clock()
    


    #tela do jogo
tela = pygame.display.set_mode ((Largura, altura))


