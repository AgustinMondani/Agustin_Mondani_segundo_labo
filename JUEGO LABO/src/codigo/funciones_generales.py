import pygame
from config import *

def cargar_lista_imagenes(ruta:str ,cantidad_imagenes:int)->list:
    """Document
    Toma un ruta de imagenes y genera una lista con las imagenes, las renombra desde el 0 y las escala
    Parametros:
        ruta(str):El enlace de donde estan guardas las imagenes
        cantidad_imagenes(int): cuantas imagenes hay en la ruta
        tamaño(int): a que tamaño se desea escalar
    Return:
        lista_de_imagenes(list)Con todas las imagenes del sprite
    """
    lista_de_imagenes = []
    for i in range(cantidad_imagenes):
        frame = pygame.image.load(ruta+"/"+str(i)+".png").convert_alpha()
        lista_de_imagenes.append(frame)
    return lista_de_imagenes


def dibujar_texto(texto:str, font:str, color:tuple, x:int, y:int) -> None:
    imagen = font.render(texto, True, color)
    PANTALLA.blit(imagen, (x, y))



