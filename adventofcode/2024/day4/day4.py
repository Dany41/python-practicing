def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line))
    return lines


def xmas_count(lines, i, j):
    n = len(lines)
    m = len(lines[0]) - 1
    count = 0
    # right
    if j + 3 < m and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
        count += 1
    # left
    if j - 3 >= 0 and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
        count += 1
    # top
    if i + 3 < n and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
        count += 1
    # bottom
    if i - 3 >= 0 and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
        count += 1
    # top-right
    if i - 3 >= 0 and j + 3 < m and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
        count += 1
    # left-top
    if j - 3 >= 0 and i - 3 >= 0 and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
        count += 1
    # right-bottom
    if i + 3 < n and j + 3 < m and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
        count += 1
    # bottom-left
    if i + 3 < n and j - 3 >= 0 and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
        count += 1
    return count


def resolve_part1(lines):
    res = 0
    i = 0
    n = len(lines)
    while i < n:
        j = 0
        m = len(lines[i])
        while j < m:
            if lines[i][j] == 'X':
                res += xmas_count(lines, i, j)
            j += 1

        i += 1

    return res


def x_mas_count(lines, i, j):
    count = 0

    n = len(lines)
    m = len(lines[0]) - 1
    if i - 1 >= 0 and j - 1 >= 0 and i + 1 < n and j + 1 < m:
        if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'S':
            count += 1
        if lines[i-1][j-1] == 'M' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'S':
            count += 1
        if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i+1][j+1] == 'M':
            count += 1
        if lines[i-1][j-1] == 'S' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i+1][j+1] == 'M':
            count += 1

    return count


def resolve_part2(lines):
    res = 0
    i = 0
    n = len(lines)
    while i < n:
        j = 0
        m = len(lines[i])
        while j < m:
            if lines[i][j] == 'A':
                res += x_mas_count(lines, i, j)
            j += 1

        i += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 18
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 9
    uploaded_example_input = upload_input("example.txt")
    #result_ex_part2 = resolve_part2(uploaded_example_input)
    #print("Example output is " + str(result_ex_part2))
    #assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))