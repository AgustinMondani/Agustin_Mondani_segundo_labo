import pygame
import csv
import sys
import pygame.font
from config import *

pygame.font.init()

fuente = pygame.font.SysFont("Arial", 48)
blanco = (255, 255, 255)

def cargar_csv(nombre_archivo:csv, nombre_jugador:str, puntos:str)->None:
    """"Document
    Esta funcion crea un archivo csv con una lista que ya tenemos cargada, primero lee todas las keys de los
    diccionarios que estan dentro de la lista y las aplica en la primera linea para organizarlas

    Parametros:
    nombre_archivo(str): es el nombre que va a recibir el archivo csv a crear
    productos(list): es la lista de productos a cargar
    """
    with open(nombre_archivo, 'a', newline='',encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre_jugador, puntos])


def cargar_nombre():

    nombre = ""
    escribiendo = True

    while escribiendo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN:
                    escribiendo = False
                else:
                    caracter = event.unicode
                    nombre += caracter
        
        PANTALLA.fill((0, 0, 0))
        
        texto = fuente.render("Nombre: " + nombre, True, blanco)
        
        texto_rect = texto.get_rect(center=(PANTALLA.get_width() // 2, PANTALLA.get_height() // 2))
        
        PANTALLA.blit(texto, texto_rect)

        pygame.display.flip()

    return nombre
        
def cargar_tabla():
    puntajes = []
    with open("scores.csv", 'r') as archivo:
        lector = csv.reader(archivo)
        
        for linea in lector:
            nombre = linea[0]
            puntaje = int(linea[1])
            puntajes.append([nombre, puntaje])

    puntajes.sort(key=lambda x: x[1], reverse=False)
    
    return puntajes[:5]

def mostrar_tabla(puntajes):

    negro = (0, 0, 0)
    
    y = 100
    
    nombres = fuente.render("TOP 5", True, negro)
    rect_nombre = nombres.get_rect(center=(PANTALLA.get_width() // 1.25, y))
    PANTALLA.blit(nombres, rect_nombre)

    for indice, jugador in enumerate(puntajes):
        y += 80
        nombre = jugador[0]
        puntaje = jugador[1]
        
        texto_nombre = fuente.render(nombre, True, negro)
        rect_nombre = texto_nombre.get_rect(center=(PANTALLA.get_width() // 1.25, y))
        PANTALLA.blit(texto_nombre, rect_nombre)
        
        texto_puntaje = fuente.render(str(puntaje), True, negro)
        rect_puntaje = texto_puntaje.get_rect(right=PANTALLA.get_width() - 50, centery=y)
        PANTALLA.blit(texto_puntaje, rect_puntaje)
        
        
    pygame.display.flip()