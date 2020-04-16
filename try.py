
# [xPos, yPos, width, height]
rectangle1 = [0,0,50,100]
rectangle2 = [20,40,10,30]

extremoDX1 = rectangle1[0] + rectangle1[2]
extremoSY2 = rectangle1[1] + rectangle1[3]

def choca ():
    if (rectangle1[1] < rectangle2[1]-rectangle2[3]) and (rectangle1[0]+rectangle1[2] > rectangle2[0]):
        return True