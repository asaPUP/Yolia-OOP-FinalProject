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
        self._moviles = pygame.sprite.GroupSingle()

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
        self._metas.add(Meta(20 + (64 * 8) - 32, 60 + (64 * 9)))
        self._metas.add(Meta(616 + (64 * 8) - 32, 60 + (64 * 9)))

    def nivel2(self):
        self._metas.empty()
        self._metas.add(Meta(20 + (64 * 2) - 32, 60 + (64 * 2)))
        self._metas.add(Meta(616 + (64 * 9) - 32, 60 + (64 * 1)))

        self._paredes.empty()
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 5), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 2) - 32, 60 + (64 * 1), 'piedra'))
        self._paredes.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 2), 'piedra'))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 4), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 4), 'hoyo'))
        self._paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 1), 'hoyo'))