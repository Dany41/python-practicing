from functools import cache


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            return line.split(" ")


def resolve(line, num):
    res = 0

    for x in line:
        res += recursive_blinking(x, num)

    return res


def blink(val):
    if int(val) == 0:
        return ["1"]
    elif len(val) % 2 == 0:
        return [str(int(val[:int(len(val) / 2)])), str(int(val[int(len(val) / 2):]))]
    else:
        return [str(int(val) * 2024)]


@cache
def recursive_blinking(val, blink_count):
    if blink_count == 0:
        return 1
    res = 0
    for x in blink(val):
        tmp = recursive_blinking(x, blink_count - 1)
        res += tmp
    return res


if __name__ == "__main__":
    example_expectation_part1 = 55312
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve(uploaded_example_input, 25)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve(uploaded_input, 25)))


    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve(uploaded_input, 75)
    print("Part2 answer is: " + str(part_2_res))