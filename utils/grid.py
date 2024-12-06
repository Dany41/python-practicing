def is_grid_valid(grid):
    n = len(grid)
    assert n > 0
    m = len(grid[0])
    assert m > 0
    for row in grid:
        assert len(row) == m


def copy_2dim_array(arrays):
    res = []
    for array in arrays:
        arr_copied = []
        for el in array:
            arr_copied.append(el)
        res.append(arr_copied)
    return res


class Grid:

    def __init__(self, grid):
        is_grid_valid(grid)
        self.grid = copy_2dim_array(grid)
        self.n = len(grid)
        self.m = len(grid[0])

    def find(self, value):
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[0]):
                if self.grid[i][j] == value:
                    return Point(i, j)
                j += 1
            i += 1

    def value_at(self, point):
        return self.grid[point.x][point.y]

    def set_at(self, point, value):
        self.grid[point.x][point.y] = value

    def print(self):
        for x in self.grid:
            print(x)

    def is_in(self, point):
        return self.n > point.x >= 0 and self.m > point.y >= 0


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

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
