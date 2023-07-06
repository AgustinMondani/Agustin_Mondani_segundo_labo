import pygame

WIDHT ,HEIGHT = 1280,720
FPS = 30
GRAVEDAD = 1.25
COLOR = (84,237,239)

volumen_inicial = 0.5

PANTALLA = pygame.display.set_mode((WIDHT, HEIGHT))
reloj = pygame.time.Clock()

img_jugar = pygame.image.load("src/texturas/botones/jugar.png").convert_alpha()
img_opciones = pygame.image.load("src/texturas/botones/opciones.png").convert_alpha()
img_salir = pygame.image.load("src/texturas/botones/salir.png").convert_alpha()

img_menu = pygame.image.load("src/texturas/botones/menu.png").convert_alpha()
img_volumen_mas = pygame.image.load("src/texturas/volumen/Volume.png").convert_alpha()
img_volumen_menos = pygame.image.load("src/texturas/volumen/Volume-.png").convert_alpha()


pygame.mixer.init()

sound = pygame.mixer.Sound("src/sonidos/ouch.mp3")
sound_victoria = pygame.mixer.Sound("src/sonidos/homero27.mp3")
sound_matar = pygame.mixer.Sound("src/sonidos/homer-simpson-aiuju.mp3")
sound_inicio = pygame.mixer.Sound("src/sonidos/television-simpsons.mp3")
