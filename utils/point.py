from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def to_string(self):
        return "Point(x=" + str(self.x) + ",y=" + str(self.y) + ")"

    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def move(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __eq__(self, __value):
        return self.x == __value.x and self.y == __value.y

    def __hash__(self):
        return hash((self.x, self.y))


class Direction(Enum):
    NONE = 1,
    UP = 2,
    RIGHT = 3,
    DOWN = 4,
    LEFT = 5

    def turn_right(self):
        return Direction(self.value[0] + 1)


@dataclass
class PointWithDirection(Point):

    direction: Direction