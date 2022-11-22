import pygame
from jugador import Jugador
from nivel import Nivel

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
                Nivel.cont_nivel = 1
                break

##========================================# PLAYERS #======================================================#

player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(1))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(2))

#Lista de objetos de tipo jugador, que a la vez son group single por necesidad de pygame
jugadores = [player1, player2]

##=======================================# CONTADORES Y LIMITANTES #=======================================#

nivel = Nivel()

# Lista de objetos de diferentes clases (todos son grupo por necesidades de pygame, pero cada grupo tiene diferentes clases)
elementos = [nivel.estaticos, nivel.movil1, nivel.movil2]

contador_fin = 0

game_active = False
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
            pos_ant1 = (jugadores[0].sprite.rect.x, jugadores[0].sprite.rect.y)
            pos_ant2 = (jugadores[1].sprite.rect.x, jugadores[1].sprite.rect.y)
            Jugador.player_input(event, jugadores[0], jugadores[1])

    if game_active:
        #IMPRIME FONDO
        WIN.blit(fondo_surface, (0,0))

        for elemento in elementos: # Se recorre la lista de objetos elementos
            elemento.draw(WIN) # Se dibujan todos los elementos del nivel
            
            #=================== INTERACCION CON ELEMENTOS ESTATICOS
            if elemento == nivel.estaticos:
                for i in range(len(nivel.estaticos)):
                    #=================== DETECTA SI LLEGA A LA META
                    if(elemento.sprites()[i].tipo == "meta"):
                        if (elemento.sprites()[i].collision(jugadores[0].sprite) and elemento.sprites()[i + 1].collision(jugadores[1].sprite)):
                            llego = True
                            contador_fin += 1
                            if contador_fin == 30: # 30 frames = 1/2 segundo, cuando el contador llega a 30, se pasa al siguiente nivel
                                game_active = False
                                Nivel.cont_nivel += 1

                    #=================== COLISION CON PARED
                    if(elemento.sprites()[i].tipo == "pared"):
                        if (elemento.sprites()[i].collision(jugadores[0].sprite)):
                            jugadores[0].sprite.rect.x = pos_ant1[0]
                            jugadores[0].sprite.rect.y = pos_ant1[1]
                        
                        if (elemento.sprites()[i].collision(jugadores[1].sprite)):
                            jugadores[1].sprite.rect.x = pos_ant2[0]
                            jugadores[1].sprite.rect.y = pos_ant2[1]
                    
                    #=================== COLISION CON PICOS
                    if(elemento.sprites()[i].tipo == "pico"):
                        if (elemento.sprites()[i].collision(jugadores[0].sprite) or elemento.sprites()[i].collision(jugadores[1].sprite)):
                            jugadores[0].sprite.restart() # Se reinicia la posicion de los jugadores
                            jugadores[1].sprite.restart()

                            # Reiniciar la posicion de los moviles
                            if nivel.movil1 and nivel.movil2:
                                elementos[1].sprite.restart()
                                elementos[2].sprite.restart()
            else:
                #=================== EMPUJAR MOVILES
                if nivel.movil1 and nivel.movil2:
                    if(elementos[1].sprite.collision(jugadores[0].sprite)):
                        elementos[1].sprite.mover(pos_ant1)

                        if (player1.sprite.rect.x + 64 > 532 or player1.sprite.rect.x - 64 < 20):
                            player1.sprite.rect.x = pos_ant1[0]
                        if (player1.sprite.rect.y + 64 > 572 or player1.sprite.rect.y - 64 < 60):
                            player1.sprite.rect.y = pos_ant1[1]

                    if(elementos[2].sprite.collision(jugadores[1].sprite)):
                        elementos[2].sprite.mover(pos_ant2)

                        if (player2.sprite.rect.x + 64 > 1128 or player2.sprite.rect.x - 64 < 616):
                            player2.sprite.rect.x = pos_ant2[0]
                        if (player2.sprite.rect.y + 64 > 572 or player2.sprite.rect.y - 64 < 60):
                            player2.sprite.rect.y = pos_ant2[1]

        #=================== DIBUJA JUGADORES
        for player in jugadores:
            player.draw(WIN)
            player.sprite.animation_state()
        
        #=================== DIBUJA TITULO
        text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 60)
        text_surface = text_font.render('YOLIA', False, 'Black')
        text_rectangle = text_surface.get_rect(center = (WIDTH/2, 25))
        WIN.blit(text_surface, text_rectangle)

    else:
        game_active = True
        contador_fin = 0
        llego = False

        #PLAYERS
        for player in jugadores:
            player.sprite.restart()

        if Nivel.cont_nivel == 1:
            nivel.nivel1()
        if Nivel.cont_nivel == 2:
            nivel.nivel2()
        if Nivel.cont_nivel == 3:
            nivel.nivel3()
        if Nivel.cont_nivel == 4:
            nivel.nivel4()
        if Nivel.cont_nivel == 5:
            WIN.blit(titulo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
    