import math

from utils.grid import Grid
from utils.point import Point, Direction


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line.replace('\n', '')))
    return lines


def make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q):
    if not grid.is_in(start):
        return
    if start in minimum_path:
        if minimum_path[start] >= points:
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


def collect_cheats(grid):
    i = 0
    res = set()
    while i < grid.n:
        j = 0
        while j < grid.m:
            cand = Point(i, j)
            if grid.value_at(cand) == '#':
                if (grid.is_in(cand.up()) and grid.value_at(cand.up()) != '#' and grid.is_in(cand.down()) and grid.value_at(cand.down()) != '#' and
                        grid.is_in(cand.left()) and grid.value_at(cand.left()) == '#' and grid.is_in(cand.right()) and grid.value_at(cand.right()) == '#'):
                    res.add(cand)
                if (grid.is_in(cand.left()) and grid.value_at(cand.left()) != '#' and grid.is_in(cand.right()) and grid.value_at(cand.right()) != '#'
                        and grid.is_in(cand.up()) and grid.value_at(cand.up()) == '#' and grid.is_in(cand.down()) and grid.value_at(cand.down()) == '#'):
                    res.add(cand)
            j += 1
        i += 1
    return res


def resolve_part1(data):

    res = 0
    grid = Grid(data)

    minimum_path = {}
    finish = grid.find('E')
    start = grid.find('S')
    obstacles = grid.find_all('#')
    q = [(start, Direction.LEFT, 0)]

    while len(q) > 0:
        start, direction, points = q.pop(0)
        make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)


    min_path_cost = minimum_path[finish]
    saved_min_path = minimum_path.copy()

    print("Min cost is " + str(min_path_cost))
    take_candidates_to_cheat = collect_cheats(grid)


    for o in take_candidates_to_cheat:
        grid.set_at(o, '.')
        minimum_path = saved_min_path.copy()
        obstacles.remove(o)
        finish = grid.find('E')
        start = grid.find('S')
        q = [(start, Direction.LEFT, 0)]

        while len(q) > 0:
            start, direction, points = q.pop(0)
            make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)
        cost = min_path_cost - minimum_path[finish]
        if cost >= 100:
            res += 1
        obstacles.add(o)
        grid.set_at(o, '#')

    return res


def distance_in_picoseconds(d1, d2):
    return int(math.fabs(d2.x - d1.x) + math.fabs(d2.y - d1.y))


def make_a_move_through_obstacles(start, direction, minimum_path, grid, obstacles, points, finish, q, max_steps):
    if not grid.is_in(start):
        return
    if start in minimum_path:
        if minimum_path[start] > points:
            minimum_path[start] = points
        else:
            return
    else:
        minimum_path[start] = points
    if points > max_steps:
        return
    if start == finish:
        return
    if start.move_in_d(direction) not in obstacles or start.move_in_d(direction) == finish:
        q.append((start.move_in_d(direction), direction, points + 1))
    if start.move_in_d(direction.turn_right()) not in obstacles or start.move_in_d(direction.turn_right()) == finish:
        q.append((start.move_in_d(direction.turn_right()), direction.turn_right(), points + 1))
    if start.move_in_d(direction.turn_left()) not in obstacles or start.move_in_d(direction.turn_left()) == finish:
        q.append((start.move_in_d(direction.turn_left()), direction.turn_left(), points + 1))
    if start.move_in_d(direction.turn_left().turn_left()) not in obstacles or start.move_in_d(direction.turn_left().turn_left()) == finish:
        q.append((start.move_in_d(direction.turn_left().turn_left()), direction.turn_left(), points + 1))
    return


def no_dots_between(d1, d2, grid, obstacles):
    minimum_path = {}
    finish = d2
    start = d1
    max_steps = 20
    q = [(start, Direction.LEFT, 0)]

    while len(q) > 0:
        if finish in minimum_path:
            break
        start, direction, points = q.pop(0)
        make_a_move_through_obstacles(start, direction, minimum_path, grid, obstacles, points, finish, q, max_steps)

    if finish in minimum_path:
        return minimum_path[finish]
    else:
        return -1


def collect_cheats_part2(grid):
    dots = grid.find_all('.')
    res = set()
    for d1 in dots:
        for d2 in dots:
            if d1 != d2:
                dist = distance_in_picoseconds(d1, d2)
                if dist <= 20:
                    dots_count = no_dots_between(d1, d2, grid)
                    if dots_count != -1:
                        res.add((d1, d2, dots_count))
    return res


def make_a_move_with_cheat(start, direction, minimum_path, grid, obstacles, points, finish, q, cheat):
    if not grid.is_in(start):
        return
    if start in minimum_path:
        if minimum_path[start] >= points:
            minimum_path[start] = points
        else:
            return
    else:
        minimum_path[start] = points
    if start == finish:
        return
    if start == cheat[0]:
        q.append((cheat[1], direction, points + cheat[2]))
    if start.move_in_d(direction) not in obstacles:
        q.append((start.move_in_d(direction), direction, points + 1))
    if start.move_in_d(direction.turn_right()) not in obstacles:
        q.append((start.move_in_d(direction.turn_right()), direction.turn_right(), points + 1))
    if start.move_in_d(direction.turn_left()) not in obstacles:
        q.append((start.move_in_d(direction.turn_left()), direction.turn_left(), points + 1))
    return


def resolve_part2(data):
    grid = Grid(data)

    minimum_path = {}
    finish = grid.find('E')
    start = grid.find('S')
    obstacles = grid.find_all('#')
    q = [(start, Direction.LEFT, 0)]

    while len(q) > 0:
        start, direction, points = q.pop(0)
        make_a_move(start, direction, minimum_path, grid, obstacles, points, finish, q)

    min_path_cost = minimum_path[finish]
    saved_min_path = minimum_path.copy()

    # take_candidates_to_cheat = collect_cheats_part2(grid)
    print("Min cost is " + str(min_path_cost))

    dots = grid.find_all('.')
    dots.add(grid.find('S'))
    dots.add(grid.find('E'))
    res = 0
    seen_pairs = set()
    needed = 100
    total = len(dots) * len(dots)
    i = 0
    for d1 in dots:
        for d2 in dots:
            i += 1
            if i % 10000 == 0:
                print("On " + str(i) + "th pait out of " + str(total))
            if d1 != d2:
                dist = distance_in_picoseconds(d1, d2)
                if dist <= 20:
                    poss_gain = saved_min_path[d2] - saved_min_path[d1]
                    if poss_gain - dist >= needed:
                        res += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 0
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = 0
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))