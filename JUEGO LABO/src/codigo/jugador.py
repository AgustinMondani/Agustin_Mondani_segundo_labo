import pygame
from config import *
from funciones_generales import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, cantidad_enemigos) -> None:
        #self.rect = pygame.Rect(x, y , 30, 61)
        self.image = pygame.image.load("src/texturas/personaje/quieto/0.png")
        self.rect = self.image.get_rect()
        self.x_inicial = x
        self.y_inicial = y
        self.enemigos_iniciales = cantidad_enemigos
        self.rect.x = x
        self.rect.y = y
        self.velocidad_jugador = 6
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.direccion = 'quieto'
        self.anterior_direccion = 'right'
        self.contador_caidas = 0
        self.contador_saltos = 0
        self.count = 0
        self.cantidad_enemigos = self.enemigos_iniciales
        self.hit = False
        self.bottom = self.rect.bottom
        self.right = self.rect.right
        self.left = self.rect.left
        self.top = self.rect.top
        self.center = self.rect.center
        self.hitbox  = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.vidas_img = pygame.image.load("src/texturas/vida/vida.png")
        self.image_vidas = pygame.transform.scale(self.vidas_img,(45,45))
        self.vidas = 3
        self.gano = False

        self.quieto = cargar_lista_imagenes("src/texturas/personaje/quieto", 1)
        self.caminar = cargar_lista_imagenes("src/texturas/personaje/caminar", 8)
        self.saltar = cargar_lista_imagenes("src/texturas/personaje/saltar", 1)
        self.caer  = cargar_lista_imagenes("src/texturas/personaje/caer", 1)
        self.contador_sprite = 0
        
        
    def actualizarHitbox(self):
        self.bottom = self.rect.bottom
        self.right = self.rect.right
        self.left = self.rect.left
        self.top = self.rect.top
        self.center = self.rect.center

    def mover(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def mover_izquierda(self):
        if self.rect.x > 2:
            self.velocidad_x = -self.velocidad_jugador
            if self.direccion != "left":
                self.direccion = "left"

    def mover_derecha(self):
        if self.rect.x < WIDHT - self.rect.width:
            self.velocidad_x = self.velocidad_jugador
            if self.direccion != "right":
                self.direccion = "right"
    
    def salto(self):
        self.velocidad_y = - GRAVEDAD * 8
        self.contador_saltos += 1
        if self.contador_saltos == 1:
            self.contador_caidas = 0

    def bucle_movimiento(self):
        self.velocidad_y += min(1, (self.contador_caidas / FPS) * GRAVEDAD)
        self.contador_caidas += 1
        self.mover(self.velocidad_x, self.velocidad_y) 

    def draw(self):
        self.hitbox  = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        if self.contador_sprite + 1 >= 8:
            self.contador_sprite = 0

        if self.velocidad_y < 0:
            if self.velocidad_x > 0:
                PANTALLA.blit((self.saltar[0]), (self.rect.x, self.rect.y))
            elif self.velocidad_x < 0:
                PANTALLA.blit(pygame.transform.flip((self.saltar[0]), True, False), (self.rect.x, self.rect.y))
            elif self.velocidad_x == 0:
                if self.anterior_direccion == 'right':
                    PANTALLA.blit(self.saltar[0], (self.rect.x, self.rect.y))
                    #self.image = self.saltar[0]
                elif self.anterior_direccion == 'left':
                    PANTALLA.blit(pygame.transform.flip((self.saltar[0]), True, False), (self.rect.x, self.rect.y))
                    #self.image = pygame.transform.flip(self.saltar[0], True, False)
        elif self.velocidad_y > GRAVEDAD * 2:
            if self.velocidad_x > 0:
                PANTALLA.blit((self.caer[0]), (self.rect.x, self.rect.y))
            elif self.velocidad_x < 0:
                PANTALLA.blit(pygame.transform.flip((self.caer[0]), True, False), (self.rect.x, self.rect.y))
            elif self.velocidad_x == 0:
                if self.anterior_direccion == 'right':
                    PANTALLA.blit(self.caer[0], (self.rect.x, self.rect.y))
                    #self.image = self.caer[0]
                elif self.anterior_direccion == 'left':
                    PANTALLA.blit(pygame.transform.flip((self.caer[0]), True, False), (self.rect.x, self.rect.y))
                    #self.image = pygame.transform.flip(self.caer[0], True, False)
    
        else:
            #Tecla < - Moviemiento a la izquierda
            if self.direccion == 'left':
                PANTALLA.blit(pygame.transform.flip((self.caminar[self.contador_sprite]), True, False), (self.rect.x, self.rect.y))
                #self.image = pygame.transform.flip(self.caminar[self.contador_sprite], True, False)
                self.contador_sprite += 1
                self.anterior_direccion = 'left'

            #Tecla -> - Moviemiento a la derecha
            elif self.direccion == 'right':
                PANTALLA.blit((self.caminar[self.contador_sprite]), (self.rect.x, self.rect.y))
                #self.image = self.caminar[self.contador_sprite]
                self.contador_sprite += 1
                self.anterior_direccion = 'right'
        
            if self.direccion == 'quieto':
                if self.anterior_direccion == 'right':
                    PANTALLA.blit(self.quieto[0], (self.rect.x, self.rect.y))
                    #self.image = self.quieto[0]
                elif self.anterior_direccion == 'left':
                    PANTALLA.blit(pygame.transform.flip((self.quieto[0]), True, False), (self.rect.x, self.rect.y))
                    #self.image = pygame.transform.flip(self.quieto[0], True, False)
        
        match self.vidas:
            case 1:
                PANTALLA.blit(self.image_vidas, (20 , 20))
            case 2:
                PANTALLA.blit(self.image_vidas, (20 , 20))
                PANTALLA.blit(self.image_vidas, (40 , 20))
            case 3:
                PANTALLA.blit(self.image_vidas, (20 , 20))
                PANTALLA.blit(self.image_vidas, (40 , 20))
                PANTALLA.blit(self.image_vidas, (60 , 20))
            case 0:
                pass


        if(self.hit):
            self.hitbox  = (self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            pygame.draw.rect(PANTALLA, (255,0,0), self.hitbox, 2)

    def colisiones_y(self, objetos, dy):
        collided_objects = []
        for obj in objetos:
            if pygame.sprite.collide_mask(self, obj):
                if dy > 0:
                    self.rect.bottom = obj.rect.top
                    #colision arriba
                    self.contador_caidas = 0
                    self.velocidad_y = 0
                    self.contador_saltos = 0
                elif dy < 0:
                    self.rect.top = obj.rect.bottom
                    #colision abajo
                    self.count = 0
                    self.velocidad_y *= -1
                collided_objects.append(obj)
        return collided_objects
    
    def colisiones_x(self, objetos, dx):
        self.mover(dx,0)
        collided_objects = []
        for obj in objetos:
            if pygame.sprite.collide_mask(self, obj):
                collided_objects.append(obj)
        self.mover(-dx, 0)

        return collided_objects
    

    def movimiento(self, objetos):
        self.bucle_movimiento()
        keys = pygame.key.get_pressed()

        self.velocidad_x = 0
        colision_izquierda = self.colisiones_x(objetos, -self.velocidad_jugador)
        colision_derecha = self.colisiones_x(objetos, self.velocidad_jugador)

        if keys[pygame.K_RIGHT] and not colision_derecha:
            self.mover_derecha()
        elif keys[pygame.K_LEFT] and not colision_izquierda:
            self.mover_izquierda()
        else:
            self.direccion = 'quieto'

        self.colisiones_y(objetos, self.velocidad_y)
    
    def reset(self):

        self.rect.x = self.x_inicial
        self.rect.y = self.y_inicial
        self.cantidad_enemigos = self.enemigos_iniciales
        self.gano = False
        self.vidas = 3