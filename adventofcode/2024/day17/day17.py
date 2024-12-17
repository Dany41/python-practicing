import math

from utils.grid import Grid
from utils.point import Point


def upload_input(file_path):
    data = {
        "registers": {},
        "program": []
    }

    # Read and parse the file
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Register"):
                # Parse registers
                key, value = line.split(":")
                data["registers"][key.strip()] = int(value.strip())
            elif line.startswith("Program"):
                # Parse program
                _, program_values = line.split(":")
                data["program"] = list(map(int, program_values.strip().split(",")))
    return data


def get_combo(val, r_a, r_b, r_c):
    if val < 4:
        return val
    if val == 4:
        return r_a
    if val == 5:
        return r_b
    if val == 6:
        return r_c
    raise Exception("Unexpected val for combo " + str(val))


def execute_program(program, r_a, r_b, r_c):

    pointer = 0
    output = []
    n = len(program)

    while pointer < n:
        opcode = program[pointer]
        literal = program[pointer + 1]
        combo = get_combo(literal, r_a, r_b, r_c)
        if opcode == 0:
            r_a = math.floor(r_a / (2 ** combo))
        if opcode == 1:
            r_b ^= literal
        if opcode == 2:
            r_b = combo % 8
        if opcode == 3:
            if r_a != 0:
                pointer = literal
                continue
        if opcode == 4:
            r_b ^= r_c
        if opcode == 5:
            output.append(combo % 8)
        if opcode == 6:
            r_b = math.floor(r_a / (2 ** combo))
        if opcode == 7:
            r_c = math.floor(r_a / (2 ** combo))
        pointer += 2

    return output


def resolve_part1(data):
    return execute_program(data["program"], data["registers"]["Register A"], 0, 0)


def execute_program_with_compare(program, r_a, r_b, r_c, expected):

    pointer = 0
    pointer_exp = 0
    output = []
    n = len(program)
    m = len(expected)

    while pointer < n:
        opcode = program[pointer]
        literal = program[pointer + 1]
        combo = get_combo(literal, r_a, r_b, r_c)
        if opcode == 0:
            r_a = math.floor(r_a / (2 ** combo))
        if opcode == 1:
            r_b ^= literal
        if opcode == 2:
            r_b = combo % 8
        if opcode == 3:
            if r_a != 0:
                pointer = literal
                continue
        if opcode == 4:
            r_b ^= r_c
        if opcode == 5:
            if pointer_exp >= m or combo % 8 != expected[pointer_exp]:
                return []
            else:
                pointer_exp += 1
                output.append(combo % 8)
        if opcode == 6:
            r_b = math.floor(r_a / (2 ** combo))
        if opcode == 7:
            r_c = math.floor(r_a / (2 ** combo))
        pointer += 2

    return output


def resolve_part2(data):

    program = data["program"]
    output = execute_program(program, data["registers"]["Register A"], 0, 0)

    r_a = 13427091588403*8

    while not output.__eq__(program): # [1,->]1678386448550; 3,-> 13427091588403
        r_a += 1

        output = execute_program(program, r_a, 0, 0)


    return r_a


if __name__ == "__main__":
    example_expectation_part1 = [4,6,3,5,6,3,5,2,1,0]
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + ",".join(map(str, part_1_solution)))
    assert part_1_solution == [2,1,3,0,5,2,3,7,1]

    # example_expectation_part2 = 117440
    # uploaded_example_input = upload_input("example2.txt")
    # result_ex_part2 = resolve_part2(uploaded_example_input)
    # print("Example output is " + str(result_ex_part2))
    # assert result_ex_part2 == example_expectation_part2
    # print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))