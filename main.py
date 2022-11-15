import pygame
from jugador import Jugador
from obstaculo import Obstaculo
from nivel import Nivel

from pared import Pared
from meta import Meta
from pico import Pico
from movil import Movil

from sys import exit

##========================================# INICIALIZACION #================================================#

pygame.init()

WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("YOLIA")

clock = pygame.time.Clock()

##========================================# MUSICA #========================================================#

pygame.mixer.init()
pygame.mixer.music.load("music/musica.wav")
pygame.mixer.music.play(-1)

##========================================# CARGA DE FUENTE Y FONDO #=======================================#

text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 64)
fondo_surface = pygame.image.load('assets/Fondos/FondoMarco.png').convert()
fondo_surface = pygame.transform.scale2x(fondo_surface)

##========================================# PANTALLA DE TITULO #============================================#

titulo_surface = pygame.image.load("assets/fondo.png").convert()
nombre_surface = pygame.image.load("assets/Titulo.png").convert()
nombre_surface = pygame.transform.scale2x(nombre_surface)

menu = True

while menu == True:
    WIN.blit(titulo_surface, (0,0))
    WIN.blit(nombre_surface, (200,50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
                game_active = True
                cont_nivel = 1
                break

##========================================# PLAYERS #======================================================#

player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(1))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(2))

##=======================================# CONTADORES Y LIMITANTES #=======================================#

cont_nivel = 0
nivel = Nivel()
game_active = False
contador_fin = 0
llego = False

WIN.blit(nombre_surface, (200,50))

##========================================# LOOP DEL JUEGO #===============================================#

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #DETECTAR TECLAS
        if (event.type == pygame.KEYDOWN and llego == False):
            pos_ant1 = (player1.sprite.rect.x, player1.sprite.rect.y)
            pos_ant2 = (player2.sprite.rect.x, player2.sprite.rect.y)
            Jugador.playerInput(event, player1, player2)

    if game_active:
        #IMPRIME FONDO
        WIN.blit(fondo_surface, (0,0))
        
        #IMPRIME METAS
        WIN.blit(meta1.image, meta1.rect)
        WIN.blit(meta2.image, meta2.rect)

        #IMPRIME MOVILES
        WIN.blit(movil1.image, movil1.rect)
        WIN.blit(movil2.image, movil2.rect)

        #EMPUJAR MOVILES
        if(player1.sprite.collision(movil1)):
            movil1.mover(pos_ant1)

            if (player1.sprite.rect.x + 64 > 532 or player1.sprite.rect.x - 64 < 20):
                player1.sprite.rect.x = pos_ant1[0]
            if (player1.sprite.rect.y + 64 > 572 or player1.sprite.rect.y - 64 < 60):
                player1.sprite.rect.y = pos_ant1[1]

        if(player2.sprite.collision(movil2)):
            movil2.mover(pos_ant2)

            if (player2.sprite.rect.x + 64 > 1128 or player2.sprite.rect.x - 64 < 616):
                player2.sprite.rect.x = pos_ant2[0]
            if (player2.sprite.rect.y + 64 > 572 or player2.sprite.rect.y - 64 < 60):
                player2.sprite.rect.y = pos_ant2[1]
                

        #DIBUJA PICOS
        picos.draw(WIN)

        #DIBUJA PAREDES
        paredes.draw(WIN)

        #DETECTA SI LLEGA A LA META
        if (player1.sprite.llega_meta(obstaculos) and player2.sprite.llega_meta(meta2)):
            llego = True
            contador_fin += 1

        if contador_fin == 30:
            game_active = False                

        #=================== COLISION CON PICOS

        for i in range (len(picos)):
            if(player1.sprite.rect.colliderect(picos.sprites()[i].rect) or player2.sprite.rect.colliderect(picos.sprites()[i].rect)):
                player1.sprite.restart()
                movil1.reiniciar()
                player2.sprite.restart()
                movil2.reiniciar()

        #=================== COLISION CON PARED

        for i in range (len(paredes)):
            if(player1.sprite.rect.colliderect(paredes.sprites()[i].rect)):
                player1.sprite.rect.x = pos_ant1[0]
                player1.sprite.rect.y = pos_ant1[1]
            
            if(player2.sprite.rect.colliderect(paredes.sprites()[i].rect)):
                player2.sprite.rect.x = pos_ant2[0]
                player2.sprite.rect.y = pos_ant2[1]

        # MANTENERLOS AL FINAL DEL CICLO
        player1.draw(WIN)
        player1.animation_state()
        
        player2.draw(WIN)
        player2.animation_state()

        text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 60)
        text_surface = text_font.render('YOLIA', False, 'Black')

        text_rectangle = text_surface.get_rect(center = (WIDTH/2, 25))
        WIN.blit(text_surface, text_rectangle)

    else:
        game_active = True
        cont_nivel += 1
        contador_fin = 0
        llego = False

        #PLAYERS
        player1.remove(player1.sprite)
        player2.remove(player2.sprite)
        
        player1.add(Jugador(1))
        player2.add(Jugador(2))

        if cont_nivel == 1:
            nivel.cont_nivel1()
        if cont_nivel == 2:
            nivel.cont_nivel2()
        if cont_nivel == 3:
            nivel.cont_nivel3()
        if cont_nivel == 4:
            nivel.cont_nivel4()
        if cont_nivel == 5:
            WIN.blit(titulo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
    