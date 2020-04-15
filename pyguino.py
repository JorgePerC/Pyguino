# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.Colores import Colores

colores = Colores()

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# assigning values to X and Y variable 
X = 700
Y = 700

y_Line = 350

x_Axis = np.linspace(-400, X, 100, endpoint=True)
y_Axis = np.linspace(0, y_Line, endpoint=True)

# create the display surface object 
# of specific dimension..e(X, Y). 
windowSurface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Pyguino') 
  
# create a surface object, image is drawn on it. 
pinguino = pygame.image.load("resources/pinguino.png") 
montana = pygame.image.load("resources/montana.png") 

x_pos = 0
y_pos = 0
while True : 
  
    # completely fill the surface object 
    # with white colour 
    windowSurface.fill(colores.black) 

    pygame.draw.line(windowSurface, colores.white, [0,y_Line], [X, y_Line], 5)
  
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    
    windowSurface.blit(pinguino, (x_Axis[x_pos], 0)) 

    windowSurface.blit(montana, (10, y_Axis[0])) 
    
    
    
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
                y_pos +=1
    
    # Draws the surface object to the screen.   
    pygame.display.update()  
    if x_pos == -len(x_Axis):
        x_pos = len(x_Axis)-1
    else:
        x_pos -= 1