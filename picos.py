import pygame
from obstaculo import Obstaculo

class Picos(Obstaculo):
    def __init__(self):
        super().__init__()

        if self._tipo == 1:
            self._image = pygame.image.load('assets/Enredaderas/enredadera.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
            
        else:
            self._image = pygame.image.load('assets/Rosales/rosales.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self.image) # Escala imagen a 2x        

        self._rect = self.image.get_rect(midbottom = (self.x, self.y))
    
    def collision(self, jugador):
        if self.rect.colliderect(jugador.rect):
            return True