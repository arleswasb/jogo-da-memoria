import os
import sys
import random
import pygame

class cartas:
    def __init__(self):
        self.nome_menu=''
        self.largura_tela_menu = 600
        self.altura_tela_menu = 600
        self.mem_figura = []
        self.imagem_oculta = []
        self.mem_figuraRect = []
        self.cartas_memoria = []
        self.capas_cartas = []


    def cart(self,conf):
        
        if conf.fase == 1:
            cont=0
            for item in os.listdir('imagem_geral/imagens1/fig'):
                self.cartas_memoria.append((item.split('.')[0],cont)) #cria lista cartas_memoria
                cont+=1
            cont1=0
            for item in os.listdir('imagem_geral/imagens1/pers'):
                self.cartas_memoria.append((item.split('.')[0],cont1)) #cria lista cartas_memoria
                cont1+=1
            random.shuffle(self.cartas_memoria)
            return self.cartas_memoria
        if conf.fase == 2:
            cont=0
            for item in os.listdir('imagem_geral/imagens2/fig'):
                self.cartas_memoria.append((item.split('.')[0],cont)) #cria lista cartas_memoria
                cont+=1
            cont1=0
            for item in os.listdir('imagem_geral/imagens2/pers'):
                self.cartas_memoria.append((item.split('.')[0],cont1)) #cria lista cartas_memoria
                cont1+=1
            random.shuffle(self.cartas_memoria)
            return self.cartas_memoria
        if conf.fase == 3:
            cont=0
            for item in os.listdir('imagem_geral/imagens3/fig'):
                self.cartas_memoria.append((item.split('.')[0],cont)) #cria lista cartas_memoria
                cont+=1
            cont1=0
            for item in os.listdir('imagem_geral/imagens3/pers'):
                self.cartas_memoria.append((item.split('.')[0],cont1)) #cria lista cartas_memoria
                cont1+=1
            random.shuffle(self.cartas_memoria)
            return self.cartas_memoria

    def imagens_cartas(self,conf):
        for item in self.cartas_memoria:
            if conf.fase == 1:
                try:
                    picture = pygame.image.load(f'imagem_geral/imagens1/fig/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)
                except:
                    picture = pygame.image.load(f'imagem_geral/imagens1/pers/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)

            if conf.fase == 2:
                try:
                    picture = pygame.image.load(f'imagem_geral/imagens2/fig/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)
                except:
                    picture = pygame.image.load(f'imagem_geral/imagens2/pers/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)

            if conf.fase == 3:
                try:
                    picture = pygame.image.load(f'imagem_geral/imagens3/fig/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)
                except:
                    picture = pygame.image.load(f'imagem_geral/imagens3/pers/{item[0]}.png')
                    picture = pygame.transform.scale(picture, (conf.tamanho_figura, conf.tamanho_figura))
                    self.mem_figura.append(picture)
                    pictureRect = picture.get_rect()
                    self.mem_figuraRect.append(pictureRect)

        for i in range(len(self.cartas_memoria)):
            self.mem_figuraRect[i][0] = conf.calc_rect(i)[0]
            self.mem_figuraRect[i][1] = conf.calc_rect(i)[1]
            self.imagem_oculta.append(False)
            
    
        print(self.cartas_memoria)
        print(self.mem_figura)
        print(self.mem_figuraRect)
        print(self.imagem_oculta)
        print(conf.fase)

