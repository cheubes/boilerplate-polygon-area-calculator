import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50 :
            return 'Too big for picture.'
        picture = ''
        for line in range(0, self.height) :
            for col in range(0, self.width) :
                picture += '*'
            picture += '\n'
        return picture

    def get_amount_inside(self, shape) :
        in_height = math.floor(self.height / shape.height)
        in_width = math.floor(self.width / shape.width)
        return in_height * in_width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f'Square(side={self.width})'
