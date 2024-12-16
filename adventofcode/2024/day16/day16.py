from copy import copy

from utils.grid import Grid
from utils.point import Point, Direction


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line.replace('\n', '')))
    return lines


up = Point(-1, 0)
right = Point(0, 1)
down = Point(1, 0)
left = Point(0, -1)


def is_passing(start, direction, obstacles):
    return start.move_in_d(direction.turn_left()) in obstacles and start.move_in_d(direction.turn_right()) in obstacles and start.move_in_d(direction) not in obstacles


def find_next_intersection(start, direction, obstacles, grid):
    curr = start
    points = 0
    while is_passing(curr, direction, obstacles):
        curr = curr.move_in_d(direction)
        points += 1
    return curr, points



def make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q):
    if start in minimum_path:
        if minimum_path[start] > points:
            minimum_path[start] = points
        else:
            return
    else:
        minimum_path[start] = points
    if start == finish:
        return
    if is_passing(start, direction, obstacles):
        #next_p, dp = find_next_intersection(start, direction, obstacles, grid)
        q.append((start.move_in_d(direction), direction, points + 1))
    else:
        if start.move_in_d(direction) not in obstacles:
            q.append((start.move_in_d(direction), direction, points + 1))
        if start.move_in_d(direction.turn_right()) not in obstacles:
            q.append((start.move_in_d(direction.turn_right()), direction.turn_right(), points + 1001))
        if start.move_in_d(direction.turn_left()) not in obstacles:
            q.append((start.move_in_d(direction.turn_left()), direction.turn_left(), points + 1001))
        return


def resolve_part1(data):

    grid = Grid(data)
    finish = grid.find('E')
    minimum_path = {}
    obstacles = grid.find_all('#')

    q = [(grid.find('S'), Direction.RIGHT, 0)]

    while len(q) > 0:
        start, direction, points = q.pop(0)
        make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)



    return minimum_path[finish]


def find_shortest_path(start, direction, minimum_path_value, path, obstacles, points, finish, q, short_pass):
    if points > minimum_path_value or start in path:
        return
    path.add(start)
    if start == finish and points == minimum_path_value:
        for point in path:
            short_pass.add(point)
        return
    if is_passing(start, direction, obstacles):
        q.append((start.move_in_d(direction), direction, points + 1, path.copy()))
    else:
        if start.move_in_d(direction) not in obstacles:
            q.append((start.move_in_d(direction), direction, points + 1, path.copy()))
        if start.move_in_d(direction.turn_right()) not in obstacles:
            q.append((start.move_in_d(direction.turn_right()), direction.turn_right(), points + 1001, path.copy()))
        if start.move_in_d(direction.turn_left()) not in obstacles:
            q.append((start.move_in_d(direction.turn_left()), direction.turn_left(), points + 1001, path.copy()))
        return


def resolve_part2(data):
    grid = Grid(data)
    finish = grid.find('E')
    minimum_path = {}
    obstacles = grid.find_all('#')

    q = [(grid.find('S'), Direction.RIGHT, 0)]

    while len(q) > 0:
        start, direction, points = q.pop(0)
        make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)

    start = grid.find('S')
    q = [(start, Direction.RIGHT, 0, set())]
    short_pass = set()
    minimum_path_value = minimum_path[finish]
    while len(q) > 0:
        start, direction, points, path = q.pop(0)
        if not minimum_path[start] + 1000 < points:
            find_shortest_path(start, direction, minimum_path_value, path, obstacles, points, finish, q, short_pass)

    return len(short_pass)


if __name__ == "__main__":
    example_expectation_part1 = 7036
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case #1 has passed for the part 1")
    example_expectation_part1 = 11048
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case #2 has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 45
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    example_expectation_part2 = 64
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))