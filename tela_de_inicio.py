import pygame
from jogo_cobrinha import *



#menu do jogo
#variaveis da tela
Largura = 1000
altura = 500

#relogio
relogio = pygame.time.Clock()

#tela do jogo
tela = pygame.display.set_mode ((Largura, altura))

centro = pygame.Vector2(Largura/2, altura/2) 

game = True

while game:
    target = pygame.mouse.get_pos()
    pos_mouse = pygame.Vector2(target[0], target[1])
    distancia_ao_centro = (pos_mouse - centro).magnitude()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            cobrinha1(tela, relogio)
        if distancia_ao_centro < 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cobrinha1(tela, relogio)
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (0, 255, 0), centro, 20)
    relogio.tick(36)
    pygame.display.update()
pygame.quit()