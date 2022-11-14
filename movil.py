import pygame
from obstaculo import Obstaculo

class Movil(Obstaculo):
    def __init__(self):
        super().__init__()

        self._tipo = "movil"
        
        self._start_x = self._x
        self._start_y = self._y

        if self._religion == 1:
            self._image = pygame.image.load('assets/Escultura/escultura.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x

        else:
            self._image = pygame.image.load('assets/Estatuas/estatua.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x

        self._rect = self._image.get_rect(midbottom = (self._x, self._y))

    def collision(self, jugador):
        if self._rect.colliderect(jugador._rect):
            return True
    
    def mover(self, pos_anterior):
        if pos_anterior[1] > self._rect.y:
            #ABAJO A ARRIBA
            self._rect.y -= 64
            
        elif pos_anterior[1] < self._rect.y:
            #ARRIBA A ABAJO
            self._rect.y += 64

        elif pos_anterior[0] > self._rect.x:
            #DERECHA A IZQUIERDA
            self._rect.x -= 64

        elif pos_anterior[0] < self._rect.x:
            #EMPUJA A LA DERECHA
            self._rect.x += 64

        ############LIMITES############
        if self._religion == 1:
            if self._rect.x  > 1128:
                self._rect.x = 1128

            if self._rect.x  < 616:
                self._rect.x = 616

            if self._rect.y  > 572:
                self._rect.y = 572

            if self._rect.y  < 60:
                self._rect.y = 60
        
        else:
            if self._rect.x  > 532:
                self._rect.x = 532

            if self._rect.x  < 20:
                self._rect.x = 20

            if self._rect.y  > 572:
                self._rect.y = 572
                
            if self._rect.y  < 60:
                self._rect.y = 60
    
    def reiniciar(self):
        self._rect = self._image.get_rect(midbottom = (self._start_x, self._start_y))