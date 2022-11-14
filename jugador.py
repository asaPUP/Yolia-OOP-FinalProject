import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, dalt, religion):
        super().__init__()

        self._religion = religion

        if self._religion == 1:
            self._x = 308
            self._y = 380
        else:
            self._x = 904
            self._y = 380

        self._frames = []
        self._frame_index = 0

        #==================== MEXICA ====================#
        if self._religion == 'mexica':
            jugador1 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek1.png').convert_alpha())
            jugador2 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek2.png').convert_alpha())
            jugador3 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek3.png').convert_alpha())
            jugador4 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek4.png').convert_alpha())
            jugador5 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek5.png').convert_alpha())
            jugador6 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek6.png').convert_alpha())
            jugador7 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek7.png').convert_alpha())
            jugador8 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo2/Canek8.png').convert_alpha())

        #=================== CRISTIANO ===================#
        elif self._religion == 'cristiano' :
            jugador1 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0004.png').convert_alpha())
            jugador2 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0005.png').convert_alpha())
            jugador3 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0006.png').convert_alpha())
            jugador4 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0007.png').convert_alpha())
            jugador5 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0008.png').convert_alpha())
            jugador6 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0009.png').convert_alpha())
            jugador7 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0010.png').convert_alpha())
            jugador8 = pygame.transform.scale2x(pygame.image.load('assets/uglyAssMofo/Sprite-0011.png').convert_alpha())
        
        self._jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
        
        self._jugador_index = 0
        self._image = self.jugadorWalk[self._jugador_index]
        self._rect = self._image.get_rect(midbottom = (self._x, self._y))

    def animationState(self):
        self.jugador_index += 0.1
        if self.jugador_index >= len(self.jugadorWalk):
            self.jugador_index = 0
        self.image = self.jugadorWalk[int(self.jugador_index)]
    
    @staticmethod
    def playerInput(event, player1, player2):

        #=================== MOVIMIENTO ===================#

        if event.key == pygame.K_DOWN:
            print('down')
            player1.sprite.rect._y += 64
            player2.sprite.rect._y += 64

        if event.key == pygame.K_UP:
            print('up')
            player1.sprite.rect._y -= 64
            player2.sprite.rect._y -= 64

        if event.key == pygame.K_LEFT:
            print('left')
            player1.sprite.rect._x -= 64
            player2.sprite.rect._x -= 64

        if event.key == pygame.K_RIGHT:
            print('right')
            player1.sprite.rect._x += 64
            player2.sprite.rect._x += 64
        
        #=================== LIMITES PARA Y ===================#
        if player1.sprite.rect._y  > 572:
            player1.sprite.rect._y = 572
        if player1.sprite.rect._y  < 60:
            player1.sprite.rect._y = 60

        if player2.sprite.rect._y  > 572:
            player2.sprite.rect._y = 572 
        if player2.sprite.rect._y  < 60:
            player2.sprite.rect._y = 60
        #=================== LIMITES PARA X ===================#
        if player1.sprite.rect._x  > 532:
            player1.sprite.rect._x = 532
        if player1.sprite.rect._x  < 20:
            player1.sprite.rect._x = 20

        if player2.sprite.rect._x  > 1128:
            player2.sprite.rect._x = 1128 
        if player2.sprite.rect._x  < 616:
            player2.sprite.rect._x = 616
    
    def llega_meta(self, meta):
        if self.rect.colliderect(meta.rect):
            return True
        else:
            return False

    def collision(self, objetos):
        if self.rect.colliderect(objetos.rect):
            return True
        else:
            return False

    def restart(self):
        if self._religion == 'mexica':
            self.rect = self.image.get_rect(midbottom = (308, 380))
        else:
            self.rect = self.image.get_rect(midbottom = (904, 380))

