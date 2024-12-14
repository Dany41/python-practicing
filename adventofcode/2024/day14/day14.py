import math

from utils.grid import Grid
from utils.point import Point


def upload_input(file_path):
    point_pairs = []

    with open(file_path, 'r') as file:
        for line in file:
            # Extracting p and v values
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # Skip invalid lines

            # Parsing the start point (p=...)
            p_coords = parts[0][2:].split(",")
            px, py = map(int, p_coords)

            # Parsing the velocity (v=...)
            v_coords = parts[1][2:].split(",")
            vx, vy = map(int, v_coords)


            # Adding the parsed pair
            point_pairs.append({"point": Point(px, py), "v": Point(vx, vy)})

    return point_pairs


def resolve_part1(data, height = 103, width = 101):

    res = 1

    seconds = 100

    grid = Grid.create(height, width)

    quadrants = {1:0,2:0,3:0,4:0}
    x_axis = math.floor(width / 2)
    y_axis = math.floor(height / 2)

    for pointWithVelocity in data:
        point = pointWithVelocity["point"]
        velocity = pointWithVelocity["v"]
        final_x = (point.x + velocity.x * seconds) % width
        final_y = (point.y + velocity.y * seconds) % height
        grid.set_at(Point(final_y, final_x), 'P')
        if final_x == x_axis:
            continue
        if final_y == y_axis:
            continue
        if final_x < x_axis and final_y > y_axis:
            quadrants[1] += 1
        if final_x < x_axis and final_y < y_axis:
            quadrants[2] += 1
        if final_x > x_axis and final_y < y_axis:
            quadrants[3] += 1
        if final_x > x_axis and final_y > y_axis:
            quadrants[4] += 1

    grid.print()
    for q_v in quadrants.values():
        if q_v != 0:
            res *= q_v

    return res


up = Point(-1, 0)
right = Point(0, 1)
down = Point(1, 0)
left = Point(0, -1)


def collect_region(crop_point, grid, intermediate):
    value = grid.value_at(crop_point)
    moved_up = crop_point.move(up)
    if grid.is_in(moved_up) and moved_up not in intermediate and grid.value_at(moved_up) == value:
        intermediate.add(moved_up)
        for point in collect_region(moved_up, grid, intermediate):
            intermediate.add(point)
    moved_right = crop_point.move(right)
    if grid.is_in(moved_right) and moved_right not in intermediate and grid.value_at(moved_right) == value:
        intermediate.add(moved_right)
        for point in collect_region(moved_right, grid, intermediate):
            intermediate.add(point)
    moved_down = crop_point.move(down)
    if grid.is_in(moved_down) and moved_down not in intermediate and grid.value_at(moved_down) == value:
        intermediate.add(moved_down)
        for point in collect_region(moved_down, grid, intermediate):
            intermediate.add(point)
    moved_left = crop_point.move(left)
    if grid.is_in(moved_left) and moved_left not in intermediate and grid.value_at(moved_left) == value:
        intermediate.add(moved_left)
        for point in collect_region(moved_left, grid, intermediate):
            intermediate.add(point)
    return intermediate


def grid_has_tree(grid):
    for p in grid.find_all('#'):
        region = collect_region(p, grid, {p})
        reg_len = len(region)

        if reg_len > 30:
            return True


def resolve_part2(data, height = 103, width = 101):

    grid = Grid.create(height, width)

    i = 1
    while True:
        seconds = i
        for pointWithVelocity in data:
            point = pointWithVelocity["point"]
            velocity = pointWithVelocity["v"]

            prev_x = (point.x + velocity.x * (seconds-1)) % width
            prev_y = (point.y + velocity.y * (seconds-1)) % height

            grid.set_at(Point(prev_y, prev_x), '.')

            final_x = (point.x + velocity.x * seconds) % width
            final_y = (point.y + velocity.y * seconds) % height
            grid.set_at(Point(final_y, final_x), '#')
        grid.print()
        print("seconds " + str(i))
        if grid_has_tree(grid):
            return seconds
        i += 1


if __name__ == "__main__":
    example_expectation_part1 = 12
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input, 7, 11)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))


    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))