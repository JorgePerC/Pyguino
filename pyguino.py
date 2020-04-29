# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.Colores import Colores
from gameComponents.Pinguino import Pinguino
from gameComponents.Ambiente import Ambiente
# from gameComponents.AllGame import Colores, Pinguino, Ambiente

# Somebody on the internet, said I should investigate engines to make my program
# more efficient. https://www.youtube.com/watch?v=lpGNeS-yRDo
# async lib

def colision(data1, data2):
    if (data1[1] < data2[1]-data2[3]) and (data1[0] + data1[2] > data2[0]):
        return True
    else:
        return False

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
ambiente = Ambiente(windowSurface)
almaPinguino = Pinguino(windowSurface)

# set_timer(eventid, milliseconds) -> None
# Vamos a crear un evento
pygame.time.set_timer (pygame.USEREVENT, 1500 )

# Me permite brincar si dejo presionado
pygame.key.set_repeat(100)

#Añadir records

# completely fill the surface object
windowSurface.fill(colores.veryBlue) 
# Draw a rectangle
pygame.draw.rect(windowSurface,colores.white,(0,y_Line, X, Y-y_Line))
clock = pygame.time.Clock

while True : 
    clock.tick_busy_loop(40) 
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
                if not almaPinguino.isJumping:
                    almaPinguino.isJumping = True
                    almaPinguino.up_down = True
            if event.key == pygame.K_DOWN:
                if almaPinguino.isJumping:
                    almaPinguino.up_down = False
                    
        # En caso de haber pasado un segundo,
        # añadir nuevo obstaculo 
        if event.type == pygame.USEREVENT:
            ambiente.addCactus()

    ambiente.move()
    almaPinguino.show()
    # if colision(almaPinguino.pinguinData(), ambiente.incomingObstacleData()):
    #     print("K")
    # Draws the surface object to the screen.   
    pygame.display.update()  
    