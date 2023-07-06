import pygame
from config import *
from objeto import *
from jugador import *
from enemigo import *

image1 = pygame.image.load("src/texturas/fondos/nivel1.jpg")
fondo1 = pygame.transform.scale(image1,(WIDHT,HEIGHT))

tamaño_bloque  = 48 #tamaño del bloque
tipo_bloque1 = 128 #los tipos de bloques son 0 64 128
alto_enemigo = 32
alto_trampa = 30

tope_techo = [Bloque(i * tamaño_bloque, 0 - tamaño_bloque, tamaño_bloque, tipo_bloque1)
            for i in range(40)]

#cronometro1 = [Cronometro()]

player1 = Jugador(50, 600, 2)

trofeo = [Trofeo(1000, 100, player1)]
piso = [Bloque(i * tamaño_bloque, HEIGHT - tamaño_bloque, tamaño_bloque, tipo_bloque1)
            for i in range(-WIDHT// tamaño_bloque, (WIDHT * 2) // tamaño_bloque)]

plataforma_uno = [Bloque(((19 + i) *tamaño_bloque ), (HEIGHT - tamaño_bloque * 4), tamaño_bloque, tipo_bloque1)
                    for i in range(5)]

bloques_sueltos1 = [Bloque(5 * tamaño_bloque, HEIGHT - tamaño_bloque*2, tamaño_bloque, tipo_bloque1),
                    Bloque(15 * tamaño_bloque, HEIGHT - tamaño_bloque*2, tamaño_bloque, tipo_bloque1),
                    Bloque(2 * tamaño_bloque, HEIGHT - tamaño_bloque*9, tamaño_bloque, tipo_bloque1),
                    Bloque(8 * tamaño_bloque, HEIGHT - tamaño_bloque*9, tamaño_bloque, tipo_bloque1)]

plataforma_dos1 = [Bloque(((2 + i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 8), tamaño_bloque, tipo_bloque1)
                    for i in range(7)]

plataforma_tres1 = [Bloque(((13 + i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 11), tamaño_bloque, tipo_bloque1)
                    for i in range(14)]

trampas1 = [Trampa(15 * tamaño_bloque, HEIGHT - tamaño_bloque * 2 - alto_trampa, player1),
            Trampa(3 * tamaño_bloque, HEIGHT - tamaño_bloque - alto_trampa, player1),
            Trampa(21 * tamaño_bloque, HEIGHT - tamaño_bloque * 4 - alto_trampa, player1),
            Trampa(22 * tamaño_bloque, HEIGHT - tamaño_bloque * 4 - alto_trampa, player1)]

enemigos1 = [Enemy(300, HEIGHT - tamaño_bloque - alto_enemigo, 1, bloques_sueltos1, player1),
                Enemy(4 * tamaño_bloque, HEIGHT - tamaño_bloque * 8 - alto_enemigo, 1, bloques_sueltos1, player1)]
plataforma_movil1 = [Plataforma(650, 400, 48 , 5, 0, player1),Plataforma(602, 400, 48 , 5, 0, player1)]
bloques1 = [*piso, *plataforma_uno, *plataforma_movil1, *bloques_sueltos1, *plataforma_dos1, *plataforma_tres1, *trofeo, *tope_techo]#,*cronometro1]

####  NIVEL 2  ##################################################################################################################################

player2 = Jugador(100,500, 1)         
image2 = pygame.image.load("src/texturas/fondos/nivel2.jpg")
fondo2 = pygame.transform.scale(image2,(WIDHT,HEIGHT))

tamaño_bloque  = 48 #tamaño del bloque
tipo_bloque2 = 64 #los tipos de bloques2 son 0 64 128


trofeo2 = [Trofeo(2, 100, player2)]
piso2 = [Bloque(i * tamaño_bloque, HEIGHT - tamaño_bloque, tamaño_bloque, tipo_bloque2)
            for i in range(3)]

plataforma_uno2 = [Bloque(((19 + i) *tamaño_bloque ), (HEIGHT - tamaño_bloque * 4), tamaño_bloque, tipo_bloque2)
                for i in range(5)]

bloques_sueltos2 = [Bloque(0, HEIGHT - tamaño_bloque*2, tamaño_bloque, tipo_bloque2),
                Bloque(0, HEIGHT - tamaño_bloque*3, tamaño_bloque, tipo_bloque2),
                Bloque(1 * tamaño_bloque, HEIGHT - tamaño_bloque * 2, tamaño_bloque, tipo_bloque2),
                Bloque(16 * tamaño_bloque, HEIGHT - tamaño_bloque, tamaño_bloque, tipo_bloque2),
                Bloque(10 * tamaño_bloque, HEIGHT - tamaño_bloque * 9, tamaño_bloque, tipo_bloque2),
                Bloque(10 * tamaño_bloque, HEIGHT - tamaño_bloque * 10, tamaño_bloque, tipo_bloque2),
                Bloque(0, HEIGHT - tamaño_bloque*9, tamaño_bloque, tipo_bloque2),
                Bloque(0, HEIGHT - tamaño_bloque*10, tamaño_bloque, tipo_bloque2),
                Bloque(1 * tamaño_bloque, HEIGHT - tamaño_bloque * 9, tamaño_bloque, tipo_bloque2)]

plataforma_dos2 = [Bloque(((i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 8), tamaño_bloque, tipo_bloque2)
                for i in range(11)]

plataforma_tres2 = [Bloque(((10 + i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 11), tamaño_bloque, tipo_bloque2)
                for i in range(6)]

trampas2 = [Trampa(i * tamaño_bloque, HEIGHT, player2)
            for i in range(30)]+ [Trampa(1 * tamaño_bloque, HEIGHT - tamaño_bloque * 9 - alto_trampa, player2)]

enemigos2 = [Enemy(4 * tamaño_bloque, HEIGHT - tamaño_bloque * 8 - alto_enemigo, 2, bloques_sueltos2, player2)]
plataforma_movil2 = [Plataforma(300, 600, 48 , 5, 0, player2),
                     Plataforma(348, 600, 48 , 5, 0, player2),
                     Plataforma(396, 600, 48 , 5, 0, player2),
                     Plataforma(434, 600, 48 , 5, 0, player2),
                     Plataforma(600, 325, 48 , 5, 0, player2),
                     Plataforma(648, 435, 48 , 5, 0, player2)]
bloques2 = [*piso2, *plataforma_uno2, *plataforma_movil2, *bloques_sueltos2, *plataforma_dos2, *plataforma_tres2, *trofeo2, *tope_techo]


###### NIVEL 3 #################################################################################################################################

player3 = Jugador(580,600, 2)         
image3 = pygame.image.load("src/texturas/fondos/nivel3.jpg")
fondo3 = pygame.transform.scale(image3,(WIDHT,HEIGHT))

tamaño_bloque  = 48 #tamaño del bloque
tipo_bloque3 = 0 #los tipos de bloques2 son 0 64 128


trofeo3 = [Trofeo(1150, 400, player3)]


piso3 = [Bloque((11 + i) * tamaño_bloque, HEIGHT - tamaño_bloque, tamaño_bloque, tipo_bloque3)
            for i in range(3)]

plataforma_uno3 = [Bloque(((8 + i) *tamaño_bloque ), (HEIGHT - tamaño_bloque * 6), tamaño_bloque, tipo_bloque3)
                for i in range(8)]

bloques_sueltos3 = [Bloque(0, HEIGHT - tamaño_bloque*4, tamaño_bloque, tipo_bloque3),
                Bloque(1 * tamaño_bloque, HEIGHT - tamaño_bloque * 4, tamaño_bloque, tipo_bloque3),
                Bloque(2 * tamaño_bloque, HEIGHT - tamaño_bloque * 4, tamaño_bloque, tipo_bloque3),
                Bloque(15 * tamaño_bloque, HEIGHT - tamaño_bloque * 9 + 20, tamaño_bloque, tipo_bloque3),
                Bloque(15 * tamaño_bloque, HEIGHT - tamaño_bloque * 10 + 20, tamaño_bloque, tipo_bloque3)]

bloque_invisibles = [Bloque(7 * tamaño_bloque, HEIGHT - tamaño_bloque*7, tamaño_bloque, tipo_bloque3),
                Bloque(15 * tamaño_bloque, HEIGHT - tamaño_bloque * 7, tamaño_bloque, tipo_bloque3),
                Bloque(-tamaño_bloque, HEIGHT - tamaño_bloque * 11 - 30, tamaño_bloque, tipo_bloque3),
                Bloque(10 * tamaño_bloque, HEIGHT - tamaño_bloque * 11 - 30, tamaño_bloque, tipo_bloque3)]

plataforma_dos3 = [Bloque(((i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 10 - 30), tamaño_bloque, tipo_bloque3)
                for i in range(11)]

plataforma_tres3 = [Bloque(((18 + i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 3), tamaño_bloque, tipo_bloque3)
                for i in range(6)]

trampas3 = [Trampa(i * tamaño_bloque, HEIGHT, player3)
            for i in range(30)]+ [Trampa(10 * tamaño_bloque, HEIGHT - tamaño_bloque * 11 - 12, player3)]

enemigos3 = [Enemy(9 * tamaño_bloque, HEIGHT - tamaño_bloque * 6 - alto_enemigo, 3, bloque_invisibles, player3),
             Enemy(4 * tamaño_bloque, HEIGHT - tamaño_bloque * 10 - 30 - alto_enemigo, 3, bloque_invisibles, player3)]

plataforma_movil3 = [Plataforma(250, 640, 48 , 5, 0, player3),
                     Plataforma(298, 640, 48 , 5, 0, player3)]

plataforma_superior = [ Plataforma((( i) * tamaño_bloque),(tamaño_bloque * 2), 48,  5, 15, player3)
                       for i in range(23)]

plataforma_extra3 = [Bloque((WIDHT - (i) * tamaño_bloque), (HEIGHT - tamaño_bloque * 6), tamaño_bloque, tipo_bloque3)
                for i in range(5)]
columna3 = [Bloque((WIDHT - (5) * tamaño_bloque),(HEIGHT - tamaño_bloque * (6 + i)), tamaño_bloque, tipo_bloque3)
                for i in range(5)]

bloques3 = [*piso3, *plataforma_uno3, *plataforma_movil3, *bloques_sueltos3, *plataforma_dos3, 
            *plataforma_tres3, *trofeo3, *tope_techo, * plataforma_superior, *plataforma_extra3, *columna3]

