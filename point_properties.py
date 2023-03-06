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
        value = (self._x ** 2 + self._y ** 2) ** 0.5
        if int(value) == value:
            return int(value)
        return value

    def distance_other(self, other):
        value = ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5
        if int(value) == value:
            return int(value)
        return value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        print("sorry, this is a constant point. Can not change it after creation")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


p = Point(1, 1)
print(f"x={p.x}, y={p.y}")

p.y = 11

print(p)
