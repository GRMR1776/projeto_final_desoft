import pygame
from pygame import *
from jogo_cobrinha import *
from jogo_pularv1 import *


#menu do jogo
#variaveis da tela
Largura = 1000
altura = 500
branco = (255, 255, 255)
#relogio
relogio = pygame.time.Clock()

#tela do jogo
tela = pygame.display.set_mode ((Largura, altura))

botao1 = pygame.Vector2(200, altura/2) 
botao2 = pygame.Vector2(800, altura/2) 

game = True

while game:
    target = pygame.mouse.get_pos()
    pos_mouse = pygame.Vector2(target[0], target[1])
    distancia_botao1 = (pos_mouse - botao1).magnitude()
    distancia_botao2 = (pos_mouse - botao2).magnitude()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if distancia_botao2< 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            jogo2(tela, relogio)
        if distancia_botao1< 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cobrinha1(tela, relogio)
   
    tela.fill((0, 0, 0))

    
  
    txt='Snake Game'                                 
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()              
    fontesys=pygame.font.SysFont(fonte, 50)           
    txttela = fontesys.render(txt, 1, (255,255,255))
    tela.blit(txttela,(70, (altura/2)-80)) 

    txt='Jump Game'                                 
    pygame.font.init()                                
    fonte=pygame.font.get_default_font()              
    fontesys=pygame.font.SysFont(fonte, 50)           
    txttela = fontesys.render(txt, 1, (255,255,255))
    tela.blit(txttela,(700, (altura/2)-80)) 

    pygame.draw.circle(tela, (0, 255, 0), botao1, 20)
    pygame.draw.circle(tela, (0, 255, 0), botao2, 20)
    relogio.tick(36)
    pygame.display.update()
pygame.quit