import pygame
import pygame.font

class Cronometro:
    def __init__(self):
        self.tiempo_inicial = 0
        self.tiempo_pausado = 0
        self.tiempo_transcurrido = 0
        self.en_pausa = False

    def iniciar(self):
        self.tiempo_inicial = pygame.time.get_ticks()

    def pausar(self):
        if not self.en_pausa:
            self.tiempo_pausado = pygame.time.get_ticks() - self.tiempo_inicial
            self.en_pausa = True

    def reanudar(self):
        if self.en_pausa:
            self.tiempo_inicial = pygame.time.get_ticks() - self.tiempo_pausado
            self.en_pausa = False

    def reiniciar(self):
        self.tiempo_inicial = 0
        self.tiempo_pausado = 0
        self.tiempo_transcurrido = 0
        self.en_pausa = False

    def actualizar(self):
        if not self.en_pausa:
            self.tiempo_transcurrido = pygame.time.get_ticks() - self.tiempo_inicial
            self.tiempo_transcurrido //= 1500

    def obtener_tiempo_transcurrido(self):
        return self.tiempo_transcurrido