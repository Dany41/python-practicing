from dataclasses import dataclass


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            split_lines = line.replace('\n', '').split(": ")
            lines.append([split_lines[0]] + split_lines[1].split(" "))
    return lines

@dataclass
class Equation:
    test_value: int
    candidates: []


def can_test_value_be_reached(test_value, candidates, accumulator = 0):
    if accumulator == test_value and not candidates:
        return True
    elif test_value < accumulator or not candidates:
        return False
    else:
        return can_test_value_be_reached(test_value, candidates[1:], accumulator + candidates[0]) or can_test_value_be_reached(test_value, candidates[1:], accumulator * candidates[0])



def resolve_part1(lines):
    res = 0
    equations = []
    for line in lines:
        equations.append(Equation(int(line[0]), list(map(lambda x: int(x), line[1:]))))

    for equation in equations:
        if can_test_value_be_reached(equation.test_value, equation.candidates):
            res += equation.test_value

    return res

def can_test_value_be_reached_part2(test_value, candidates, accumulator):
    if accumulator == test_value and not candidates:
        return True
    elif test_value < accumulator or not candidates:
        return False
    else:
        return (can_test_value_be_reached_part2(test_value, candidates[1:], accumulator + candidates[0]) or
                can_test_value_be_reached_part2(test_value, candidates[1:], accumulator * candidates[0]) or
                can_test_value_be_reached_part2(test_value, candidates[1:], int(str(accumulator) + str(candidates[0]))))



def resolve_part2(lines):
    res = 0
    equations = []
    for line in lines:
        equations.append(Equation(int(line[0]), list(map(lambda x: int(x), line[1:]))))

    for equation in equations:
        if can_test_value_be_reached_part2(equation.test_value, equation.candidates, 0):
            res += equation.test_value

    return res


if __name__ == "__main__":
    example_expectation_part1 = 3749
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 11387
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))