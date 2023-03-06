class Point:  # all class inherit from the object base class in python!!
    def __init__(self, x=0, y=0):  # this method will always be called when a new instance is created!!
        # define 2 attributes for my point class
        self._x = x
        self._y = y

    def __str__(self):
        # this needs to return a string object, used when printing the value of instance of Point
        value = f"({self._x}, {self._y})"
        return value

    def __repr__(self):
        return self.__str__()

    def distance_to_origin(self):
        value = (self._x**2 + self._y**2)**0.5
        if int(value) == value:
            return int(value)
        return value

    def distance_other(self, other):
        value = ((self._x-other._x)**2 + (self._y-other._y)**2)**0.5
        if int(value) == value:
            return int(value)
        return value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value


class ColoredPoint(Point):
    def __init__(self, x=0, y=0, color="black"):  # this method will always be called when a new instance is created!!
        super().__init__(x, y)  # call the __init__ from the parent!!!
        self.color = color

    def __str__(self):
        # this needs to return a string object, used when printing the value of instance of Point
        value = f"({self.x}, {self.y}, {self.color})"
        return value


p = Point(1, 1)
print(f"x={p.get_x()}, y={p.get_y()}")
p.set_y(11)

print(p)
