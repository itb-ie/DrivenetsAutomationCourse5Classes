class Point:
    def __init__(self, x=0, y=0):  # this method will always be called when a new instance is created!!
        self._x = x
        self._y = y

    def __str__(self):
        value = f"({self.x}, {self.y})"
        return value

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __getattr__(self, item):
        if item == "x":
            return self._x
        elif item == "y":
            return self._y
        elif item == "color":
            return "this is a colorless point"
        elif item == "shape":
            # for pycharm debug
            pass
        else:
            return "sorry, unsupported attribute"

    def __setattr__(self, item, value):
        if item in ("_x", "_y"):
            object.__setattr__(self, item, value)
        elif item == "x":
            self._x = value
        elif item == "y":
            self._y = value
        elif item == "color":
            print("this is a colorless point")
        else:
            raise ValueError("Don't try to set anything but x or y")


p = Point(1, 2)
p.x = 3
p.y = 4
p.color = "blue"
p.name = "James"
print(p)
