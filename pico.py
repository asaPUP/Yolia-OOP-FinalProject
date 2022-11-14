import pygame
from obstaculo import Obstaculo

class Pico(Obstaculo):
    def __init__(self):
        super().__init__()

        if self._tipo == 1:
            self._image = pygame.image.load('assets/Enredaderas/enredadera.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
            
        else:
            self._image = pygame.image.load('assets/Rosales/rosales.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self.image) # Escala imagen a 2x        

        self._rect = self._image.get_rect(midbottom = (self._x, self._y))
    
    def collision(self, jugador):
        if self._rect.colliderect(jugador._rect):
            return True