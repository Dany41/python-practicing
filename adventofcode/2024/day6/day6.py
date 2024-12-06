from utils.grid import Point, Grid


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line.replace('\n', '')))
    return lines


def get_seen_places(grid):
    up = Point(-1, 0)
    right = Point(0, 1)
    down = Point(1, 0)
    left = Point(0, -1)

    initial_point = grid.find('^')
    curr_point = initial_point
    current_direction = up

    seen_place_and_direction = set()
    next_point = curr_point
    i = 0

    while not tuple([next_point, current_direction]) in seen_place_and_direction and grid.is_in(next_point):
        next_point = curr_point
        while grid.is_in(next_point) and grid.value_at(next_point) != '#':
            seen_place_and_direction.add(tuple([next_point, current_direction]))
            next_point = next_point.move(current_direction)
            i += 1

        if grid.is_in(next_point) and grid.value_at(next_point) == '#':
            if current_direction == up:
                next_point = next_point.move(down)
                current_direction = right
            elif current_direction == right:
                next_point = next_point.move(left)
                current_direction = down
            elif current_direction == down:
                next_point = next_point.move(up)
                current_direction = left
            elif current_direction == left:
                next_point = next_point.move(right)
                current_direction = up
            curr_point = next_point

    return set(map(lambda x: x[0], seen_place_and_direction))


def is_loop(grid):
    up = Point(-1, 0)
    right = Point(0, 1)
    down = Point(1, 0)
    left = Point(0, -1)

    initial_point = grid.find('^')
    curr_point = initial_point
    current_direction = up

    seen_place_and_direction = set()
    next_point = curr_point
    i = 0

    while not tuple([next_point, current_direction]) in seen_place_and_direction and grid.is_in(next_point):
        next_point = curr_point
        while grid.is_in(next_point) and grid.value_at(next_point) != '#':
            seen_place_and_direction.add(tuple([next_point, current_direction]))
            next_point = next_point.move(current_direction)
            i += 1

        if not grid.is_in(next_point):
            return False

        if grid.is_in(next_point) and grid.value_at(next_point) == '#':
            if current_direction == up:
                next_point = next_point.move(down)
                current_direction = right
            elif current_direction == right:
                next_point = next_point.move(left)
                current_direction = down
            elif current_direction == down:
                next_point = next_point.move(up)
                current_direction = left
            elif current_direction == left:
                next_point = next_point.move(right)
                current_direction = up
            curr_point = next_point

    return True


def resolve_part1(lines):
    grid = Grid(lines)
    seen_places = get_seen_places(grid)

    return len(seen_places)


def resolve_part2(lines):
    grid = Grid(lines)
    initial_point = grid.find('^')

    seen_places = get_seen_places(grid)


    res = 0

    for seen_point in seen_places:
        if seen_point != initial_point:
            grid = Grid(lines)
            grid.set_at(seen_point, '#')
            if is_loop(grid):
                res += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 41
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 6
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))