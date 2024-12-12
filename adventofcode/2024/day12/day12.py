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


def calculate_area(region):
    return len(region)


def calculate_perimeter(region):
    points_to_sides = {}
    for point in region:
        points_to_sides[point] = 4

    for point in region:
        moved_up = point.move(up)
        if moved_up in region:
            points_to_sides[point] -= 1
        moved_right = point.move(right)
        if moved_right in region:
            points_to_sides[point] -= 1
        moved_down = point.move(down)
        if moved_down in region:
            points_to_sides[point] -= 1
        moved_left = point.move(left)
        if moved_left in region:
            points_to_sides[point] -= 1

    res = 0
    for val in points_to_sides.values():
        res += val
    return res


def resolve_part1(lines):
    res = 0

    grid = Grid(lines)

    crop_to_regions = {}

    i = 0
    while i < grid.n:
        j = 0
        while j < grid.m:
            present = False
            crop = grid.grid[i][j]
            crop_point = Point(i, j)
            if crop in crop_to_regions:
                for x in crop_to_regions[crop]:
                    if crop_point in x:
                        present = True
            if not present:
                crop_region = collect_region(crop_point, grid, {crop_point})
                if crop in crop_to_regions:
                    crop_to_regions[crop].append(crop_region)
                else:
                    crop_to_regions[crop] = [crop_region]
            j += 1
        i += 1

    for crop, crop_regions in crop_to_regions.items():
        for region in crop_regions:
            res += calculate_perimeter(region) * calculate_area(region)



    return res


def group_points(point, points, intermediate):
    moved_up = point.move(up)
    if moved_up in points and moved_up not in intermediate:
        intermediate.add(moved_up)
        for p in group_points(moved_up, points, intermediate):
            intermediate.add(p)
    moved_right = point.move(right)
    if moved_right in points and moved_right not in intermediate:
        intermediate.add(moved_right)
        for p in group_points(moved_right, points, intermediate):
            intermediate.add(p)
    moved_down = point.move(down)
    if moved_down in points and moved_down not in intermediate:
        intermediate.add(moved_down)
        for p in group_points(moved_down, points, intermediate):
            intermediate.add(p)
    moved_left = point.move(left)
    if moved_left in points and moved_left not in intermediate:
        intermediate.add(moved_left)
        for p in group_points(moved_left, points, intermediate):
            intermediate.add(p)
    return intermediate


def calculate_perimeter_part_2(region):
    points_to_sides = {}
    for point in region:
        points_to_sides[point] = [up, right, down, left]

    for point in region:
        moved_up = point.move(up)
        if moved_up in region:
            points_to_sides[point].remove(up)
        moved_right = point.move(right)
        if moved_right in region:
            points_to_sides[point].remove(right)
        moved_down = point.move(down)
        if moved_down in region:
            points_to_sides[point].remove(down)
        moved_left = point.move(left)
        if moved_left in region:
            points_to_sides[point].remove(left)

    side_to_point = {up:[], right:[], down:[], left:[]}
    for point, sides in points_to_sides.items():
        for side in sides:
            if side == up or side == down:
                side_to_point[side].append(point)
            else:
                side_to_point[side].append(point)

    res = 0
    for side, points in side_to_point.items():
        visited = []
        for point in points:
            if point not in visited:
                region = group_points(point, points, {point})
                visited += region
                res += 1


    return res

def resolve_part2(lines):
    res = 0

    grid = Grid(lines)

    crops = grid.unique_values()
    crop_to_regions = {}

    i = 0
    while i < grid.n:
        j = 0
        while j < grid.m:
            present = False
            crop = grid.grid[i][j]
            crop_point = Point(i, j)
            if crop in crop_to_regions:
                for x in crop_to_regions[crop]:
                    if crop_point in x:
                        present = True
            if not present:
                crop_region = collect_region(crop_point, grid, {crop_point})
                if crop in crop_to_regions:
                    crop_to_regions[crop].append(crop_region)
                else:
                    crop_to_regions[crop] = [crop_region]
            j += 1
        i += 1

    for crop, crop_regions in crop_to_regions.items():
        for region in crop_regions:
            res += calculate_perimeter_part_2(region) * calculate_area(region)



    return res


if __name__ == "__main__":
    example_expectation_part1 = 1930
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 1206
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))