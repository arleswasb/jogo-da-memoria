
import sys
from time import sleep
import pygame
from playsound import playsound
from pygame.locals import *
from cartas import *
from jogador import *
from config import *
#from principal import venceu
from threading import Thread


def game_play(conf):
    figura = cartas()
    jogador1 = jogador('STARDUST')
    jogador2 = jogador('MAXIMUS')
    figura.cart(conf)
    figura.imagens_cartas(conf)
    selection1 = None
    selection2 = None
    gameLoop = True
    ciclo = 0
    screen = pygame.display.set_mode(conf.abrir_tela())
    pygame.display.set_caption(conf.nome_jogo)
    pygame.display.set_icon(conf.gameIcon)
    bgImage = pygame.image.load('Background1.png')
    bgImage = pygame.transform.scale(bgImage, (conf.largura_tela, conf.altura_tela))
    bgImageRect = bgImage.get_rect()
    jogador1.jogador_ativo=True
    jogador2.jogador_ativo=False
    
    while gameLoop:
        screen.blit(bgImage, bgImageRect)
        if jogador1.jogador_ativo==True:
            conf.pontos(1,jogador1.pontos_jogador,jogador1.nome_jogador,jogador1.num_jogadas,screen)#mostra o quadro de pontos na tela
        if jogador2.jogador_ativo==True:
            conf.pontos(2,jogador2.pontos_jogador,jogador2.nome_jogador,jogador2.num_jogadas,screen)#mostra o quadro de pontos na tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ciclo +=1
                for item in figura.mem_figuraRect:
                    if item.collidepoint(event.pos):
                        if figura.imagem_oculta[figura.mem_figuraRect.index(item)] != True:
                            if selection1 != None:
                                selection2 = figura.mem_figuraRect.index(item)
                                figura.imagem_oculta[selection2] = True
                            else:
                                selection1 = figura.mem_figuraRect.index(item)
                                figura.imagem_oculta[selection1] = True
        for i in range(len(figura.cartas_memoria)):
            
            if figura.imagem_oculta[i] == True:
                screen.blit(figura.mem_figura[i], figura.mem_figuraRect[i])
            else:
                pygame.draw.rect(screen, conf.fundo, (figura.mem_figuraRect[i][0], figura.mem_figuraRect[i][1], conf.tamanho_figura, conf.tamanho_figura))
        
        pygame.display.update()

        if selection1 != None and selection2 != None:
            if figura.cartas_memoria[selection1][1] == figura.cartas_memoria[selection2][1]:
                if jogador1.jogador_ativo==True:
                    jogador1.ponto_jogador()
                if jogador2.jogador_ativo==True:
                    jogador2.ponto_jogador()
                pygame.time.wait(500)
                selection1, selection2 = None, None
                #print(jogador1.pontos_jogador,jogador2.pontos_jogador) VERIFICAÇÃO

            else:
                pygame.time.wait(500)
                figura.imagem_oculta[selection1] = False
                figura.imagem_oculta[selection2] = False
                selection1, selection2 = None, None

            if jogador1.jogador_ativo==True:
                jogador1.jogador_ativo=False
                jogador1.jogadas_jogador()
                jogador2.jogador_ativo=True
            else :
                jogador1.jogador_ativo=True
                jogador2.jogadas_jogador()
                jogador2.jogador_ativo=False

            #print(ciclo,jogador1.nome_jogador,jogador1.jogador_ativo,jogador1.num_jogadas,jogador2.nome_jogador,jogador2.jogador_ativo,jogador2.num_jogadas) VERIFICAÇÃP
            #print(jogador1.jogada_da_vez(jogador1.jogador_ativo,jogador2.jogador_ativo))VERIFICAÇÃP
        
        cont = 1
        for number in range(len(figura.imagem_oculta)):
            cont *= figura.imagem_oculta[number]
        if cont == 1:
            gameLoop = False
        #if jogador1.pontos_jogador>jogador2.pontos_jogador:
        #pygame.display.quit()
        #t1 = Thread(target=venceu(jogador1.nome_jogador))
        #t1.start()
        
        #elif jogador2.pontos_jogador>jogador1.pontos_jogador:
        #pygame.display.quit()
        #t1 = Thread(target=venceu(jogador2.nome_jogador))
        #t1.start()  
        
               
        

    
                   
