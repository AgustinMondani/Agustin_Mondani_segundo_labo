import pygame
import pygame.font
from config import *
from jugador import *
from objeto import *
from enemigo import *
from niveles import *
from cronometro import Cronometro

cronometro = Cronometro()

def niveles(player, bloques, enemigos, trampas, fondo):
    
    cronometro.actualizar()
    fuente = pygame.font.SysFont("Arial", 36)
        
    texto = fuente.render(f"{cronometro.obtener_tiempo_transcurrido()} SEG", True, (255, 100, 100))

    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(texto,(200,25))

    for obj in bloques:
        obj.draw()

    for enemi in enemigos:
        enemi.draw()

    for trampa in trampas:
        trampa.draw()

    player.movimiento(bloques)

    player.draw()

    pygame.display.update()

def resetear_nivel(player, enemigos):

    player.reset()
    for enemigo in enemigos:
        enemigo.reset()
    


