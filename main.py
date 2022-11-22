import pygame
from jugador import Jugador
from nivel import Nivel
from sys import exit

##========================================# INICIALIZACION #================================================#

pygame.init()                                   # Inicializacion de pygame

WIDTH, HEIGHT = 1212, 656                       # Dimensiones de la ventana
WIN = pygame.display.set_mode((WIDTH,HEIGHT))   # Creacion de la ventana

pygame.display.set_caption("YOLIA")             # Titulo de la ventana en windows

clock = pygame.time.Clock()                     # Inicializacion del reloj para el tiempo de ejecucion

##========================================# MUSICA #========================================================#

pygame.mixer.init()                           # Inicializacion de mixer para la musica
pygame.mixer.music.load("music/musica.wav")   # Carga el archivo de musica
pygame.mixer.music.play(-1)                   # Reproduce de la musica en bucle

##========================================# CARGA DE FUENTE Y FONDO #=======================================#

text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 64)                     # Carga la fuente del texto
fondo_surface = pygame.image.load('assets/Fondos/FondoMarco.png').convert() # Carga la imagen del fondo
fondo_surface = pygame.transform.scale2x(fondo_surface)

##========================================# PANTALLA DE TITULO #============================================#

titulo_surface = pygame.image.load("assets/fondo.png").convert() # Carga imagen de fondo

menu = True 

while menu == True: # Mientras el menu este activo
    WIN.blit(titulo_surface, (0,0))         # Dibuja la pantalla de titulo
    pygame.display.update()                 # Actualiza la pantalla
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:       # Si se presiona la X de la ventana, se cierra el juego
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:    # Si se presiona cualquier tecla, se sale del menu y se inicia el juego
            if event.key == pygame.K_SPACE:
                menu = False
                game_active = True
                break

##========================================# PLAYERS #======================================================#

player1 = pygame.sprite.GroupSingle()   # Se instancia un grupo single de sprites para el jugador 1, por la forma en que pygame maneja los sprites
player1.add(Jugador(1))                 # Se agrega el sprite del jugador 1 al grupo

player2 = pygame.sprite.GroupSingle()   # Se instancia un grupo single de sprites para el jugador 2, por la forma en que pygame maneja los sprites
player2.add(Jugador(2))                 # Se agrega el sprite del jugador 2 al grupo

#Lista de objetos de tipo jugador, que a la vez son group single por necesidad de pygame
jugadores = [player1, player2]

##=======================================# CONTADORES Y LIMITANTES #=======================================#

nivel = Nivel()         # Se instancia al objeto de tipo nivel

# Lista de objetos de diferentes clases (todos son grupo por necesidades de pygame, pero cada grupo tiene diferentes clases)
elementos = [nivel.estaticos, nivel.movil1, nivel.movil2]

game_active = False     # Variable que controla si el juego esta activo o no
llego = False           # Variable que controla si el jugador llego a la meta o no, para detener los inputs
contador_fin = 0        # Contador para detener el juego desde que se llega a la meta hasta que se pasa de nivel

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
                            llego = True                # Si ambos jugadores llegan a la meta, no puede moverse hasta pasar al siguiente nivel
                            contador_fin += 1           # Se cuenta un tiempo de espera para pasar de nivel
                            if contador_fin == 30:      # 30 frames = 1/2 segundo, cuando el contador llega a 30, se pasa al siguiente nivel
                                game_active = False     # Se desactiva el juego, para pasar de nivel

                    #=================== COLISION CON PARED
                    if(elemento.sprites()[i].tipo == "pared"):
                        # Si el jugador 1 colisiona con una pared, se devuelve a su posicion anterior
                        if (elemento.sprites()[i].collision(jugadores[0].sprite)):
                            jugadores[0].sprite.rect.x = pos_ant1[0]
                            jugadores[0].sprite.rect.y = pos_ant1[1]
                        
                        # Si el jugador 2 colisiona con una pared, se devuelve a su posicion anterior
                        if (elemento.sprites()[i].collision(jugadores[1].sprite)):
                            jugadores[1].sprite.rect.x = pos_ant2[0]
                            jugadores[1].sprite.rect.y = pos_ant2[1]
                    
                    #=================== COLISION CON PICOS
                    if(elemento.sprites()[i].tipo == "pico"):
                        if (elemento.sprites()[i].collision(jugadores[0].sprite) or elemento.sprites()[i].collision(jugadores[1].sprite)):
                            jugadores[0].sprite.restart() # Se reinicia la posicion de los jugadores
                            jugadores[1].sprite.restart()

                            # Reinicia la posicion de los moviles
                            if nivel.movil1 and nivel.movil2:
                                elementos[1].sprite.restart()
                                elementos[2].sprite.restart()
            else:
                #=================== EMPUJAR MOVILES
                if nivel.movil1 and nivel.movil2:   # Si hay moviles en el nivel
                    if(elementos[1].sprite.collision(jugadores[0].sprite)):                     # Si el jugador 1 colisiona con el movil 1
                        movil1_ant = (elementos[1].sprite.rect.x, elementos[1].sprite.rect.y)   # Se guarda la posicion anterior del movil1 antes de moverlo

                        elementos[1].sprite.mover(pos_ant1) # Se mueve el movil1

                        # Si el movil1 colisiona con una pared, el jugador1 vuelve a su posicion anterior
                        if (player1.sprite.rect.x + 64 > 532 or player1.sprite.rect.x - 64 < 20): 
                            player1.sprite.rect.x = pos_ant1[0]
                        if (player1.sprite.rect.y + 64 > 572 or player1.sprite.rect.y - 64 < 60):
                            player1.sprite.rect.y = pos_ant1[1]

                    if(elementos[2].sprite.collision(jugadores[1].sprite)):                     # Si el jugador 2 colisiona con el movil 2
                        movil2_ant = (elementos[2].sprite.rect.x, elementos[2].sprite.rect.y)   # Se guarda la posicion anterior del movil2 antes de moverlo

                        elementos[2].sprite.mover(pos_ant2) # Se mueve el movil2

                        # Si el movil2 se sale del mapa, el jugador1 vuelve a su posicion anterior
                        if (player2.sprite.rect.x + 64 > 1128 or player2.sprite.rect.x - 64 < 616):
                            player2.sprite.rect.x = pos_ant2[0]
                        if (player2.sprite.rect.y + 64 > 572 or player2.sprite.rect.y - 64 < 60):
                            player2.sprite.rect.y = pos_ant2[1]

                    # Si cualquier movil colisiona con un pico o una pared, se vuelve a su posicion anterior y el jugador vuelve a su posicion anterior
                    for barrera in elementos:
                        for i in range(len(barrera)):
                            if (barrera.sprites()[i].tipo == "pico" or barrera.sprites()[i].tipo == "pared"):
                                if (elementos[1].sprite.collision(barrera.sprites()[i])):
                                    elementos[1].sprite.rect.x = movil1_ant[0]
                                    elementos[1].sprite.rect.y = movil1_ant[1]
                                    jugadores[0].sprite.rect.x = pos_ant1[0]
                                    jugadores[0].sprite.rect.y = pos_ant1[1]
                                
                                if (elementos[2].sprite.collision(barrera.sprites()[i])):
                                    elementos[2].sprite.rect.x = movil2_ant[0]
                                    elementos[2].sprite.rect.y = movil2_ant[1]
                                    jugadores[1].sprite.rect.x = pos_ant2[0]
                                    jugadores[1].sprite.rect.y = pos_ant2[1]

        #=================== DIBUJA A LOS JUGADORES
        for player in jugadores:
            player.draw(WIN)
            player.sprite.animation_state()
        
        #=================== DIBUJA TITULO ARRIBA
        text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 60)
        text_surface = text_font.render('YOLIA', False, 'White')
        text_rectangle = text_surface.get_rect(center = (WIDTH/2, 25))
        WIN.blit(text_surface, text_rectangle)

    else: # Si el juego no esta activo, se pasa al siguiente nivel
        Nivel.cont_nivel += 1           # Se aumenta el contador de nivel
        if Nivel.cont_nivel < 5:        # Si el contador de nivel es menor a 5, el juego sigue
            game_active = True          # Se vuelve a activar el juego
        contador_fin = 0                # Se reinicia el contador de frames en la meta
        llego = False

        for player in jugadores:        # Se reinicia la posicion de los jugadores
            player.sprite.restart()

        if Nivel.cont_nivel == 1:       # Se activa el nivel correspondiente
            nivel.nivel1()
        if Nivel.cont_nivel == 2:
            nivel.nivel2()
        if Nivel.cont_nivel == 3:
            nivel.nivel3()
        if Nivel.cont_nivel == 4:
            nivel.nivel4()
        if Nivel.cont_nivel == 5:       # Si el contador de nivel es 5, se termina el juego
            final_surface = pygame.image.load("assets/final.png").convert() # Carga imagen de fondo
            WIN.blit(final_surface, (0,0))                                  # Dibuja imagen de fondo
            game_active = False                                             # Se desactiva el juego

    pygame.display.update()
    clock.tick(60)
    