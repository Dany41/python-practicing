from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NONE = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
    LEFT = 5

    def turn_right(self):
        if self is Direction.UP:
            return Direction.RIGHT
        if self is Direction.RIGHT:
            return Direction.DOWN
        if self is Direction.DOWN:
            return Direction.LEFT
        if self is Direction.LEFT:
            return Direction.UP

    def turn_left(self):
        if self is Direction.UP:
            return Direction.LEFT
        if self is Direction.LEFT:
            return Direction.DOWN
        if self is Direction.DOWN:
            return Direction.RIGHT
        if self is Direction.RIGHT:
            return Direction.UP


@dataclass
class Point:
    x: int
    y: int

    def to_string(self):
        return "Point(x=" + str(self.x) + ",y=" + str(self.y) + ")"

    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def move_in_d(self, direction: Direction):
        if direction is Direction.UP:
            return self.up()
        if direction is Direction.RIGHT:
            return self.right()
        if direction is Direction.DOWN:
            return self.down()
        if direction is Direction.LEFT:
            return self.left()

    def move(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __eq__(self, __value):
        return self.x == __value.x and self.y == __value.y

    def __hash__(self):
        return hash((self.x, self.y))

    def up(self):
        return Point(self.x - 1, self.y)

    def right(self):
        return Point(self.x, self.y + 1)

    def down(self):
        return Point(self.x + 1, self.y)

    def left(self):
        return Point(self.x, self.y - 1)

    def to_sided_points(self):
        return [self.up(), self.right(), self.down(), self.left()]


@dataclass
class PointWithDirection(Point):

    direction: Direction