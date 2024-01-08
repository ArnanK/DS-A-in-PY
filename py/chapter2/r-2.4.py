from abc import ABCMeta, abstractmethod

class Shapes(metaclass=ABCMeta):
    def getSides(self):
        """Return sides"""
        return self.sides
 
    def getColor(self):
        """Return color"""
        return self.color

    
class Square(Shapes):
    def __init__(self,  color, sides = 4):
        self.color = color


redSquare = Square('red')

print(redSquare.getColor())


   