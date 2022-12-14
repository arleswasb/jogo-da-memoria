import os
import random
import sys
from time import sleep
import pygame
from playsound import playsound
from pygame.locals import *
from cartas import *
from config import *
from principal import *
from game import game_play

def define_Fonte(b):
    if b == 1:
        fonte = pygame.font.SysFont('arial', 20)
        return fonte
    if b == 2:
        fonte = pygame.font.SysFont('Lucida Bright', 20)
        return fonte

def venceu(vencedor):
    running = True
    screen = pygame.display.set_mode((600, 600))
    fundo = pygame.image.load('vitoria.png')
    fundo = pygame.transform.scale(fundo, (600, 600))
    fundoRect = fundo.get_rect()
    screen.blit(fundo, fundoRect)
    while running:
        pygame.init()
        pygame.display.set_caption('MENU PRINCIPAL')
        gameIcon = pygame.image.load('icone.png')
        pygame.display.set_icon(gameIcon)
        font = pygame.font.SysFont('arial', 60)
        font1 = pygame.font.SysFont('arial', 20)
        draw_text(vencedor, font,(0, 0, 0), screen, 200, 100)
        draw_text('VOLTAR -> "Esc"', font1,(25,25,25), screen, 20, 550)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



def tela(c,conf):
    running = True
    while running:
        pygame.init()
        pygame.display.set_caption('MENU PRINCIPAL')
        gameIcon = pygame.image.load('icone.png')
        pygame.display.set_icon(gameIcon)
        font = define_Fonte(2)
        if c == 1:
            screen = pygame.display.set_mode((600, 600))

            cor_botao1 = (255, 250, 255)
            cor_botao2 = (255, 250, 255)
            cor_botao3 = (255, 250, 255)
            cor_botao4 = (255, 250, 255)
            cor_botao5 = (255, 250, 255)

            screen.fill((220, 220, 220))

            draw_text('BEM VINDO AO JOGO DA MEMORIA',font, (0, 0, 0), screen, 130, 30)
            draw_text('VAMOS JOGAR?', font, (0, 0, 0), screen, 230, 80)

            mx, my = pygame.mouse.get_pos()  # pega as coordenadas do mouse

            button_1 = pygame.Rect(210, 180, 200, 50)

            button_2 = pygame.Rect(210, 250, 200, 50)

            button_3 = pygame.Rect(210, 320, 200, 50)

            button_4 = pygame.Rect(210, 390, 200, 50)

            button_5 = pygame.Rect(210, 460, 200, 50)

            if button_1.collidepoint((mx, my)):
                cor_botao1 = (255, 200, 0)
                if click:
                    pygame.display.quit()
                    game_play(conf)
                     
            if button_2.collidepoint((mx, my)):
                cor_botao2 = (255, 200, 0)
                if click:
                    sub_tela(2,conf)
            if button_3.collidepoint((mx, my)):
                cor_botao3 = (255, 200, 0)
                if click:
                    sub_tela(3,conf)
            if button_4.collidepoint((mx, my)):
                cor_botao4 = (255, 200, 0)
                if click:
                    sub_tela(4,conf)
            if button_5.collidepoint((mx, my)):
                cor_botao5 = (255, 200, 0)
                if click:
                    pygame.quit()
                    sys.exit()

            click = False

            pygame.draw.rect(screen, cor_botao1, button_1)
            draw_text('PLAY', font, (0, 0, 0), screen, 285, 190)
            pygame.draw.rect(screen, cor_botao2, button_2)
            draw_text('INSTRU????ES', font, (0, 0, 0), screen, 250, 260)
            pygame.draw.rect(screen, cor_botao3, button_3)
            draw_text('CR??DITOS', font, (0, 0, 0), screen, 260, 330)
            pygame.draw.rect(screen, cor_botao4, button_4)
            draw_text('CONFIGURA????O', font, (0, 0, 0), screen, 225, 400)
            pygame.draw.rect(screen, cor_botao5, button_5)
            draw_text('SAIR', font, (0, 0, 0), screen, 285, 470)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            mainClock.tick(60)

def sub_tela(d,conf):
       
    if d == 2:
        running = True
        screen = pygame.display.set_mode((600, 600))
        while running:
            screen.fill((0, 0, 0))
            font = define_Fonte(1)
            draw_text('VOLTAR -> "Esc"', font,(255, 0, 0), screen, 20, 550)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
            mainClock.tick(60)
    if d == 3:
        running = True
        screen = pygame.display.set_mode((600, 600))
        bgImage = pygame.image.load('fundo_creditos1.jpg')
        bgImage = pygame.transform.scale(bgImage, (600, 600))
        bgImageRect = bgImage.get_rect()
        screen.blit(bgImage, bgImageRect)
        while running:
           
            font = define_Fonte(2)
            draw_text('PROGRAMADOR:', font, (255, 0, 0), screen, 20, 20)
            draw_text('Aluno: - Werbert Arles de Souza Barradas',font, (25, 25, 25), screen, 20, 60)
                
            draw_text('Graduando em Engenharia Mecatr??nica',font, (25, 25, 25), screen, 105, 90)
            draw_text('COLABORADORES:', font, (255, 0, 0), screen, 20, 120)
            draw_text('MONITOR 1 DE EXPRESS??O GRAFICA',font, (25, 25, 25), screen, 20, 160)
            draw_text('Graduando em XXXXXXXXXX', font,(25, 25, 25), screen, 105, 190)
            draw_text('MONITOR 1 DE EXPRESS??O GRAFICA',font, (25, 25, 25), screen, 20, 220)
            draw_text('Graduando em XXXXXX', font,(25, 25, 25), screen, 105, 250)
            draw_text('ORIENTADOR:', font, (255, 0, 0), screen, 20, 320)
            draw_text('Prof. Doutor Everton Santi', font,(25, 25, 25), screen, 20, 360)
            draw_text('Doutor em Engenharia da Computa????o',font, (25, 25, 25), screen, 105, 400)
            draw_text('VOLTAR -> "Esc"', font,(25, 25, 25), screen, 20, 550)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(60)
    
    if d == 4:
        running = True
        screen = pygame.display.set_mode((600, 600))
        bgImage = pygame.image.load('fundo_creditos1.jpg')
        bgImage = pygame.transform.scale(bgImage, (600, 600))
        bgImageRect = bgImage.get_rect()
        screen.blit(bgImage, bgImageRect)

        cor_circulo_marcado = (255, 0, 0)
        cor_circulo_int1 = (255, 0, 0)
        cor_circulo_int2 = (0, 0, 255)
        cor_circulo_int3 = (0, 0, 255)
        cor_quadrado = (0, 0, 255)
        

        while running:
           
            font = define_Fonte(2)
            draw_text('SELECIONE A FASE DO JOGO', font, (255, 0, 0), screen, 150, 80)
            draw_text('FASE 1 - INICIANTE',font, (25, 25, 25), screen, 60, 180)
            draw_text('FASE 2 - INTERMEDI??RIO',font, (25, 25, 25), screen, 60, 240)
            draw_text('FASE 3 - AVAN??ADO', font, (25, 25, 25), screen, 60, 300)

            mx, my = pygame.mouse.get_pos()  # pega as coordenadas do mouse

            quadrado_1 = pygame.Rect(440, 185, 20, 20)

            quadrado_2 = pygame.Rect(440, 245, 20, 20)

            quadrado_3 = pygame.Rect(440, 305, 20, 20)
           
            
            pygame.draw.rect(screen, cor_quadrado, quadrado_1)
            pygame.draw.circle(screen, cor_circulo_int1, (450, 195), 5, 0)
            pygame.draw.rect(screen, cor_quadrado, quadrado_2)
            pygame.draw.circle(screen, cor_circulo_int2, (450, 255), 5, 0)
            pygame.draw.rect(screen, cor_quadrado, quadrado_3)
            pygame.draw.circle(screen, cor_circulo_int3, (450, 315), 5, 0)
            
            if quadrado_1.collidepoint((mx, my)):
                if click:
                    if cor_circulo_int1 == (0, 0, 255):
                        cor_circulo_int1 = cor_circulo_marcado
                        cor_circulo_int2 = (0, 0, 255)
                        cor_circulo_int3 = (0, 0, 255)
                        conf.fase = 1
            if quadrado_2.collidepoint((mx, my)):
                if click:
                    if cor_circulo_int2 == (0, 0, 255):
                        cor_circulo_int2 = cor_circulo_marcado
                        cor_circulo_int1 = (0, 0, 255)
                        cor_circulo_int3 = (0, 0, 255)
                        conf.fase = 2
            if quadrado_3.collidepoint((mx, my)):
                if click:
                    if cor_circulo_int3 == (0, 0, 255):
                        cor_circulo_int3 = cor_circulo_marcado
                        cor_circulo_int1 = (0, 0, 255)
                        cor_circulo_int2 = (0, 0, 255)
                        conf.fase = 3
            click = False
            draw_text('VOLTAR -> "Esc"', font,(255,0, 0), screen, 20, 550)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            mainClock.tick(60)
mainClock = pygame.time.Clock()              

conf = Configuracao()
tela(1,conf)
