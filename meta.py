import pygame
from obstaculo import Obstaculo

class Meta(Obstaculo):
    def __init__(self):
        super().__init__()

        self._tipo = "meta"

        self._image = pygame.image.load('assets/Meta/meta.jpg').convert_alpha() # Carga imagen
        self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x

        self._rect = self._image.get_rect(midbottom = (self._x, self._y)) # Define rectangulo

    def collision(self, jugador):
        if self._rect.colliderect(jugador._rect):
            return True