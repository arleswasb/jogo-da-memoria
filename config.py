
import pygame
from playsound import playsound


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Configuracao:
    def __init__(self, a=1500, b=800, c=190, col=5, lin=4, fundo=(200, 255, 200), fase=1):
        self.largura_tela = a
        self.altura_tela = b
        self.tamanho_figura = c
        self.nome_jogo = "JOGO DA MEMORIA"
        self.fase = int(fase)
        self.gameIcon = pygame.image.load('icone.png')
        self.coluna_cartas = col
        self.linha_cartas = lin
        self.entrelinhas = 5
        self.margem_esquerda = (
            (self.largura_tela) - ((self.tamanho_figura + self.entrelinhas - 80) * self.coluna_cartas)) // 2
        self.margem_direita = self.margem_esquerda
        self.margem_superior = (
            (self.altura_tela) - ((self.tamanho_figura + self.entrelinhas) * self.linha_cartas)) // 2
        self.margem_inferior = self.margem_superior
        self.fundo = fundo

    def pontos(self, a, b, c, d, screen, e):
        font = pygame.font.SysFont('Lucida Bright', 20)
        if e == True:
            cor = (255, 200, 0)
        else:
            cor = (255, 255, 255)
        if a == 1:
            pygame.draw.rect(screen, cor, (15, 10, 440, 100))
            draw_text('JOGADOR  :', font, (25, 25, 25), screen, 20, 20)
            draw_text(c, font, (25, 25, 25), screen,
                      160, 20)  # nome do jogador
            draw_text('PONTOS:', font, (25, 25, 25), screen, 160, 50)
            draw_text(str(b), font, (25, 25, 25), screen, 260, 50)  # pontuação
            draw_text('N° JOGADAS:', font, (25, 25, 25), screen, 160, 80)
            draw_text(str(d), font, (25, 25, 25), screen,
                      300, 80)  # numero de jogadas

        if a == 2:
            pygame.draw.rect(screen, cor, (15, 120, 440, 100))
            draw_text('JOGADOR  :', font, (25, 25, 25), screen, 20, 130)
            draw_text(c, font, (25, 25, 25), screen, 160, 130)
            draw_text('PONTOS:', font, (25, 25, 25), screen, 160, 160)
            draw_text(str(b), font, (25, 25, 25), screen, 260, 160)
            draw_text('N° JOGADAS:', font, (25, 25, 25), screen, 160, 190)
            draw_text(str(d), font, (25, 25, 25),
                      screen, 300, 190)  # pontuação

    def calc_rect(self, i):
        figurarectL = (self.margem_esquerda) + (self.tamanho_figura +
                                                self.entrelinhas) * (i % self.coluna_cartas)
        figurarectH = (self.margem_superior) + (self.tamanho_figura +
                                                self.entrelinhas) * (i % self.linha_cartas)
        return (figurarectL, figurarectH)

    def abrir_tela(self):
        tela_jogo = (self.largura_tela, self.altura_tela)
        return tela_jogo
