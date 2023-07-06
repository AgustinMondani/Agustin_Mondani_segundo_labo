import pygame
from config import *
from funciones_generales import *
from boton import *
from niveles import *
from funcion_nivel import *
from objeto import *
from cronometro import Cronometro
from puntajes import *

pygame.init()

pygame.display.set_caption("Homero")

imagen_menu = pygame.image.load("src/texturas/fondos/menu.png")
fondo_menu = pygame.transform.scale(imagen_menu,(WIDHT, HEIGHT))

font  = pygame.font.SysFont("arial", 40)
color_texto = (255, 255,  255)
color_boton = (0, 0, 0)

#####
boton_jugar = Button(100, 100, img_jugar, 2)
boton_opciones = Button(100, 300, img_opciones, 2)
boton_salir = Button(100, 500, img_salir, 2)

boton_menu = Button(300, 100, img_menu, 3)
boton_mas_volumen = Button(400, 400, img_volumen_mas, 5)
boton_menos_volumen = Button(650, 400, img_volumen_menos, 5)
#####

ejecutar = True
menu_estado  = "menu"
opcion_menu = "menu"
nivel_actual = 1
player = player1
top5 = cargar_tabla()
cronometro.iniciar()

while ejecutar:
    reloj.tick(FPS)
    
    if menu_estado == "menu":
        cronometro.pausar()
        sound_inicio.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutar = False
        PANTALLA.blit(fondo_menu,(0, 0))
        if opcion_menu == "menu":
            mostrar_tabla(top5)
            if boton_jugar.draw(PANTALLA):
                cronometro.reanudar()
                menu_estado = "juego"
                opcion_menu = "menu"
                sound_inicio.stop()
            elif boton_opciones.draw(PANTALLA):
                opcion_menu = "opciones"
            elif boton_salir.draw(PANTALLA):
                pygame.quit()
                ejecutar = False
        if opcion_menu == "opciones":
            sound_inicio.set_volume(volumen_inicial)
            sound_matar.set_volume(volumen_inicial)
            sound_victoria.set_volume(volumen_inicial)
            sound.set_volume(volumen_inicial)
            if boton_menu.draw(PANTALLA):
                opcion_menu = "menu"
            if boton_mas_volumen.draw(PANTALLA):
                volumen_inicial += 0.1
            if boton_menos_volumen.draw(PANTALLA):
                volumen_inicial -= 0.1
    

    if menu_estado == "juego":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutar = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.contador_saltos < 2:
                    player.salto()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    player.hit = not(player.hit)
                if event.key == pygame.K_ESCAPE:
                    menu_estado = "menu"

        if nivel_actual == 1:
            niveles(player, bloques1, enemigos1, trampas1, fondo1)
            if player.gano:
                resetear_nivel(player, enemigos1)
                nivel_actual += 1
                player = player2
        if nivel_actual == 2:
            niveles(player, bloques2, enemigos2, trampas2, fondo2)
            if player.gano:
                resetear_nivel(player, enemigos2)
                nivel_actual += 1
                player = player3
        if nivel_actual == 3:
            niveles(player, bloques3, enemigos3, trampas3, fondo3)
            if player.gano:
                puntaje = cronometro.obtener_tiempo_transcurrido()
                nombre_player = cargar_nombre()
                cargar_csv("scores.csv",nombre_player,puntaje)
                top5 = cargar_tabla()
                menu_estado = "menu"
                nivel_actual = 1
                resetear_nivel(player, enemigos3)
                player = player1
                cronometro.reiniciar()

    pygame.display.update()
pygame.quit()

