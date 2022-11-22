import pygame
from abc import ABC, abstractmethod

class Obstaculo(pygame.sprite.Sprite, ABC):         # Clase abstracta que hereda de Sprite (pygame) y ABC, para definir diferentes obstaculos
    def __init__(self, x, y, religion):
        super().__init__()                          # Llama al constructor de las clases padres, Sprite y ABC (abstract base class)

        self._x = x                                 # Posicion en x de cada obstaculo
        self._y = y                                 # Posicion en y de cada obstaculo

        self._religion = religion                   # Religion aa la que pertenece el obstaculo

    @abstractmethod
    def cargar_imagen(self):                        # Metodo abstracto para cargar la imagen al sprite
        pass

    def collision(self, jugador):                   # Metodo implementado para detectar colisiones entre el jugador y el obstaculo
        if self._rect.colliderect(jugador.rect):
            return True

    @property
    def tipo(self):                                 # Getter para el tipo de obstaculo
        return self._tipo

    @property
    def image(self):                                # Getter para la imagen del obstaculo
        return self._image

    @property
    def rect(self):                                 # Getter para el rectangulo del obstaculo
        return self._rect