# Clase para manejar los estados del pinguino
import numpy as np

class Pinguino:
    #Private variable
    __isJumping = None
    __jumpLinspace = None
    __up_down = None
    __height = None

    def __init__(self):
        y_Line = 350
        self.__isJumping = False
        self.__up_down = False
        self.__height = 0
        self.__jumpLinspace = np.linspace(0, y_Line, endpoint=True)
        pass

    @property #Lo ponemos como una propiedad, para que el setter se vea bonito
    def isJumping(self):
        return self.__isJumping
    
    @isJumping.setter #Lo ponemos como un decorator, para que el getter se vea bonito
    def isJumping(self, value : bool):
        self.__isJumping = value    

    def jump(self):
        if self.__isJumping:
            if self.__up_down:
                self.__height +=1
            else:
                self.__height +=1
        