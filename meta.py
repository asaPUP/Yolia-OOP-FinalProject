import pygame
from obstaculo import Obstaculo

class Meta(Obstaculo):
    def __init__(self, x, y, religion):
        super().__init__(x, y, religion)    # Llama al constructor de la clase padre

        self._tipo = "meta"                 # Define el tipo de obstaculo

        self.cargar_imagen()                # Carga la imagen del obstaculo

    def cargar_imagen(self):                # Sobreescritura polimorfica del metodo abstracto
        self._image = pygame.image.load('assets/Meta/meta.jpg').convert_alpha() # Carga imagen
        self._image = pygame.transform.scale2x(self._image)                     # Escala imagen a 2x

        self._rect = self._image.get_rect(midbottom = (self._x, self._y))       # Define el rectangulo del obstaculo