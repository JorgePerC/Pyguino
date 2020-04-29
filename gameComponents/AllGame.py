import pygame
import random
import numpy as np
from collections import deque 

class Ambiente:
    # Voy a hacer una lista con los obstaculos
    # Qeque y deqeque dependiendo de cual se su
    # Posición
    # Necesito los nombres de las imagenes
    

    def __init__(self, window):
        self.window = window
        self.X = window.get_width()
        self.x_Axis = np.linspace(-10, self.X, (10 + self.X + 1), endpoint=True)
        self.obstaculos = deque() 
        self.Y = 350
        self.imgs = ["win.png", "cloud.jpg", "bigSnowball.png" ]
        self.loadedImages = [] # Para que ve se abran una vez, en vez de siempre
        self.loadImages() # Para abrir todos mis archivos
    
    def loadImages(self):
        for x in self.imgs:    
            self.loadedImages.append(pygame.image.load("resources/" + x))

    def move(self):
        for cactus in list(self.obstaculos): # La volvemos lista para evitar el "eque mutated during iteration"
            #Show my cactus at x, y
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

class Colores:
    # define the RGB value 
    def __init__(self):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.veryGreen = (0,255,0)
        self.veryRed = (255,0,0)
        self.veryBlue = (0,0,255)
        self.pink = (255, 153, 255)
        self.orange = (255, 102, 0)
        self.brown = (102, 51, 0)
        self.purple = (102, 0, 204)


class Pinguino:
    #Private variable
    __isJumping = None
    __jumpLinspace = None
    __up_down = None
    __height = None

    def __init__(self, window):
        self.window = window
        self.y_Line = 350
        self.X = 10
        self.__isJumping = False
        self.__up_down = False
        self.__height = 0
        self.__jumpLinspace = np.linspace(0, self.y_Line, self.y_Line + 1, endpoint=True)
        self.image = pygame.image.load("resources/lolly_100.png") 
        
        self.width = self.image.get_width()
        self.imgH = self.image.get_height()
        
    
    def jump(self):
        if self.__isJumping:
            if self.__up_down:
                self.__height +=1
            else:
                self.__height -=1
        # Me indica cuando termina el brinco
        if self.__height == 0:
            # print("Termino brinco")
            # print("------------")
            self.__isJumping = False
            return self.__jumpLinspace[0]
        # Si llega a la altura máxima, empieza a bajar 
        if self.__jumpLinspace[self.__height] == (self.__jumpLinspace[-1]) :
            self.__up_down = False
        # Return la diferencia de pixeles. Aka, altura
        return self.__jumpLinspace[self.__height]
    
    def show(self):
        self.window.blit(self.image, (10, self.y_Line - self.imgH -self.jump()))
    
    @property #Lo ponemos como una propiedad, para que el setter se vea bonito
    def isJumping(self):
        return self.__isJumping
    
    @isJumping.setter #Lo ponemos como un decorator, para que el getter se vea bonito
    def isJumping(self, value : bool):
        self.__isJumping = value   
    #-------------------------------------------------
    @property #Lo ponemos como una propiedad, para que el setter se vea bonito
    def up_down(self):
        return self.__up_down
    
    @up_down.setter #Lo ponemos como un decorator, para que el getter se vea bonito
    def up_down(self, value : bool):
        self.__up_down = value  
    
    def setUp(self, value: bool):
        self.__up_down = value
    
    def pinguinData(self):
        # [xPos, yPos, width, height]
        return [self.X, self.__jumpLinspace[self.__height], self.width, self.imgH]