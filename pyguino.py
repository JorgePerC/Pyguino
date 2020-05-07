# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.startOver import Background, GameObstacle, SingleImage, Pinguin, Score
# from gameComponents.AllGame import Colores, Pinguino, Ambiente

# Somebody on the internet, said I should investigate engines to make my program
# more efficient. https://www.youtube.com/watch?v=lpGNeS-yRDo
# async lib

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# assigning values to X and Y variable 
X = 700
Y = 400

pinguino = Pinguin()
marcador = Score()

fondo = Background(X,Y, pinguino, marcador)

CambiarTiempo = pygame.USEREVENT + 1
AppendObstaculo = pygame.USEREVENT + 2
MurioJugador = pygame.USEREVENT + 3

GameOver = pygame.event.Event(MurioJugador, message="Bad cat!")

## Append events
pygame.time.set_timer(CambiarTiempo, 5000)
pygame.time.set_timer(AppendObstaculo, 1500)

clock = pygame.time.Clock()

# Me permite brincar si dejo presionado
pygame.key.set_repeat(100)

showEndGame = False

while True : 
    dt = clock.tick(60)
    GameObstacle.dt = dt
    SingleImage.dt = dt
    Score.dt = dt
    
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit()
            # quit the program. 
            quit()
        if event.type == CambiarTiempo:
            fondo.state = not(fondo.state)
            GameObstacle.dayTime = not(GameObstacle.dayTime) #How to MODIFY a class variable
        if event.type == AppendObstaculo:
            fondo.addObstacle(GameObstacle())
        if event.type == MurioJugador:
            marcador.active = False
            showEndGame = True
            
        
        if event.type == pygame.KEYDOWN:    
            # If up arrow was pressed
            if event.key == pygame.K_UP:
                if not pinguino.isJumping:
                    pinguino.isJumping = True
                    pinguino.isGoingUp = True
            if event.key == pygame.K_DOWN:
                if pinguino.isJumping:
                    pinguino.isGoingUp = False
    # Está así para ver si en un futuro encuentro una
    # solución más modular
    if Background.jugadorIsDead:
        pygame.event.post(GameOver)
    
    if showEndGame:
        fondo.gameOver()    
    else:
        fondo.draw()
    
    pygame.display.update()
    


