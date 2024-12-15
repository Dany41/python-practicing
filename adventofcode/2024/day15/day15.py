from utils.grid import Grid
from utils.point import Point


def upload_input(file_path):
    lines = []
    moves = []
    map_is_ended = False
    with open(file_path, "r") as file:
        for line in file:
            if line == "\n":
                map_is_ended = True
                continue
            if not map_is_ended:
                lines.append(list(line.replace('\n', '')))
            if map_is_ended:
                moves += list(line.replace('\n', ''))
    return [lines, moves]


up = Point(-1, 0)
right = Point(0, 1)
down = Point(1, 0)
left = Point(0, -1)


def move_a_box(box, m, obstacles, boxes, grid):
    moved_box = box.move(m)
    moved = None
    if moved_box in obstacles:
        moved = False
    if moved_box in boxes:
        moved = move_a_box(moved_box, m, obstacles, boxes, grid)
    if moved_box not in obstacles and moved_box not in boxes:
        moved = True
    if moved:
        grid.set_at(box, '.')
        boxes.remove(box)
        boxes.add(moved_box)
        grid.set_at(moved_box, 'O')
    return moved



def make_a_move(start, m, obstacles, boxes, grid):
    moved = start.move(m)
    if moved not in obstacles and moved not in boxes:
        return moved
    if moved in obstacles:
        return start
    if moved in boxes:
        box_moved = move_a_box(moved, m, obstacles, boxes, grid)
        if box_moved:
            return moved
        else:
            return start


def resolve_part1(data):

    res = 0
    input_map = data[0]
    moves = data[1]

    grid = Grid(input_map)

    start = grid.find('@')
    obstacles = grid.find_all('#')
    boxes = grid.find_all('O')

    m = None

    for move in moves:
        if move == '^':
            m = up
        if move == '>':
            m = right
        if move == '<':
            m = left
        if move == 'v':
            m = down
        grid.set_at(start, '.')
        start = make_a_move(start, m, obstacles, boxes, grid)
        grid.set_at(start, '@')


    for box in boxes:
        res += 100 * box.x + box.y



    return res


def is_enlarged_box_movable(box, m, obstacles, boxes, grid):
    if grid.value_at(box) == '.':
        return True
    if grid.value_at(box) == '#':
        return False
    moved_box = box.move(m)
    moved_box_val = grid.value_at(box)
    box_second_part = None
    if m == up or m == down:
        if moved_box_val == '[':
            box_second_part = box.right()
        if moved_box_val == ']':
            box_second_part = box.left()
    else:
        box_second_part = moved_box
    next_box_part = box_second_part.move(m)
    moved = None
    if next_box_part in obstacles or moved_box in obstacles:
        moved = False
    if (m == right or m == left) and next_box_part in boxes:
        moved = move_an_enlarged_box(next_box_part, m, obstacles, boxes, grid)
    if (m == down or m == up) and (next_box_part in boxes or moved_box in boxes):
        moved = is_enlarged_box_movable(moved_box, m, obstacles, boxes, grid) and is_enlarged_box_movable(next_box_part, m, obstacles, boxes, grid)
    if next_box_part not in obstacles and next_box_part not in boxes and moved_box not in obstacles and (
            moved_box not in boxes or moved_box == box_second_part):
        moved = True
    return moved

def move_an_enlarged_box(box, m, obstacles, boxes, grid):
    if grid.value_at(box) == '.':
        return True
    moved_box = box.move(m)
    moved_box_val = grid.value_at(box)
    box_second_part = None
    if m == up or m == down:
        if moved_box_val == '[':
            box_second_part = box.right()
        if moved_box_val == ']':
            box_second_part = box.left()
    else:
        box_second_part = moved_box
    next_box_part = box_second_part.move(m)
    next_box_part_val = grid.value_at(box_second_part)
    moved = None
    if next_box_part in obstacles or moved_box in obstacles:
        moved = False
    if (m == right or m == left) and next_box_part in boxes:
        moved = move_an_enlarged_box(next_box_part, m, obstacles, boxes, grid)
    if (m == down or m == up) and (next_box_part in boxes or moved_box in boxes):
        is_movable = is_enlarged_box_movable(moved_box, m, obstacles, boxes, grid) and is_enlarged_box_movable(next_box_part, m, obstacles, boxes, grid)
        if is_movable:
            move_an_enlarged_box(moved_box, m, obstacles, boxes, grid)
            move_an_enlarged_box(next_box_part, m, obstacles, boxes, grid)
        moved = is_movable
    if next_box_part not in obstacles and next_box_part not in boxes and moved_box not in obstacles and (moved_box not in boxes or moved_box == box_second_part):
        moved = True
    if moved:
        grid.set_at(box, '.')
        grid.set_at(box_second_part, '.')
        boxes.remove(box)
        boxes.remove(box_second_part)
        boxes.add(moved_box)
        boxes.add(next_box_part)
        grid.set_at(moved_box, moved_box_val)
        grid.set_at(next_box_part, next_box_part_val)
    return moved


def make_a_move_enlarged(start, m, obstacles, boxes, grid):
    moved = start.move(m)
    if moved not in obstacles and moved not in boxes:
        return moved
    if moved in obstacles:
        return start
    if grid.value_at(moved) == '[' or grid.value_at(moved) == ']':
        box_moved = move_an_enlarged_box(moved, m, obstacles, boxes, grid)
        if box_moved:
            return moved
        else:
            return start


def enlarge(input_map):
    res = []
    for rr in input_map:
        new_row = []
        for rv in rr:
            if rv == '#':
                new_row.append('#')
                new_row.append('#')
            if rv == 'O':
                new_row.append('[')
                new_row.append(']')
            if rv == '@':
                new_row.append('@')
                new_row.append('.')
            if rv == '.':
                new_row.append('.')
                new_row.append('.')
        res.append(new_row)
    return res


def resolve_part2(data):
    res = 0
    input_map = data[0]
    moves = data[1]

    input_map_enlarged = enlarge(input_map)

    grid = Grid(input_map_enlarged)

    start = grid.find('@')
    obstacles = grid.find_all('#')
    boxes_starts = grid.find_all('[')
    boxes_ends = grid.find_all(']')

    boxes = boxes_starts.union(boxes_ends)

    m = None

    for move in moves:
        if move == '^':
            m = up
        if move == '>':
            m = right
        if move == '<':
            m = left
        if move == 'v':
            m = down
        prev = start
        start = make_a_move_enlarged(start, m, obstacles, boxes, grid)
        grid.set_at(prev, '.')
        grid.set_at(start, '@')


    for box in boxes:
        if grid.value_at(box) == '[':
            res += 100 * box.x + box.y

    return res


if __name__ == "__main__":
    example_expectation_part1 = 2028
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case #1 has passed for the part 1")
    example_expectation_part1 = 10092
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case #1 has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 9021
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))