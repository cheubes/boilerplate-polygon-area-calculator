class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square(Rectangle):

    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)
