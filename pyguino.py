# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.Colores import Colores
from gameComponents.Pinguino import Pinguino
from gameComponents.Ambiente import Ambiente


def colision(data1, data2):
    # [xPos, yPos, width, height]
    
    pass

colores = Colores()


# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# assigning values to X and Y variable 
X = 700
Y = 400

y_Line = 350

# create the display surface object 
# of specific dimension...(X, Y). 
windowSurface = pygame.display.set_mode((X, Y))
#  ------------------------------------------
#  |[0,0]           x --> X            [n,0]|
#  |                                        |
#  |   y                                    |
#  |   ¦                                    |
#  |   v                                    |
#  |   Y                                    |
#  |                                        |
#  |[0,n]                              [n,n]|
#  ------------------------------------------

# set the pygame window name 
pygame.display.set_caption('Pyguino') 
  
# create a surface object, images are drawn on it.
ambiente = Ambiente(windowSurface, X)
almaPinguino = Pinguino(windowSurface)

# set_timer(eventid, milliseconds) -> None
# Vamos a crear un evento
pygame.time.set_timer (pygame.USEREVENT, 1500 )
pygame.key.set_repeat(1)

#Añadir records

while True : 
   
    # completely fill the surface object 
    # with white colour 
    windowSurface.fill(colores.veryBlue) 

    pygame.draw.line(windowSurface, colores.white, [0,y_Line], [X, y_Line], 5)

    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit()
            # quit the program. 
            quit()
    
        # Update the keyboard readings
        # K_UP -> up arrow
        
        if event.type == pygame.KEYDOWN:
            
            # If up arrow was pressed
            if event.key == pygame.K_UP:
                if almaPinguino.isJumping:
                    pass
                else: 
                    almaPinguino.isJumping = True
                    almaPinguino.setUp(True)
                    
        # En caso de haber pasado un segundo, 
        if event.type == pygame.USEREVENT:
            ambiente.addCactus()
    almaPinguino.show()
    ambiente.move()
    # Draws the surface object to the screen.   
    pygame.display.update()  
    