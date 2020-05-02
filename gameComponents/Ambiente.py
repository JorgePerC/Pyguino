# Así se van a generar los obstaculos
import pygame
import random
import numpy as np
from collections import deque 
# https://www.geeksforgeeks.org/queue-in-python/

class Ambiente:
    # Voy a hacer una lista con los obstaculos
    # Qeque y deqeque dependiendo de cual se su
    # Posición
    # Necesito los nombres de las imagenes
    

    def __init__(self, window):
        self.window = window
        self.X = window.get_width()
        self.x_Axis = np.linspace(-40, self.X, (40 + self.X + 1), endpoint=True)
        self.obstaculos = deque() 
        self.Y = 350
        self.imgs = ["bigSnowball.png", "cloud.png", "win.png" ]
        self.loadedImages = [] # Para que ve se abran una vez, en vez de siempre
        self.loadImages() # Para abrir todos mis archivos
    
    def loadImages(self):
        for x in self.imgs:    
            self.loadedImages.append(pygame.image.load("resources/" + x))

    def move(self):
        for cactus in list(self.obstaculos): # La volvemos lista para evitar el "eque mutated during iteration"
            #Show my cactus at x, y
            #self.window.blit(self.loadedImages[cactus[0]], (self.x_Axis[cactus[1]], self.Y-cactus[3])) 
            self.window.blit(self.loadedImages[cactus[0]], (self.x_Axis[cactus[1]], self.Y-cactus[3])) 
            #If my individual cactus has reach the border
            if cactus[1] == self.x_Axis[0]:
                print("Removed image at pos " + str(cactus[1]))
                self.obstaculos.popleft()
            else:
                cactus[1] -= 1
    
    def addCactus(self):
        print("Aded image")
        #read the image
        selected = random.randint(0,len(self.imgs)-1)
        #List [image, position, width, height]
        self.obstaculos.append([selected, self.X, 
                self.loadedImages[selected].get_width(), 
                self.loadedImages[selected].get_height()])

    def incomingObstacleData(self):
        try:
            halfData = self.obstaculos[0]
        except IndexError as e:
            # Como da error si no hay obstaculos,
            # Agarro el cath y le doy unos valores random
            #print("No hay obstaculos")
            return[150,self.Y, 100, 100]
        # [xPos, yPos, width, height]
        return [self.x_Axis[halfData[1]], self.Y, halfData[2], halfData[3]]
    
# When we use a parenthesis in a class, we use inheritance
# class GameObstacle(pygame.surface):
#     def __init__(self, kind: str, xPos :int = 0 , yPos: int = 0):
#         pygame.Surface.__init__(self, 0,0 )
#         self.dayImg = pygame.image.load("resources/Day/day" + kind)
#         self.nightImg = pygame.image.load("resources/Night/night" + kind)
#         self.__dayTime = True
#         self.xPos = 0
#         self.yPos = 0


    