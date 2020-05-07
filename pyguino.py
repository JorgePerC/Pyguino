# Juego tipo Dino Chrome, verisón Pingüino
# En colaboración con Valera π
# Link a la documentación: https://www.pygame.org/docs

import pygame
import numpy as np
from gameComponents.startOver import Background, GameObstacle, SingleImage, Pinguin, Score

# Somebody on the internet, said I should investigate engines to make my program
# more efficient. https://www.youtube.com/watch?v=lpGNeS-yRDo
# async lib

# Activate the pygame library. 
# Initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# assigning values to X and Y variable 
X = 700
Y = 400

#Create a Pinguin and scoring Object.
pinguino = Pinguin()
marcador = Score()

# Creates the background
# Check StarOver
fondo = Background(X,Y, pinguino, marcador)

#Create custom events
CambiarTiempo = pygame.USEREVENT + 1
AppendObstaculo = pygame.USEREVENT + 2
MurioJugador = pygame.USEREVENT + 3

# Create event of event Type
GameOver = pygame.event.Event(MurioJugador, message="Bad cat!")

# Append events based on time
pygame.time.set_timer(CambiarTiempo, 5000)
pygame.time.set_timer(AppendObstaculo, 1500)

# Create clock Object, necesary for dt
# More on startOver
clock = pygame.time.Clock()

# Allows me to jump is key is pressed
pygame.key.set_repeat(100)

# Tells me when to show the end image
showEndGame = False

while True : 
    # slice a second 60 times
    dt = clock.tick(60)
    GameObstacle.dt = dt
    SingleImage.dt = dt
    Score.dt = dt

    # iterate over the list of Event objects 
        # that is returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit()
            # quit the program. 
            quit()

        # In case nMiliseconds pass
        # an event will be added to the queue
        if event.type == CambiarTiempo:
            # Chage backgroud settings
            fondo.isDay = not(fondo.isDay)
            GameObstacle.dayTime = not(GameObstacle.dayTime) 
                                        # How to MODIFY a class variable
        if event.type == AppendObstaculo:
            # Add new obstacle
            fondo.addObstacle(GameObstacle())
        if event.type == MurioJugador:
            # Show final mark
            marcador.active = False
            showEndGame = True
            
        # Update the keyboard readings
        # K_UP -> up arrow
        if event.type == pygame.KEYDOWN:    
            # If up arrow was pressed
            if event.key == pygame.K_UP:
                # It will only jump if its not jumping
                if not pinguino.isJumping:
                    pinguino.isJumping = True
            if event.key == pygame.K_DOWN:
                if pinguino.isJumping:
                    # TODO: 
                    # Make it fall faster
                    print("TODO")
    
    # Está así para ver si en un futuro encuentro una
    # solución más modular, como tal no es necesario
    # postear el event
    if Background.jugadorIsDead:
        pygame.event.post(GameOver)
    
    if showEndGame:
        fondo.gameOver()    
    else:
        fondo.draw()
    # Refresh screen objects
    pygame.display.update()
    


