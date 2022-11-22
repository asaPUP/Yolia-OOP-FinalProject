import pygame
from obstaculo import Obstaculo

class Movil(Obstaculo):
    def __init__(self, x, y, religion):
        super().__init__(x, y, religion)    # Llama al constructor de la clase padre

        self._tipo = "movil"                # Define el tipo de obstaculo
        
        self._start_x = self._x             # Guarda la posicion inicial del obstaculo, para poder reiniciarla
        self._start_y = self._y             # Guarda la posicion inicial del obstaculo, para poder reiniciarla

        self.cargar_imagen()

    def cargar_imagen(self):                # Sobreescritura polimorfica del metodo abstracto
        if self._religion == 1:
            self._image = pygame.image.load('assets/Escultura/escultura.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x
        else:
            self._image = pygame.image.load('assets/Estatuas/estatua.png').convert_alpha() # Carga imagen
            self._image = pygame.transform.scale2x(self._image) # Escala imagen a 2x

        self._rect = self._image.get_rect(midbottom = (self._x, self._y))
    
    def mover(self, pos_ant_jugador):
        # Detecta la posicion del jugador a comparacion del obstaculo, y mueve el obstaculo correspondientemente
        if pos_ant_jugador[1] > self._rect.y: 
            #ABAJO A ARRIBA
            self._rect.y -= 64
            
        elif pos_ant_jugador[1] < self._rect.y:
            #ARRIBA A ABAJO
            self._rect.y += 64

        elif pos_ant_jugador[0] > self._rect.x:
            #DERECHA A IZQUIERDA
            self._rect.x -= 64

        elif pos_ant_jugador[0] < self._rect.x:
            #EMPUJA A LA DERECHA
            self._rect.x += 64

        ############LIMITES DE MOVIMIENTO DEL OBSTACULO############
        # Los limites del mapa dependen de la religion del obstaculo
        if self._religion == 1:         
            if self._rect.x  > 532:
                self._rect.x = 532

            if self._rect.x  < 20:
                self._rect.x = 20

            if self._rect.y  > 572:
                self._rect.y = 572
                
            if self._rect.y  < 60:
                self._rect.y = 60

        elif self._religion == 2:
            if self._rect.x  > 1128:
                self._rect.x = 1128

            if self._rect.x  < 616:
                self._rect.x = 616

            if self._rect.y  > 572:
                self._rect.y = 572

            if self._rect.y  < 60:
                self._rect.y = 60
    
    def restart(self):                  # Metodo para reinicar la posicion del obstaculo
        self._rect = self._image.get_rect(midbottom = (self._start_x, self._start_y))