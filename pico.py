import pygame
from obstaculo import Obstaculo

class Pico(Obstaculo):
    def __init__(self, x, y, religion):
        super().__init__(x, y, religion)    # Llama al constructor de la clase padre

        self._tipo = "pico"                 # Define el tipo de obstaculo

        self.cargar_imagen()                # Carga la imagen del obstaculo

    def cargar_imagen(self):                # Sobreescritura polimorfica del metodo abstracto
        if self._religion == 1:
            self._image = pygame.image.load('assets/Enredaderas/enredadera.png').convert_alpha()    # Carga imagen
            self._image = pygame.transform.scale2x(self.image)                                      # Escala imagen a 2x
        else:
            self._image = pygame.image.load('assets/Rosales/rosales.png').convert_alpha()           # Carga imagen
            self._image = pygame.transform.scale2x(self.image)                                      # Escala imagen a 2x        

        self._rect = self._image.get_rect(midbottom = (self._x, self._y))                           # Define el rectangulo del obstaculo