from collections import deque
import pygame

pygame.init() 

window = pygame.display.set_mode((800,800))
pygame.display.set_caption('Pyguino') 
img = pygame.image.load("resources/cac3.png")

while True : 
    window.fill((255,255,255)) 
    window.blit(img, (100, 33))
    window.blit(img, (400, 300))
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
            # deactivates the pygame library 
            pygame.quit()
            # quit the program. 
            quit()
    pygame.display.update()  
# [xPos, yPos, width, height]
    # rectangle1 = [0,0,50,100]
    # rectangle2 = [50,40,10,30]

    # extremoDX1 = rectangle1[0] + rectangle1[2]
    # extremoSY2 = rectangle1[1] + rectangle1[3]

    # def choca ():
    #     if (rectangle1[1] < rectangle2[1]-rectangle2[3]) and (rectangle1[0]+rectangle1[2] > rectangle2[0]):
    #         return True
    #     else:
    #         return False

    # print(choca())

    # obstaculos = deque() 
    # obstaculos.append(1)
    # obstaculos.append(2)
    # obstaculos.append(3)
    # print(obstaculos.popleft())
    # print(obstaculos[0])