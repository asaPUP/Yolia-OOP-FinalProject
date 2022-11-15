import pygame
from abc import abc, abstractmethod

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, religion):
        super().__init__()

        self._x = x
        self._y = y

        self._religion = religion

    @abstractmethod
    def cargar_imagen(self):                        # Metodo abstracto para cargar la imagen al sprite
        pass

    def collision(self, jugador):                   # Metodo para detectar colisiones entre el jugador y el obstaculo
        if self._rect.colliderect(jugador._rect):
            return True