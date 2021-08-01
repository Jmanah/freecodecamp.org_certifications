class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = (2 * self.width) + (2 * self.height)
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        print(f"area = {self.area}")
        return self.area

    def get_perimeter(self):
        print(f"area = {self.perimeter}")
        return self.perimeter
    
    def get_diagonal(self):
        print(f"area = {self.diagonal}")
        return self.diagonal
    
    def get_picture(self):
        out = []
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        for h in range(self.height, 0, -1):
            out.append ("".join(["*" for n in range(0, self.width, 1)]))
            out.append ("\n")
        print ("".join(out))
        return "".join(out)
    
    def get_amount_inside(self, shape):
        width = self.width // shape.width
        height = self.height // shape.height
        out = width * height
        return out

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side
        self.area = self.width * self.height
        self.perimeter = (2 * self.width) + (2 * self.height)
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5

    def __str__(self):
        return f"{type(self).__name__}(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_width(self, width):
        self.width = width
        self.side = width

    def set_height(self, height):
        self.width = height
        self.side = height

    def get_picture(self):
        out = []
        if self.side > 50:
            return "Too big for picture."
        for h in range(self.side, 0, -1):
            out.append ("".join(["*" for n in range(0, self.side, 1)]))
            out.append ("\n")
        print ("".join(out))
        return "".join(out)