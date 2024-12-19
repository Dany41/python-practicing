from utils.grid import Grid
from utils.point import Point, Direction


def upload_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove empty lines and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]

    # First line: name patterns
    if lines:
        name_patterns = lines[0].split(", ")
        designs = lines[1:]
        return name_patterns, designs
    else:
        return None, None


def can_be_made(design: str, patterns, no_in_patterns):
    if len(design) == 0:
        return True
    if design in no_in_patterns:
        return False
    match = False
    for pattern in patterns:
        p_n = len(pattern)
        if design[:p_n] == pattern:
            match = match or can_be_made(design[p_n:], patterns, no_in_patterns)

    if not match:
        no_in_patterns.add(design)

    return match


def resolve_part1(data):

    res = 0

    patterns, designs = data
    patterns = sorted(patterns, reverse=True, key=lambda x: len(x))
    no_in_patterns = set()
    for design in designs:
        if can_be_made(design, patterns, no_in_patterns):
            res += 1

    return res


def different_ways_can_be_made(design: str, patterns, no_in_patterns, can_be_made_dict, accumulator):
    if len(design) == 0:
        return 1
    if design in can_be_made_dict:
        return can_be_made_dict[design]
    if design in no_in_patterns:
        return 0
    count = 0
    for pattern in patterns:
        p_n = len(pattern)
        if design[:p_n] == pattern:
            count += different_ways_can_be_made(design[p_n:], patterns, no_in_patterns, can_be_made_dict, accumulator)

    if count == 0:
        no_in_patterns.add(design)
    else:
        can_be_made_dict[design] = count
    accumulator += count

    return accumulator


def resolve_part2(data):
    res = 0

    patterns, designs = data
    patterns = sorted(patterns, reverse=True, key=lambda x: len(x))
    no_in_patterns = set()
    can_be_made_dict = {}
    for design in designs:
        if can_be_made(design, patterns, no_in_patterns):
            res += different_ways_can_be_made(design, patterns, no_in_patterns, can_be_made_dict, 0)

    return res


if __name__ == "__main__":
    example_expectation_part1 = 6
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = 16
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))