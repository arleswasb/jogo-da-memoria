
import sys
from time import sleep
import pygame
from playsound import playsound
from pygame.locals import *
from cartas import *
from jogador import *
from config import *
from threading import Thread


def game_play(conf):

    #passagens dos parametros utilizados na função

    figura = cartas()
    jogador1 = jogador('EQUIPE 01')
    jogador2 = jogador('EQUIPE 02')
    figura.cart(conf)
    figura.imagens_cartas(conf)
    selection1 = None
    selection2 = None
    gameLoop = True
    ciclo = 0

    #criação da tela principal do jogo

    screen = pygame.display.set_mode(conf.abrir_tela())
    pygame.display.set_caption(conf.nome_jogo)
    pygame.display.set_icon(conf.gameIcon)
    bgImage = pygame.image.load('Background1.png')
    bgImage = pygame.transform.scale(
    bgImage, (conf.largura_tela, conf.altura_tela))
    bgImageRect = bgImage.get_rect()
    jogador1.jogador_ativo = True
    jogador2.jogador_ativo = False
    font = pygame.font.SysFont('Lucida Bright', 20)
    screen.blit(bgImage, bgImageRect)

    #inicia o loop do jogo

    while gameLoop:

        conf.pontos(1, jogador1.pontos_jogador, jogador1.nome_jogador, jogador1.num_jogadas,
                    screen, jogador1.jogador_ativo)  # mostra o quadro de pontos na tela
        
        conf.pontos(2, jogador2.pontos_jogador, jogador2.nome_jogador, jogador2.num_jogadas,
                    screen, jogador2.jogador_ativo)  # mostra o quadro de pontos na tela
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #verifica qual carta foi clicada e aberta

                ciclo += 1 #variavel que conta as vezes que cada jogador jogou
                # verifica qual carta foi clicada pelo jogador e indica com true que a carta foi virada
                for item in figura.mem_figuraRect:
                    if item.collidepoint(event.pos):
                        if figura.imagem_oculta[figura.mem_figuraRect.index(item)] != True:
                            if selection1 != None:
                                selection2 = figura.mem_figuraRect.index(item)#identifica a carta 1
                                figura.imagem_oculta[selection2] = True
                            else:
                                selection1 = figura.mem_figuraRect.index(item)#identifica a carta dois
                                figura.imagem_oculta[selection1] = True

        for i in range(len(figura.cartas_memoria)):

            if figura.imagem_oculta[i] == True:
                screen.blit(figura.mem_figura[i], figura.mem_figuraRect[i])#vira a carta identificada anteriormente
            else:#desvira a carta quando o jogador não acerta
                pygame.draw.rect(screen, conf.fundo, (
                    figura.mem_figuraRect[i][0], figura.mem_figuraRect[i][1], conf.tamanho_figura, conf.tamanho_figura))

        pygame.display.update()

        if selection1 != None and selection2 != None:
            if figura.cartas_memoria[selection1][1] == figura.cartas_memoria[selection2][1]:
                if jogador1.jogador_ativo == True:
                    jogador1.ponto_jogador()#acrescenta ponto ao jogador da vez
                if jogador2.jogador_ativo == True:
                    jogador2.ponto_jogador()#acrescenta ponto ao jogador da vez
                pygame.time.wait(500)
                selection1, selection2 = None, None #zera o indentificador das cartas para uma nova jogada

            else:#caso não acerte as cartas marca as cartas como falsa
                pygame.time.wait(500)
                figura.imagem_oculta[selection1] = False
                figura.imagem_oculta[selection2] = False
                selection1, selection2 = None, None #zera o indentificador das cartas para uma nova jogada

            #identifica qual jogador esta na vez de jogar

            if jogador1.jogador_ativo == True:
                jogador1.jogador_ativo = False
                jogador1.jogadas_jogador()#soma o numero de jogadas de cada jogador
                jogador2.jogador_ativo = True
            else:
                jogador1.jogador_ativo = True
                jogador2.jogadas_jogador()#soma o numero de jogadas de cada jogador
                jogador2.jogador_ativo = False

            # print(ciclo,jogador1.nome_jogador,jogador1.jogador_ativo,jogador1.num_jogadas,jogador2.nome_jogador,jogador2.jogador_ativo,jogador2.num_jogadas) VERIFICAÇÃP
            # print(jogador1.jogada_da_vez(jogador1.jogador_ativo,jogador2.jogador_ativo))VERIFICAÇÃP

        cont = 1
        for number in range(len(figura.imagem_oculta)):
            cont *= figura.imagem_oculta[number]
        cont = 1
        if cont == 1:
            # exibe a tela com o nome do vencedor
            if jogador1.pontos_jogador > jogador2.pontos_jogador:
                picture = pygame.image.load('vitoria.png')
                picture = pygame.transform.scale(picture, (405, 250))
                screen.blit(picture, (15, 350, 440, 300))
                draw_text(jogador1.nome_jogador, font,
                          (255, 0, 0), screen, 170, 395)
            else:
                picture = pygame.image.load('vitoria.png')
                picture = pygame.transform.scale(picture, (405, 250))
                screen.blit(picture, (15, 350, 440, 300))
                draw_text(jogador2.nome_jogador, font,
                          (0, 0, 0), screen, 170, 395)
                draw_text('VOLTAR -> "Esc"', font,
                          (255, 200, 0), screen, 20, 650)

            pygame.time.wait(500)
