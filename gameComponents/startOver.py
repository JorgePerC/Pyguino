from gameComponents.Colores import Colores
import pygame


class Background:
    def __init__(self, X: int, Y: int):
        self.__colores = Colores()
        self.__state = False
        self.__y_Line = 350
        self.W = pygame.display.set_mode((X, Y))
        self.__X = X
        self.__Y = Y
        self.__obstacles = []

        pygame.display.set_caption('Pyguino') 

    def draw(self):
        if self.__state:
            # completely fill the surface object
            self.W.fill(self.__colores.daySky) 
            # Draw a rectangle
            pygame.draw.rect(self.W, 
                self.__colores.daySnow, 
                (0, self.__y_Line, self.__X, self.__Y-self.__y_Line))
        else:
            self.W.fill(self.__colores.nightSky) 
            pygame.draw.rect(self.W, 
                self.__colores.nightSnow, 
                (0, self.__y_Line, self.__X, self.__Y-self.__y_Line))
        a = self.addImages()
        print("Done with a")
        self.W.blits( a ) # Calling the method
    
    @property
    def state (self):
        return self.__state
    
    @state.setter
    def state (self, value: bool):
        self.__state = value

    def addImages (self):
        drawings = []
        for obstacle in self.__obstacles:
            drawings.append([obstacle.img, (obstacle.updateXPosition(), obstacle.Y)])
            print("\t Drawings: " + str(obstacle.X) + " " + str(obstacle.Y) )
        # Append a tupple at drawings
        return drawings
    
    def addObstacle(self, obs): # How to make a class, a type?
        print("added obstacle")
        self.__obstacles.append(obs)

class GameObstacle:
    dayTime = False # Class variable, this is kinda static
                # True if day, false if night
    dt = 0 # So all objects have the same dt
    def __init__(self, obstacle : str):
        self.__dayImg = pygame.image.load("resources/Day/day" + obstacle + ".png")
        self.__nightImg = pygame.image.load("resources/Night/night" + obstacle + ".png")
        self.__Y = 19
        self.__X = 19
        self.__speed = 1

    def img (self):
        return self.__dayImg if GameObstacle.dayTime else self.__nightImg

    def updateXPosition(self):
        self.__X += self.__speed * GameObstacle.dt
        return self.__X

    @property
    def X (self):
        return self.__X

    @X.setter
    def X (self, value : int):
        self.__X = value

    @property
    def Y (self):
        return self.__Y
    @Y.setter
    def Y (self, value :int):
        self.__Y = value

class Pinguin:
    def __init__(self):
        self.__character = pygame.image.load("resorces/lolly.png")
        self.__heiht = 19

    def Img(self):
        return self.__character