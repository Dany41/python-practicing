from utils.grid import Grid
from utils.point import Point, Direction


def upload_input(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            # Split the line by comma and convert to integers
            x, y = map(int, line.strip().split(","))
            points.append(Point(y, x))
    return points


def make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q):
    if not grid.is_in(start):
        return
    if start in minimum_path:
        if minimum_path[start] > points:
            minimum_path[start] = points
        else:
            return
    else:
        minimum_path[start] = points
    if start == finish:
        return
    if start.move_in_d(direction) not in obstacles:
        q.append((start.move_in_d(direction), direction, points + 1))
    if start.move_in_d(direction.turn_right()) not in obstacles:
        q.append((start.move_in_d(direction.turn_right()), direction.turn_right(), points + 1))
    if start.move_in_d(direction.turn_left()) not in obstacles:
        q.append((start.move_in_d(direction.turn_left()), direction.turn_left(), points + 1))
    return


def resolve_part1(byte_points, bytes_to_fall = 1024, height = 71, width = 71):

    grid = Grid.create(height, width, '.')

    i = 0
    while i < bytes_to_fall:
        grid.set_at(byte_points[i], '#')
        i += 1

    minimum_path = {}
    finish = Point(height-1, width-1)
    obstacles = grid.find_all('#')
    q = [(Point(0, 0), Direction.RIGHT, 0)]

    while len(q) > 0:
        start, direction, points = q.pop(0)
        make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)

    return minimum_path[finish]


def resolve_part2(byte_points, bytes_to_fall = 1024, height = 71, width = 71):

    grid = Grid.create(height, width, '.')

    i = 0
    while i < bytes_to_fall:
        grid.set_at(byte_points[i], '#')
        i += 1

    obstacles = grid.find_all('#')
    finish = Point(height - 1, width - 1)

    while i < len(byte_points):
        minimum_path = {}
        obstacles.add(byte_points[i])
        grid.set_at(byte_points[i], '#')
        q = [(Point(0, 0), Direction.RIGHT, 0)]

        while len(q) > 0:
            start, direction, points = q.pop(0)
            make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)

        if finish not in minimum_path:
            return byte_points[i]
        i += 1


if __name__ == "__main__":
    example_expectation_part1 = 22
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input, 12, 7, 7)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = Point(1,6)
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input, 12, 7, 7)
    print("Example output is " + str(result_ex_part2.y) + "," + str(result_ex_part2.x))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res.y) + "," + str(part_2_res.x))