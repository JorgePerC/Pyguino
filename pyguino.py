# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.Pinguino import Pinguino
from gameComponents.startOver import Background, GameObstacle, SingleImage, Pinguin
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

fondo = Background(X,Y, pinguino)


CambiarTiempo = pygame.USEREVENT + 1
AppendObstaculo = pygame.USEREVENT + 2

## Append events
pygame.time.set_timer(CambiarTiempo, 2000)
pygame.time.set_timer(AppendObstaculo, 1000)

clock = pygame.time.Clock()

# Me permite brincar si dejo presionado
pygame.key.set_repeat(100)

while True : 
    dt = clock.tick(60)
    GameObstacle.dt = dt
    SingleImage.dt = dt
    
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
        
        if event.type == pygame.KEYDOWN:    
            # If up arrow was pressed
            if event.key == pygame.K_UP:
                print("K_Up")
                if not pinguino.isJumping:
                    pinguino.isJumping = True
                    pinguino.isGoingUp = True
            if event.key == pygame.K_DOWN:
                print("K_Down")
                if pinguino.isJumping:
                    pinguino.isGoingUp = False
    
    fondo.draw()
    pygame.display.update()


