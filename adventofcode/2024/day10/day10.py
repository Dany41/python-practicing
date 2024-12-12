from utils.grid import Grid
from utils.point import Point


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

def get_number_of_hikes(start, grid, accumulator):
    value = int(grid.value_at(start))
    if value == 9:
        return accumulator.add(start)
    moved_up = start.move(up)
    if grid.is_in(moved_up) and int(grid.value_at(moved_up)) - 1 == value:
        get_number_of_hikes(moved_up, grid, accumulator)
    moved_right = start.move(right)
    if grid.is_in(moved_right) and int(grid.value_at(moved_right)) - 1 == value:
        get_number_of_hikes(moved_right, grid, accumulator)
    moved_down = start.move(down)
    if grid.is_in(moved_down) and int(grid.value_at(moved_down)) - 1 == value:
        get_number_of_hikes(moved_down, grid, accumulator)
    moved_left = start.move(left)
    if grid.is_in(moved_left) and int(grid.value_at(moved_left)) - 1 == value:
        get_number_of_hikes(moved_left, grid, accumulator)
    return len(accumulator)


def resolve_part1(lines):
    res = 0

    grid = Grid(lines)

    starts = grid.find_all('0')

    for start in starts:
        res += get_number_of_hikes(start, grid, set())

    return res


def get_number_of_hikes_part2(start, grid):
    value = int(grid.value_at(start))
    if value == 9:
        return 1
    res = 0
    moved_up = start.move(up)
    if grid.is_in(moved_up) and int(grid.value_at(moved_up)) - 1 == value:
        res += get_number_of_hikes_part2(moved_up, grid)
    moved_right = start.move(right)
    if grid.is_in(moved_right) and int(grid.value_at(moved_right)) - 1 == value:
        res += get_number_of_hikes_part2(moved_right, grid)
    moved_down = start.move(down)
    if grid.is_in(moved_down) and int(grid.value_at(moved_down)) - 1 == value:
        res += get_number_of_hikes_part2(moved_down, grid)
    moved_left = start.move(left)
    if grid.is_in(moved_left) and int(grid.value_at(moved_left)) - 1 == value:
        res += get_number_of_hikes_part2(moved_left, grid)
    return res


def resolve_part2(lines):
    res = 0

    grid = Grid(lines)

    starts = grid.find_all('0')

    for start in starts:
        res += get_number_of_hikes_part2(start, grid)

    return res


if __name__ == "__main__":
    example_expectation_part1 = 36
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 81
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))