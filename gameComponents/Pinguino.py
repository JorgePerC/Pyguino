# Clase para manejar los estados del pinguino
import numpy as np
import pygame

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
        self.image = pygame.image.load("resources/lolly.png") 
        
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
    
    def pinguinData(self):
        # [xPos, yPos, width, height]
        return [self.X, self.__jumpLinspace[self.__height], self.width, self.imgH]