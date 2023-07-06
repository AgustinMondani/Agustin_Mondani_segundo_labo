import pygame
from config import *
from funciones_generales import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vida, colisiones, personaje)-> None:

        self.images_mover = cargar_lista_imagenes("src/texturas/enemigo", 4)  # Cargar imágenes de caminar
        self.rect = self.images_mover[0].get_rect()
        self.colisiones = colisiones
        self.player = personaje
        self.x_inicial = x
        self.y_inicial = y
        self.rect.x = x
        self.rect.y = y
        self.direction = -1
        self.contador_sprite = 0
        self.vivo = True

    def update(self):
        self.rect.x += self.direction * 5

        for obstacle in self.colisiones:
            if self.rect.colliderect(obstacle.rect):
                self.direction *= -1  
                
        if self.rect.colliderect(self.player.rect) and self.player.rect.bottom < self.rect.bottom:
            self.vivo = False
            self.player.cantidad_enemigos -= 1
            print(self.player.cantidad_enemigos)
            sound_matar.play()
           
        elif self.rect.colliderect(self.player.rect):
            if self.rect.left > self.player.rect.left or self.rect.right < self.player.rect.right:
                self.player.rect.x = self.player.x_inicial
                self.player.rect.y  = self.player.y_inicial
                self.player.vidas -= 1
                sound.play()
        

    def draw(self):
        if self.vivo:
            self.update()
            self.contador_sprite += 1
            if (self.contador_sprite == 4):
                self.contador_sprite = 0
            PANTALLA.blit(self.images_mover[self.contador_sprite], (self.rect.x, self.rect.y))

    def reset(self):
        self.vivo = True
        self.rect.x = self.x_inicial
        self.rect.y = self.y_inicial
       