from utils.point import Point
from utils.region import Region


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

    @staticmethod
    def create(height, width, val = '.'):
        grid = [[val] * width] * height
        return Grid(grid)

    def find(self, value):
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[0]):
                if self.grid[i][j] == value:
                    return Point(i, j)
                j += 1
            i += 1

    def find_all(self, value):
        found = set()
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[0]):
                if self.grid[i][j] == value:
                    found.add(Point(i, j))
                j += 1
            i += 1
        return found

    def unique_values(self, exception =''):
        unique = set()
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[0]):
                if self.grid[i][j] != exception:
                    unique.add(self.grid[i][j])
                j += 1
            i += 1
        return unique

    def value_at(self, point):
        return self.grid[point.x][point.y]

    def set_at(self, point, value):
        self.grid[point.x][point.y] = value

    def print(self):
        for x in self.grid:
            print(x)

    def is_in(self, point):
        return self.n > point.x >= 0 and self.m > point.y >= 0

    def regions(self, exception = ''):
        def collect_region(p, grid, intermediate):
            value = grid.value_at(p)
            for p_s in p.to_sided_points():
                if grid.is_in(p_s) and p_s not in intermediate and grid.value_at(p_s) == value:
                    intermediate.add(p_s)
                    for p2 in collect_region(p_s, grid, intermediate):
                        intermediate.add(p2)
            return intermediate
        regions = []
        visited = []
        for val in self.unique_values(exception):
            for point in self.find_all(val):
                if point not in visited:
                    region = Region(collect_region(point, self, {point}))
                    regions.append(region)
                    visited += region.points

        return regions
