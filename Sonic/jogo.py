#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUÇÃO DO DESAFIO 2
---
Construa um jogo com uma imagem
de cenário e uma imagem de personagem
que consegue se mover.
"""

import pygame
from pygame import mixer
from pathlib import Path
from pygame.locals import *

DIRETORIO_ATUAL = str(Path(__file__).parent.absolute())

tela = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock() 




egg= pygame.image.load('imagens/robotunicoSprite.webp')
sonic = pygame.image.load('imagens/sonic-stop.png')
fundo = pygame.image.load('imagens/green-hills.png')
pygame.mixer.init()
pygame.mixer.music.load('musicas/8d82b5_Sonic_Green_Hill_Zone_Theme_Song.mp3')
pygame.mixer.music.play()

sonic_x = 100
sonic_y = 350
direcao = (0, 0)

egg_x = 100
egg_y = 350
egg_direcao = (0, 0)

egg_x += direcao[0]
egg_y += direcao[1]
    
tela.blit(fundo, [0, 0])
tela.blit(egg, [egg_x, egg_y])
clock.tick(30)


executando = True
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                direcao = (0, -20)
            if evento.key == pygame.K_DOWN:
                direcao = (0, 20)
            if evento.key == pygame.K_LEFT:
                direcao = (-20, 0)
            if evento.key == pygame.K_RIGHT:
                direcao = (20, 0)
        
        if evento.type == pygame.KEYUP:
            direcao = (0, 0)

    sonic_x += direcao[0]
    sonic_y += direcao[1]
    
    tela.blit(fundo, [0, 0])
    tela.blit(sonic, [sonic_x, sonic_y])
    clock.tick(30)

    

    pygame.display.update()
    



pygame.quit()