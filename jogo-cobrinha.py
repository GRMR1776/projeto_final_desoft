import pygame
from pygame.event import Event
from pygame.locals import *
from sys import exit
from random import randint
from tela_de_inicio import *


pygame.init()
'''pygame.mixer.init()
#musica de fundo
pygame.mixer.music.load('C:/Users/rodol/Downloads/jogo_so_meu/jogo-principal/jogos/musica/pacman.fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)

#musica de colisao
barulho = pygame.mixer.Sound('C:/Users/rodol/Downloads/jogo_so_meu/jogo-principal/jogos/musica/coin.mario.mp3'''


#variaveis da tela
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


#texto
def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])


#pontos do jogo 
pontos = 0


#tela do jogo
tela = pygame.display.set_mode ((Largura, altura))


#relogio
relogio = pygame.time.Clock()
