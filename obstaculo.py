import pygame
from abc import ABC, abstractmethod

class Obstaculo(pygame.sprite.Sprite, ABC):         # Clase abstracta que hereda de Sprite (pygame) y ABC, para definir diferentes obstaculos
    def __init__(self, x, y, religion):
        super().__init__()

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
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect