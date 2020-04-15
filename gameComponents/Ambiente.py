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
    

    def __init__(self, window, X_window):
        self.window = window
        self.X = X_window
        self.x_Axis = np.linspace(-10, self.X, (10 + self.X + 1), endpoint=True)
        self.obstaculos = deque() 

        self.imgs = ["cac1.png", "cac2.png", "img2.png"]
    
    # def show(self):    
    #     self.window.blit(self.montana, (0, 300)) 

    def move(self):
        for cactus in list(self.obstaculos): # La volvemos lista para evitar el "eque mutated during iteration"
            self.window.blit(cactus[0], (self.x_Axis[cactus[1]], 0)) 
            #If my individual cactus has reach the border
            if cactus[1] == self.x_Axis[0]:
                print("Removed image at pos " + str(cactus[1]))
                self.obstaculos.popleft()
            else:
                cactus[1] -= 1

    #Return a random image
    def selectObject(self):
        return pygame.image.load("resources/" + self.imgs[random.randint(0,len(self.imgs)-1)]) 
    
    def addCactus(self):
        print("Aded image")
        self.obstaculos.append([self.selectObject(), self.X])