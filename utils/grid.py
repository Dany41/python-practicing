def is_grid_valid(grid):
    n = len(grid)
    assert n > 0
    m = len(grid[0])
    assert m > 0
    for row in grid:
        assert len(row) == m


class Grid:

    def __init__(self, grid):
        is_grid_valid(grid)
        self.grid = grid


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "Point(x=" + str(self.x) + ",y=" + str(self.y) + ")"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy