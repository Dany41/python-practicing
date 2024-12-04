import math
from collections import Counter


def upload_input(file_path):
    left_column = []
    right_column = []
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into two integers
            left, right = map(int, line.split())
            # Append each integer to the appropriate list
            left_column.append(left)
            right_column.append(right)
    return [left_column, right_column]


def resolve_part1(left_list, right_list):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    n = len(left_list)
    i = 0
    res = 0
    while i < n:
        res += math.fabs(sorted_left_list[i] - sorted_right_list[i])
        i += 1
    return int(res)


def resolve_part2(left_list, right_list):
    n = len(left_list)
    ll_counts = Counter(right_list)
    i = 0
    res = 0
    while i < n:
        curr = left_list[i]
        res += curr * ll_counts[curr]
        i += 1
    return res


if __name__ == "__main__":
    example_expectation_part1 = 11
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input[0], uploaded_example_input[1])
    assert result_ex_part1 == 11
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input[0], uploaded_input[1])))

    result_ex_part2 = resolve_part2(uploaded_example_input[0], uploaded_example_input[1])
    assert result_ex_part2 == 31
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input[0], uploaded_input[1])))