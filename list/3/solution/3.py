import math

class Figure:
    """
    Base class
    """

    # Figure init
    def __init__(self, sides, angles):
        self.name = "figure"
        self.sides = sides
        self.angles = angles

    # Calculate figure's diagonal
    def diagonal(self):
        return "unknown"

    # Calculate figure's perimeter
    def perimeter(self):
        return sum(self.sides)

class Diamond(Figure):
    """
    Derived class
    """

    # Diamond init. Overwrites Figure init
    def __init__(self, side, angle):
        sides = [side, side, side, side]
        angles = [angle, math.pi - angle, angle, math.pi - angle]
        super().__init__(sides, angles)
        self.name = "diamond"

    # Calculate diamond's diagonal. Overwrites Figure diagonal
    def diagonal(self):
        return 2 * self.sides[0] * math.cos(self.angles[0] / 2)

class Square(Diamond):
    """
    Subderived class
    """

    # Square init. Overwrites Diamond init
    def __init__(self, side):
        angle = math.pi / 2
        super().__init__(side, angle)
        self.name = "square" 

octagon_sides = [2 for i in range(8)]
octagon_angles = [3 * math.pi / 4 for i in range(8)]

octagon = Figure(octagon_sides, octagon_angles)
diamond = Diamond(2, math.pi / 4)
square = Square(2)

figures = [octagon, diamond, square]
for figure in figures:
    print(f"{figure.name}'s diagonal is {figure.diagonal()}")
    print(f"{figure.name}'s perimeter is {figure.perimeter()}\n")





class Container:
    def __init__(self, object):
        self.object = object

    def length(self):
        length = 0
        for i in self.object:
            length = length + 1
        return length

str = Container("string")
vec = Container(["this", "is", "a", "vec"])
dict = Container({"this": "is", "a": "dict"})

print(str.length())
print(vec.length())
print(dict.length())
