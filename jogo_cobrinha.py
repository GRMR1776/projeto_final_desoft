import pygame
from pygame.event import Event
from pygame.locals import *
from sys import exit
from random import randint
import os



pygame.init()


diretorio_principal = os.path.dirname(__file__)
diretorio_sons = os.path.join(diretorio_principal, 'sons')

'''#musica de fundo
pygame.mixer.music.load('C:/Users/rodol/Downloads/jogo_so_meu/jogo-principal/jogos/musica/pacman.fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.01)'''



#texto
def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

#reinicia o jogo
def reiniciar():
    Largura = 1000
    altura = 500
    global pontos, comprimento, x, y, lista_cobra, lista_cabeca, x1, y1, morreu
    pontos = 0
    comprimento = 25
    x = int(Largura/2)
    y = int(altura/2)
    lista_cobra=[]
    lista_cabeca=[]
    x1 = randint(10, Largura-10)
    y1 = randint(10, altura-10)
    morreu = False


def cria_corpo(lista_cobra):
    Largura = 1000
    altura = 500
    tela = pygame.display.set_mode ((Largura, altura))
    
    for XeY in lista_cobra:
        #Xey = [x, y]
        pygame.draw.rect(tela, (255, 0, 0), (XeY[0], XeY[1], 20,20))

    


def cobrinha1(tela, relogio):
    pygame.mixer.init()

    #musica de colisao
    barulho = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))

    Largura = 1000
    altura = 500
    branco = (255, 255, 255)
    vermelho = (255, 0, 0)
    verde  = (0, 255, 0)
    azul = (0, 0, 255)
    PRETO = (0, 0, 0)

    x=Largura/2
    y=altura/2




    #funcao cria corpo
    lista_cobra = []
    comprimento = 1000


    #relogio
    relogio = pygame.time.Clock()
        


        #tela do jogo
    tela = pygame.display.set_mode ((Largura, altura))

    '''#comprimento
    compri = comprimento'''
    
    #relogio
    relogio = pygame.time.Clock()


        #pontos do jogo 
    pontos = 0
    

    #morte da cobra
    morreu = False

    #controle cobra
    velocidade = 2
    x2 = 2
    y2 =  0

     #posicao maca
    x1 = randint(50, 250)
    y1 = randint(50, 250)

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
   
        '''#posicao cobra
        x = int(Largura/2)
        y = int(altura/2)'''

        #controle
        x = x +x2
        y = y + y2


        '''#atualiza tela
        tela.fill(PRETO)'''

        
       
        
                    
        #objetos
        cobra =pygame.draw.rect(tela, (255, 0, 0), (x, y, 20, 20))
        Maça=pygame.draw.rect(tela, (0, 0, 255), (x1, y1, 20, 20))
        

        #colisao 
        if cobra.colliderect(Maça):
            x1 = randint(10, 800)
            y1 = randint(10, 400)
            pontos = pontos + 1
            barulho.play()
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
                txt2=f'Game Over'                                                               
                fonte2=pygame.font.get_default_font()              
                fontesys2=pygame.font.SysFont(fonte2, 30)           
                txttela2 = fontesys2.render(txt2, 1, (255,255,255))
                tela.blit(txttela2,(450, 200))
                txt2=f'Aperte R para reiniciar'                                                               
                fonte2=pygame.font.get_default_font()              
                fontesys2=pygame.font.SysFont(fonte2, 30)           
                txttela2 = fontesys2.render(txt2, 1, (255,255,255))
                tela.blit(txttela2,(410, 350))

                pygame.display.update()
            while morreu:
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        
           
    
        #reiniciando depois de morto
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            pontos = 0
                            comprimento = 25
                            x = int(Largura/2)
                            y = int(altura/2)
                            lista_cobra=[]
                            lista_cabeca=[]
                            x1 = randint(10, Largura-10)
                            y1 = randint(10, altura-10)
                            morreu = False
                    
                    


        #tirando o infinito da tela
    
        x = x%Largura
        y = y%altura


        #corpo cobra
        if len(lista_cobra) > comprimento:
            del lista_cobra[0]
        cria_corpo(lista_cobra)

        pygame.draw.rect(tela, (0, 0, 255), (x1, y1, 20, 20))

        txt2=f'pontos: {pontos}'                                                               
        fonte2=pygame.font.get_default_font()              
        fontesys2=pygame.font.SysFont(fonte2, 20)           
        txttela2 = fontesys2.render(txt2, 1, (255,255,255))
        tela.blit(txttela2,(10, 475))


        relogio.tick(100)
        pygame.display.update()
pygame.quit()