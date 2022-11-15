import pygame
from pared import Pared
from meta import Meta
from pico import Pico
from movil import Movil

class Nivel(object):
    def __init__(self):
        self._paredes = pygame.sprite.Group()
        self._metas = pygame.sprite.Group()
        self._picos = pygame.sprite.Group()
        self._movil1 = pygame.sprite.GroupSingle()  # El moimiento es indepentiente por cada objeto, debe de estar en un grupo unico
        self._movil2 = pygame.sprite.GroupSingle()  # ^^^

    @property
    def paredes(self):
        return self._paredes

    @property
    def metas(self):
        return self._metas

    @property
    def picos(self):
        return self._picos
    
    @property
    def moviles(self):
        return self._moviles

    def nivel1(self):
        self._metas.empty()
        self._metas.add(Meta(20 + (64 * 8) - 32, 60 + (64 * 9), 1))
        self._metas.add(Meta(616 + (64 * 8) - 32, 60 + (64 * 9), 2))

    def nivel2(self):
        self._metas.empty()
        self._metas.add(Meta(20 + (64 * 2) - 32, 60 + (64 * 2), 1))
        self._metas.add(Meta(616 + (64 * 9) - 32, 60 + (64 * 1), 2))

        self._paredes.empty()
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 1))
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 5), 1))
        self._paredes.add(Pared(20 + (64 * 2) - 32, 60 + (64 * 1), 1))
        self._paredes.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 2), 1))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 2))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 2))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 1), 2))

    def nivel3(self):
        self._metas.empty()
        self._metas.add(Meta(20 + (64 * 2) - 32, 60 + (64 * 2), 1))
        self._metas.add(Meta(616 + (64 * 8) - 32, 60 + (64 * 8), 2))

        self._paredes.empty()
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 7), 1))
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 8), 1))
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 9), 1))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 1))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 3), 1))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 2), 1))
        self._paredes.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 2), 1))
        self._paredes.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 4), 1))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 3), 2))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 2), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 1), 2))
        self._paredes.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 6), 2))
        self._paredes.add(Pared(616 + (64 * 2) - 32, 60 + (64 * 6), 2))
        self._paredes.add(Pared(616 + (64 * 3) - 32, 60 + (64 * 6), 2))
        self._paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 5), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 6), 2))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 3), 2))
        self._paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 2))
        self._paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 9), 2))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 7), 2))

    def nivel4(self):
        self._metas.empty()
        self._metas.add(Meta(20 + (64 * 3) - 32, 60 + (64 * 5), 1))
        self._metas.add(Meta(616 + (64 * 2) - 32, 60 + (64 * 1), 2))

        self._paredes.empty()
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 1))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 1))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 1))
        self._paredes.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 7), 1))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 1), 1))
        self._paredes.add(Pared(20 + (64 * 7) - 32, 60 + (64 * 2), 1))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 2))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 2))
        self._paredes.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 6), 2))
        self._paredes.add(Pared(616 + (64 * 9) - 32, 60 + (64 * 7), 2))
        self._paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 2))
        self._paredes.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 2), 2))

        self._picos.empty()
        self._picos.add(Pico(20 + (64 * 2) - 32, 60 + (64 * 5), 1))
        self._picos.add(Pico(20 + (64 * 1) - 32, 60 + (64 * 6), 1))
        self._picos.add(Pico(616 + (64 * 1) - 32, 60 + (64 * 1), 2))
        self._picos.add(Pico(616 + (64 * 3) - 32, 60 + (64 * 2), 2))

        self._movil1.empty()
        self._movil1.add(Movil(20 + (64 * 6) - 32, 60 + (64 * 5), 1))

        self._movil2.empty()
        self._movil2.add(Movil(616 + (64 * 5) - 32, 60 + (64 * 4), 2))