import pygame
import pygame.font
from config import *
from os.path import join
from funciones_generales import *

def get_block(size,dir):
    image = pygame.image.load("src/texturas/suelo/suelo.png").convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, dir, size, size)
    surface.blit(image, (0, 0), rect)
    return surface

def get_platform(ancho, alto, dir):
    image = pygame.image.load("src/texturas/suelo/suelo.png").convert_alpha()
    surface = pygame.Surface((ancho, alto), pygame.SRCALPHA, 32) #El srcalpha es para mantener la trasparencia
    rect = pygame.Rect(272, dir, ancho, alto)
    surface.blit(image, (0, 0), rect)
    return surface

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height

    def draw(self):
        PANTALLA.blit(self.image, (self.rect.x, self.rect.y))

class Bloque(Objeto):
    def __init__(self, x, y, size,dir):
        super().__init__(x, y, size, size)
        block = get_block(size,dir)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Plataforma(Objeto):
    def __init__(self, x, y, ancho, alto, dir, personaje):
        super().__init__(x, y, ancho, alto)
        block = get_platform(ancho, alto, dir)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.direccion_movimiento = "left"
        self.cont = 0
        self.personaje = personaje
        self.velocidad_x = -5

    def draw(self):
        self.movimiento()
        return super().draw()

    def mover(self, dx):
        self.rect.x += dx

    def movimiento(self):
        if(self.direccion_movimiento == "left"):
            self.mover(2)
            self.cont += 1
            if(self.cont ==  80):
                self.cont = 0
                self.direccion_movimiento = "right"
        elif(self.direccion_movimiento == "right"):
            self.mover(-2)
            self.cont += 1
            if(self.cont ==  80):
                self.cont = 0
                self.direccion_movimiento = "left"
            
class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, personaje):
        self.img = pygame.image.load("src/texturas/trampa/0.png")
        self.imagen = pygame.transform.scale(self.img,(48, 30))
        self.rect = self.imagen.get_rect()
        self.mask = pygame.mask.from_surface(self.imagen)
        self.player = personaje
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.colliderect(self.player.rect) and self.player.rect.bottom < self.rect.bottom:
            self.player.rect.x = self.player.x_inicial
            self.player.rect.y  = self.player.y_inicial
            self.player.vidas -= 1
            sound.play()
           
        elif self.rect.colliderect(self.player.rect):
            if self.rect.left > self.player.rect.left or self.rect.right < self.player.rect.right:
                self.player.rect.x = self.player.x_inicial
                self.player.rect.y  = self.player.y_inicial
                self.player.vidas -= 1
                sound.play()

    def draw(self):
        self.update()
        PANTALLA.blit((self.imagen), (self.rect.x, self.rect.y))


class Trofeo(pygame.sprite.Sprite):
    def __init__(self, x, y, personaje):
        super().__init__()
        self.imagen = pygame.image.load("src/texturas/final/0.png")
        self.rect = self.imagen.get_rect()
        self.mask = pygame.mask.from_surface(self.imagen)
        self.player = personaje
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.colliderect(self.player.rect) and self.player.rect.bottom < self.rect.bottom:
            if self.player.cantidad_enemigos == 0:
                self.player.gano = True
                sound_victoria.play()
           
        elif self.rect.colliderect(self.player.rect):
            if self.rect.left > self.player.rect.left or self.rect.right < self.player.rect.right:
                if self.player.cantidad_enemigos == 0:
                    self.player.gano = True
                    sound_victoria.play()


    def draw(self):
        self.update()
        PANTALLA.blit(self.imagen, (self.rect.x, self.rect.y))


    


        