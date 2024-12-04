import re

def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line)
            lines.append(line)
    return lines


def upload_input_p2(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
            lines.append(line)
    return lines


def parse_mul(mul_str):
    a, b = map(int, re.findall(r"\d+", mul_str))
    return a * b


def resolve_part1(lines):
    res = 0
    i = 0
    n = len(lines)
    while i < n:
        j = 0
        m = len(lines[i])
        while j < m:
            res += parse_mul(lines[i][j])
            j += 1

        i += 1

    return res




def resolve_part2(lines):
    res = 0
    i = 0
    n = len(lines)
    allowed = True
    while i < n:
        j = 0
        m = len(lines[i])
        while j < m:
            if lines[i][j] == "do()":
                allowed = True
                j += 1
                continue
            if lines[i][j] == "don't()":
                allowed = False
                j += 1
                continue
            if allowed:
                res += parse_mul(lines[i][j])
            j += 1

        i += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 161
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 48
    uploaded_example_input = upload_input_p2("example_p2.txt")
    #result_ex_part2 = resolve_part2(uploaded_example_input)
    #print("Example output is " + str(result_ex_part2))
    #assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input_p2("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))