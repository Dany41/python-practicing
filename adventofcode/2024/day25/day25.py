def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        box = []
        for line in file:
            if line == '\n':
                lines.append(box)
                box = []
                continue
            box.append(list(line.replace('\n', '')))
    lines.append(box)
    return lines


def get_heights(box):
    heights = []
    n = len(box)
    m = len(box[0])
    i = 0
    for j in range(m):
        count = 0
        for i in range(n):
            if box[i][j] == '#':
                count += 1
        heights.append(count)
    return heights


def boxes_fit(box1, box2):
    for i in range(len(box1)):
        if box1[i] + box2[i] > 7:
            return False
    return True


def resolve_part1(data):
    res = 0

    keys = []
    locks = []

    for box in data:
        if box[0][0] == '#':
            locks.append(box)
        else:
            keys.append(box)

    key_heights = []
    for key in keys:
        key_heights.append(get_heights(key))
    lock_heights = []
    for lock in locks:
        lock_heights.append(get_heights(lock))
    for kh in key_heights:
        for lh in lock_heights:
            if boxes_fit(kh, lh):
                res += 1




    return res


if __name__ == "__main__":
    example_expectation_part1 = 3
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))