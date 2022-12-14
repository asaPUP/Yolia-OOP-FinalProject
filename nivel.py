import pygame
from pared import Pared
from meta import Meta
from pico import Pico
from movil import Movil

class Nivel(object):                                # Clase compuesta por una lista de objetos de diferentes tipos, que instancian cada nivel
    
    cont_nivel = 0                                  # Variable estatica para el contador de niveles
    
    def __init__(self):
        self._estaticos = pygame.sprite.Group()     # Los grupos funcionan como listas de objetos, pero con funciones que requiere pygame para manejarlas
        self._movil1 = pygame.sprite.GroupSingle()  # Los obstaculos "movil" tiene un movimiento indepentiente por cada objeto, deben de estar en grupos single
        self._movil2 = pygame.sprite.GroupSingle()

    @property                   # Getter de la lista polimorfica de diferentes obstaculos a instanciarse en cada nivel
    def estaticos(self):
        return self._estaticos
    
    @property                   # Getter de la lista singel del obstaculo movil 1
    def movil1(self):
        return self._movil1

    @property
    def movil2(self):           # Getter de la lista singel del obstaculo movil 2
        return self._movil2

    def nivel1(self):           # Definicion de cada uno de los obstaculos en los 4 niveles, agregando elementos a la lista polimorfica de obstaculos
        self._estaticos.empty()

        self._estaticos.add(Meta(20 + (64 * 8) - 32, 60 + (64 * 9), 1))
        self._estaticos.add(Meta(616 + (64 * 8) - 32, 60 + (64 * 9), 2))

    def nivel2(self):
        self._estaticos.empty()

        self._estaticos.add(Meta(20 + (64 * 2) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Meta(616 + (64 * 9) - 32, 60 + (64 * 1), 2))

        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 1))
        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 5), 1))
        self._estaticos.add(Pared(20 + (64 * 2) - 32, 60 + (64 * 1), 1))
        self._estaticos.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 2))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 2))
        self._estaticos.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 1), 2))

    def nivel3(self):
        self._estaticos.empty()

        self._estaticos.add(Meta(20 + (64 * 2) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Meta(616 + (64 * 8) - 32, 60 + (64 * 8), 2))

        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 7), 1))
        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 8), 1))
        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 9), 1))
        self._estaticos.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 1))
        self._estaticos.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 3), 1))
        self._estaticos.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 4), 1))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 3), 2))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 2), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 1), 2))
        self._estaticos.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 6), 2))
        self._estaticos.add(Pared(616 + (64 * 2) - 32, 60 + (64 * 6), 2))
        self._estaticos.add(Pared(616 + (64 * 3) - 32, 60 + (64 * 6), 2))
        self._estaticos.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 5), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 6), 2))
        self._estaticos.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 3), 2))
        self._estaticos.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 2))
        self._estaticos.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 9), 2))
        self._estaticos.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 7), 2))

    def nivel4(self):
        self._estaticos.empty()

        self._estaticos.add(Meta(20 + (64 * 3) - 32, 60 + (64 * 5), 1))
        self._estaticos.add(Meta(616 + (64 * 2) - 32, 60 + (64 * 1), 2))

        self._estaticos.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 1))
        self._estaticos.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 1))
        self._estaticos.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 7), 1))
        self._estaticos.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 1), 1))
        self._estaticos.add(Pared(20 + (64 * 7) - 32, 60 + (64 * 2), 1))
        self._estaticos.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 2))
        self._estaticos.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 2))
        self._estaticos.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 6), 2))
        self._estaticos.add(Pared(616 + (64 * 9) - 32, 60 + (64 * 7), 2))
        self._estaticos.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 2))
        self._estaticos.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 2), 2))

        self._estaticos.add(Pico(20 + (64 * 2) - 32, 60 + (64 * 5), 1))
        self._estaticos.add(Pico(20 + (64 * 1) - 32, 60 + (64 * 6), 1))
        self._estaticos.add(Pico(616 + (64 * 1) - 32, 60 + (64 * 1), 2))
        self._estaticos.add(Pico(616 + (64 * 3) - 32, 60 + (64 * 2), 2))

        self._movil1.empty()
        self._movil1.add(Movil(20 + (64 * 6) - 32, 60 + (64 * 5), 1))

        self._movil2.empty()
        self._movil2.add(Movil(616 + (64 * 5) - 32, 60 + (64 * 4), 2))