import math
class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (2*self.width+2*self.height)

    def get_diagonal(self):
        return ((self.width**2+self.height**2)**0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        output = ''
        for lines in range(self.height):
            if output != '':
                output += '\n'
            for stars in range(self.width):
                output += '*'
        return output + '\n'


    def get_amount_inside(self,shape):
        
        if (self.width + self.height) < (shape.width + shape.height):
            return 0
        
        return math.floor((self.width/shape.width)*(self.height/shape.height))

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)

class Square(Rectangle):

    def __init__(self,length):
        super().__init__(length,length)

    def __str__(self):
        return 'Square(side={})'.format(self.width,self.height)

    def set_side(self,length):
        return super().set_width(length),super().set_height(length)
 
    def set_width(self, length):
        return super().set_width(length),super().set_height(length)
    
    def set_height(self, length):
        return super().set_height(length),super().set_width(length)
    
    def get_area(self):
        return super().get_area()

    def get_diagonal(self):
        return super().get_diagonal()