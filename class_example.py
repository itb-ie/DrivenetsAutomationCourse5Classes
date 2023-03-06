class Point:  # all class inherit from the object base class in python!!
    def __init__(self, x=0, y=0):  # this method will always be called when a new instance is created!!
        # define 2 attributes for my point class
        self.x = x
        self.y = y

    def __str__(self):
        # this needs to return a string object, used when printing the value of instance of Point
        value = f"({self.x}, {self.y})"
        return value

    def __repr__(self):
        return self.__str__()

    def distance_to_origin(self):
        value = (self.x**2 + self.y**2)**0.5
        if int(value) == value:
            return int(value)
        return value

    def distance_other(self, other):
        value = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if int(value) == value:
            return int(value)
        return value


class ColoredPoint(Point):
    def __init__(self, x=0, y=0, color="black"):  # this method will always be called when a new instance is created!!
        super().__init__(x, y)  # call the __init__ from the parent!!!
        self.color = color

    def __str__(self):
        # this needs to return a string object, used when printing the value of instance of Point
        value = f"({self.x}, {self.y}, {self.color})"
        return value


p = Point(1, 2)
p2 = Point(y=1, x=2)
print(p, p2)
p3 = Point()
p4 = Point(x=3, y=4)
p5 = Point(3, 10)
print(p4)
print(f"Distance to origin for {p4} = {p4.distance_to_origin()}")
print(p4.distance_other(p5))
color_p = ColoredPoint(1, 2, "blue")
color_p2 = ColoredPoint(y=1, x=2, color="yellow")
print(color_p, color_p2)
print(color_p.distance_other(color_p2))
print([color_p, color_p2])

p = Point(1, 1)
p.x = 7
print(p)
