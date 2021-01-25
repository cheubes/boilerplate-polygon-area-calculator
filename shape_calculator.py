class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)

    def __str__(self):
        return f'Square(side={self.width})'
