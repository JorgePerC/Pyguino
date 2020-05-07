from gameComponents.Colores import Colores
import pygame
import random
from collections import deque

# https://stackoverflow.com/questions/35617246/setting-a-fixed-fps-in-pygame-python-3

class Background:

    jugadorIsDead = False

    def __init__(self, X: int, Y: int, pin, score):
        self.__colores = Colores()
        self.__state = False
        self.__y_Line = 350
        self.W = pygame.display.set_mode((X, Y))
        self.__X = X
        self.__Y = Y
        self.__obstacles = deque()

        self.__moon = pygame.image.load("resources/Night/nightMoon.png")
        self.__gameOver = pygame.image.load("resources/game-over.png")

        self.__pinguin = pin
        self.__score = score

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
            # https://stackoverflow.com/questions/35304498/what-are-the-pygame-surface-get-rect-key-arguments
            if a[0][0].get_rect(topleft = a[0][1]).colliderect(a[-1][0].get_rect( topleft =  a[-1][1])):
                # Choca y termina el juego
                Background.jugadorIsDead = True
            self.W.blits( a ) # Calling the method
                    # Draw Score
            self.W.blit(self.__score.getScore(), (560, 20))
    
    @property
    def state (self):
        return self.__state
    
    @state.setter
    def state (self, value: bool):
        self.__state = value

    def addImages (self):
        drawings = []
        for obstacle in list(self.__obstacles):
            xpos = obstacle.updateXPosition()
            if xpos <= -(obstacle.width):
                self.__obstacles.popleft()
                # Remove obstacle
            else:
                drawings.append((obstacle.img(), (xpos, obstacle.Y)))
                # Append a tupple at drawings
        # Draw moon only when is night
        if not self.__state:
            drawings.append( (self.__moon, (500, 20)) )
        # Draw penguin
        drawings.append( (self.__pinguin.img, 
            (self.__pinguin.X, 
            self.__pinguin.Y - self.__pinguin.height - self.__pinguin.jump())) )
        return drawings
    
    def addObstacle(self, obs): # How to make a class, a type?
        self.__obstacles.append(obs)

    def gameOver(self):
        self.W.fill(self.__colores.water)
        self.W.blit(self.__score.getScore(), (325, 150))
        self.W.blit(self.__gameOver, (300, 50))



class GameObstacle:
    dayTime = False # Class variable, this is kinda static
                # True if day, false if night
    dt = 0 # So all objects have the same dt
 
    # You can't overload constructors in Python, we need to make the first one handle all cases
    def __init__(self, obstacle : str = None):
        if obstacle is None:
            obstacles = [
            "Barrel",
            "Esno",
            "Fin",
            "Hole",
            "Huntx",
            "Mt",
            "Plastic"
            ]
            
            rad = random.randint(0,len(obstacles)-1)
            obstacle = obstacles[rad]

            # Desfazamiento 
            if obstacle == "Barrel":
                des = 23
            elif obstacle == "Fin":
                des = 24
            else:
                des = 0
        self.__dayImg = pygame.image.load("resources/Day/day" + obstacle + ".png")
        self.__nightImg = pygame.image.load("resources/Night/night" + obstacle + ".png")
        
        self.__speed = 30
        
        self.__width = self.__dayImg.get_width()
        self.__height = self.__dayImg.get_height()

        self.__Y = 350 - self.__height + des
        self.__X = 700

    def img (self):
        return self.__dayImg if GameObstacle.dayTime else self.__nightImg

    def updateXPosition(self):
        self.__X -= self.__speed * GameObstacle.dt*0.01
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

    @property
    def width (self):
        return self.__width

class SingleImage:

    dt = 0

    def __init__(self, direction: str):
        self.__img = pygame.image.load(direction)
        self.__Y = 350
        self.__X = 10

        self.__width = self.__img.get_width()
        self.__height = self.__img.get_height()
    
    @property
    def X (self):
        return self.__X
    
    @X.setter
    def X (self, value):
        self.__X = value
    
    @property
    def Y (self):
        return self.__Y
    
    @Y.setter
    def Y (self, value):
        self.__Y = value

    @property
    def img (self):
        return self.__img
    
    @img.setter
    def img (self, value):
        self.__img = value

    @property
    def height (self):
        return self.__height
    @height.setter
    def height (self, value):
        self.__height = value

class Pinguin(SingleImage):
    def __init__(self):
        SingleImage.__init__(self,"resources/lolly.png")
        self.__isJumping = False
        self.__isGoingUp = False
        self.__h = 0
        self.__initialV = 70
        self.jumpCount = 0

    def jump(self):
        if self.__isJumping:
            self.jumpCount += SingleImage.dt*0.01
            self.__h = (self.__initialV * self.jumpCount) - (5*self.jumpCount**2)
        # Me indica cuando termina el brinco
        if self.__h <= 0:
            # print("Termino brinco")
            # print("------------")
            self.__isJumping = False
            self.jumpCount = 0
            return 0
        return self.__h

    @property #Lo ponemos como una propiedad, para que el setter se vea bonito
    def isJumping(self):
        return self.__isJumping
    
    @isJumping.setter #Lo ponemos como un decorator, para que el getter se vea bonito
    def isJumping(self, value : bool):
        self.jumpCount = 0
        self.__isJumping = value   
    #-------------------------------------------------
    @property #Lo ponemos como una propiedad, para que el setter se vea bonito
    def isGoingUp(self):
        return self.__isGoingUp
    
    @isGoingUp.setter #Lo ponemos como un decorator, para que el getter se vea bonito
    def isGoingUp(self, value : bool):
        self.__isGoingUp = value  

class Score:

    dt = 0

    def __init__(self):
        self.fontObj = pygame.font.SysFont("swiss721", 20)
        self.__count = 0
        self.__active = True

    def increment(self):
        if self.__active:
            self.__count += round(Score.dt*0.1 )            
    
    def getScore(self):
        self.increment()
        score = self.fontObj.render(str(int(self.__count*0.4)), True, (0,0,0))
        return score

    @property
    def active (self):
        return self.__active
    
    @active.setter
    def active (self, value: bool):
        self.__active = value

# TODO: 
# It would be nice if in a future we implement inheritance from the surface object.
# A lot of class attributes would have been avoided.
# For the moment, I'm satisfied with the result