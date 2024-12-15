from utils.point import Point


def validate(points: list[Point]):
    assert len(points) > 0
    start = points[0]
    visited = set()
    def move_around(point):
        visited.add(point)
        for s_p in point.to_sided_points():
            if s_p in points and s_p not in visited:
                visited.add(s_p)
                move_around(s_p)

    move_around(start)
    assert set(points) == visited




class Region:

    def __init__(self, points):
        validate(list(points))
        self.points = points

    def __len__(self):
        return len(self.points)