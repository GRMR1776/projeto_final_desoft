import pygame
from pygame.event import Event
from pygame.locals import *
from sys import exit
from random import randint
from variaveis_cobrinha import *


pygame.init()
'''pygame.mixer.init()

#musica de fundo
pygame.mixer.music.load('C:/Users/rodol/Downloads/jogo_so_meu/jogo-principal/jogos/musica/pacman.fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)

#musica de colisao
barulho = pygame.mixer.Sound('C:/Users/rodol/Downloads/jogo_so_meu/jogo-principal/jogos/musica/coin.mario.mp3'''

#texto
def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

#reinicia o jogo
def reiniciar():
    global pontos, comprimento, x, y, lista_cobra, lista_cabeca, x1, y1, morreu
    pontos = 0
    comprimento = 25
    x = int(Largura/2)
    y = int(altura/2)
    lista_cobra=[]
    lista_cabeca=[]
    x1 = randint(10, 800)
    y1 = randint(10, 400)
    morreu = False


def cria_corpo(lista_cobra):
    for XeY in lista_cobra:
        #Xey = [x, y]
        pygame.draw.rect(tela, (255, 0, 0), (XeY[0], XeY[1], 20,20))


def cobrinha1(tela, relogio):
    
    #relogio
    relogio = pygame.time.Clock()


        #pontos do jogo 
    pontos = 0


    #morte da cobra
    morreu = False

    #loop

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False


        #movimento controlado do objeto
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if x2 == velocidade:
                        pass
                    else:
                        x2 = - velocidade
                        y2 = 0
                if event.key == K_d:
                    if x2 == - velocidade:
                        pass
                    else:
                        x2 = velocidade
                        y2 = 0
                if event.key == K_w:
                    if y2 == velocidade:
                        pass
                    else:
                        y2 = - velocidade
                        x2 = 0
                if event.key == K_s:
                    if y2 == - velocidade:
                        pass
                    else:
                        y2 = velocidade
                        x2 = 0 
   
   
        #controle
        x = x +x2
        y = y + y2


        #atualiza tela
        tela.fill(PRETO)


        #texto
        texto(tela, f"pontos: {pontos}", branco, 20, 10, altura - 20)
    


                    
        #objetos
        cobra =pygame.draw.rect(tela, (255, 0, 0), (x, y, 20, 20))
        Maça=pygame.draw.rect(tela, (0, 0, 255), (x1, y1, 20, 20))


        #colisao 
        if cobra.colliderect(Maça):
            x1 = randint(10, 800)
            y1 = randint(10, 400)
            pontos = pontos + 1
            #barulho.play()
            comprimento = comprimento +10

        #corpocobra
        lista_cabeca = []
        lista_cabeca.append(x)
        lista_cabeca.append(y)
        lista_cobra.append(lista_cabeca)

        
        #morte cobra
        if lista_cobra.count(lista_cabeca) > 1:
            morreu = True
            if morreu == True:
                texto(tela, "GAME OVER", branco, 50, (Largura/2)-100,  altura/2)
                texto(tela, "aperte R para reiniciar", branco, 50, (Largura/2)-180,  (altura/2)+100)

                pygame.display.update()
            while morreu:
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        
           
    
        #reiniciando depois de morto
                    if event.type == KEYDOWN:
                            if event.key == K_r:
                                reiniciar()
                    
                    


        #tirando o infinito da tela
    
        x = x%Largura
        y = y%altura


        #corpo cobra
        if len(lista_cobra) > comprimento:
            del lista_cobra[0]
        cria_corpo(lista_cobra)


        relogio.tick(100)
        pygame.display.update()
pygame.quit()