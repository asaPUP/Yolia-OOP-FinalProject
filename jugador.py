import pygame

class Jugador(pygame.sprite.Sprite):        # Clase que hereda de Sprite (pygame) para definir a cada jugador
    def __init__(self, religion):
        super().__init__()                  # Inicializa la clase padre (Sprite)

        self._religion = religion           # Religion del jugador

        if self._religion == 1:             # Posicion inicial del jugador, dependiendo de su religion
            self._x = 308
            self._y = 380
        else:
            self._x = 904
            self._y = 380

        self.cargar_imagen()                # Carga las imagenes del jugador

    def cargar_imagen(self):                # Metodo para cargar la imagenes de la animacion del sprite, dependiendo de la religion del jugador
        #==================== MEXICA ====================#
        if self._religion == 1:
            jugador1 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek1.png').convert_alpha())
            jugador2 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek2.png').convert_alpha())
            jugador3 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek3.png').convert_alpha())
            jugador4 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek4.png').convert_alpha())
            jugador5 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek5.png').convert_alpha())
            jugador6 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek6.png').convert_alpha())
            jugador7 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek7.png').convert_alpha())
            jugador8 = pygame.transform.scale2x(pygame.image.load('assets/Canek/Canek8.png').convert_alpha())

        #=================== CRISTIANO ===================#
        else:
            jugador1 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb1.png').convert_alpha())
            jugador2 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb2.png').convert_alpha())
            jugador3 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb3.png').convert_alpha())
            jugador4 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb4.png').convert_alpha())
            jugador5 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb5.png').convert_alpha())
            jugador6 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb6.png').convert_alpha())
            jugador7 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb7.png').convert_alpha())
            jugador8 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb8.png').convert_alpha())
        
        self._jugador_walk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]   # Lista con las imagenes del jugador (caminando)
        
        self._jugador_index = 0                                             # Indice de la lista de imagenes del jugador
        self._image = self._jugador_walk[self._jugador_index]               # Imagen actual del jugador
        self._rect = self._image.get_rect(midbottom = (self._x, self._y))   # Rectangulo del jugador

    @property               # Getter de la imagen del jugador
    def image(self):
        return self._image
    
    @property               # Getter del rectangulo del jugador
    def rect(self):
        return self._rect

    def animation_state(self):      # Metodo para cambiar la imagen del jugador, mostrando la animaciOn de caminar
        self._jugador_index += 0.1
        if self._jugador_index >= len(self._jugador_walk):
            self._jugador_index = 0
        self._image = self._jugador_walk[int(self._jugador_index)]
    
    @staticmethod
    def player_input(event, player1, player2):      # Metodo estatico para recibir input del jugador, ambos se mueven al mismo tiempo
        #=================== MOVIMIENTO ===================#
        if event.key == pygame.K_DOWN:              # Cada jugador se mueve hacia la direccion que se presione 
            player1.sprite.rect.y += 64
            player2.sprite.rect.y += 64

        if event.key == pygame.K_UP:
            player1.sprite.rect.y -= 64
            player2.sprite.rect.y -= 64

        if event.key == pygame.K_LEFT:
            player1.sprite.rect.x -= 64
            player2.sprite.rect.x -= 64

        if event.key == pygame.K_RIGHT:
            player1.sprite.rect.x += 64
            player2.sprite.rect.x += 64
        
        #=================== LIMITES DEL MAPA EN Y ===================#
        if player1.sprite.rect.y  > 572:
            player1.sprite.rect.y = 572
        if player1.sprite.rect.y  < 60:
            player1.sprite.rect.y = 60

        if player2.sprite.rect.y  > 572:
            player2.sprite.rect.y = 572 
        if player2.sprite.rect.y  < 60:
            player2.sprite.rect.y = 60

        #=================== LIMITES DEL MAPA EN X ===================#
        if player1.sprite.rect.x  > 532:
            player1.sprite.rect.x = 532
        if player1.sprite.rect.x  < 20:
            player1.sprite.rect.x = 20

        if player2.sprite.rect.x  > 1128:
            player2.sprite.rect.x = 1128 
        if player2.sprite.rect.x  < 616:
            player2.sprite.rect.x = 616

    def restart(self):            # Metodo para reiniciar la posicion de cada jugador
        if self._religion == 1:
            self._rect = self._image.get_rect(midbottom = (308, 380))
        else:
            self._rect = self._image.get_rect(midbottom = (904, 380))

