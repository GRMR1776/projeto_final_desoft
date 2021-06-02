import pygame
from random import *

Largura = 1000
altura = 500
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde  = (0, 255, 0)
azul = (0, 0, 255)
PRETO = (0, 0, 0)


    #posicao cobra
x = int(Largura/2)
y = int(altura/2)


    #posicao maca
x1 = randint(10, 800)
y1 = randint(10, 400)


    #controle cobra
velocidade = 2
x2 = velocidade 
y2 =  0

    #funcao cria corpo
lista_cobra = []
comprimento = 10


#relogio
relogio = pygame.time.Clock()
    


    #tela do jogo
tela = pygame.display.set_mode ((Largura, altura))


