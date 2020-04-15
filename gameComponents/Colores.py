# Clase para manejar los colores en el juego

class Colores:
    # define the RGB value 
    def __init__(self):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.colors = {
            "white": (255,255,255)
        }
        pass
    def getColor(self, color : str):
        return self.colors.get(color)