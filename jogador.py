import os
import sys
import random
import pygame
from playsound import playsound
from pygame.locals import *

class jogador:
    def __init__(self,nome):
        self.nome_jogador = nome
        self.num_jogadas = 0
        self.pontos_jogador = 0
        self.jogador_ativo = True
        self.vencedor = False

    def ponto_jogador(self):
        if self.jogador_ativo == True:
            self.pontos_jogador += 10


    def jogadas_jogador(self):
            self.num_jogadas += 1

    
    def jogada_da_vez(self,jogador1):
        if jogador1==True:
                self.jogador_ativo = False
        else:
             self.jogador_ativo=True

        

        



