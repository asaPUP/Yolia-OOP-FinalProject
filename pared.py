import pygame
from obstaculo import Obstaculo

class Pared(Obstaculo):
    def __init__(self):
        super().__init__()

        self._tipo = "pared"

        self.cargar_imagen()

    def cargar_imagen(self):                # Sobreescritura polimorfica del metodo abstracto
        if self._religion == 1:
            self._image = pygame.image.load('assets/Piedras/piedra.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x
        else:
            self._image = pygame.image.load('assets/Hoyo/HoyoNube.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x
        
        self._rect = self._image.get_rect(midbottom = (self._x, self._y)) # Define rectangulo