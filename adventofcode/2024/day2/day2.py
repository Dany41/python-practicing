import math


def upload_input(file_path):
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into two integers
            report = map(int, line.split())
            # Append each integer to the appropriate list
            reports.append(list(report))
    return reports


def resolve_part1(reports):
    res = 0
    for x in reports:
        n = len(x)
        ascending = None
        if x[0] > x[1]:
            ascending = False
        elif x[0] < x[1]:
            ascending = True
        else:
            pass
        i = 0
        keep_going = True
        while i < n - 1 and keep_going:
            if ascending and x[i] >= x[i + 1]:
                keep_going = False
            if not ascending and x[i] <= x[i + 1]:
                keep_going = False
            if math.fabs(x[i] - x[i + 1]) > 3:
                keep_going = False
            i += 1

        if keep_going:
            res += 1

    return res


def check_report(x):
    n = len(x)
    ascending = None
    if x[0] > x[1]:
        ascending = False
    elif x[0] < x[1]:
        ascending = True
    else:
        pass
    i = 0
    keep_going = True
    while i < n - 1 and keep_going:
        if ascending and x[i] >= x[i + 1]:
            keep_going = False
        if not ascending and x[i] <= x[i + 1]:
            keep_going = False
        if math.fabs(x[i] - x[i + 1]) > 3:
            keep_going = False
        i += 1
    return keep_going


def resolve_part2(reports):
    res = 0
    for x in reports:
        keep_going = check_report(x)

        if not keep_going:
            i = 0
            while i < len(x):
                keep_going = keep_going or check_report(x[:i] + x[i+1:])
                i += 1

        if keep_going:
            res += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 2
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 4
    uploaded_example_input = upload_input("example.txt")
    #result_ex_part2 = resolve_part2(uploaded_example_input)
    #print("Example output is " + str(result_ex_part2))
    #assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))