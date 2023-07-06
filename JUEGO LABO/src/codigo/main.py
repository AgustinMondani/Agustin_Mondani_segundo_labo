import pygame
from config import *
from jugador import Jugador
from objeto import *
from nivelUno import *
from funciones_generales import * 

pygame.init()

pygame.display.set_caption("Agustin Mondani")

ejecuta = True
while ejecuta:

    reloj.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.contador_saltos < 2:
                player.salto()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                player.hit = not(player.hit)
            
    draw(player, bloques)
    
    player.bucle_movimiento()
    player.movimiento(bloques)

    pygame.display.update()

pygame.quit()


