from abc import abstractmethod, ABC


class AbstractPoint(ABC):
    @abstractmethod
    def distance_to_origin(self):
        pass

    @abstractmethod
    def distance_to_other(self, other):
        pass


class Point2D(AbstractPoint):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to_origin(self):
        return 0

    def distance_to_other(self, other):
        return 0

# class Point3D(AbstractPoint):

p = Point2D(2, 3)
print(p)
# p.distance_to_origin()

