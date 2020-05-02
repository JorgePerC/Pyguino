# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.Pinguino import Pinguino
from gameComponents.startOver import Background, GameObstacle
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
fondo = Background(X,Y)
obj = GameObstacle ("Plastic")
obj2 = GameObstacle ("Barrel")

CambiarTiempo = pygame.USEREVENT + 1
AppendObstaculo = pygame.USEREVENT + 1

## Append events
pygame.time.set_timer(CambiarTiempo, 2000)

fondo.addObstacle(obj)
fondo.addObstacle(obj2)

clock = pygame.time.Clock()

while True : 
    dt = clock.tick(60)
    GameObstacle.dt = dt
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit()
            # quit the program. 
            quit()
        if event.type == CambiarTiempo:
            fondo.state = not(fondo.state)
            GameObstacle.dayTime = not(GameObstacle.dayTime) #How to MODIFY a class variable
    
    fondo.draw()
    pygame.display.update()